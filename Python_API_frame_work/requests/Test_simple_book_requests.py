import random

from Python_API_frame_work.request_methods.api_methods import Rest_api_methods
from random import randint
class Test_Simple_books(Rest_api_methods):
    Rest_api_methods.base_url = r'https://simple-books-api.glitch.me'
    END_payload_file = r"../json_files/pay_load_file.json"
    test_data_file = r"../json_files/test_data.json"

    def test_getting_access_token(self):
        data_dict = self.json_data_reading(self.END_payload_file)
        data_dict[1]["Gen_token_body"].update(clientEmail=f'kasimohana{randint(1900,2100)}robo@gmail.com')
        token_data = self.post_requests(data_dict[0]["Gen_token_END_POINT"], data_dict[1]["Gen_token_body"])
        self.json_tets_data_writing(self.test_data_file,token_data.json())
        print(token_data.json())
        assert token_data.status_code == 201

    def test_create_order(self):
        acc_token = self.json_data_reading(self.test_data_file)
        End_point = self.json_data_reading(self.END_payload_file)[0]["Create_order_END_POINT"]
        body = self.json_data_reading(self.END_payload_file)[1]["create_order_body"]
        response = self.post_requests(End_point, body, acc_token['accessToken'])
        acc_token.update(id=response.json()['orderId'])
        self.json_tets_data_writing(self.test_data_file, acc_token)
        print(response.json())
        assert response.status_code == 201

    def test_get_book(self):
        order_details = self.json_data_reading(self.test_data_file)
        end_point = self.json_data_reading(self.END_payload_file)[0]["Get_order_END_POINT"]+str(order_details['id'])
        res = self.get_request(end_point, order_details['accessToken'])
        print(res.json())
        assert res.status_code == 200

    #
    def test_deleting_a_book(self):
        order_details = self.json_data_reading(self.test_data_file)
        end_point = self.json_data_reading(self.END_payload_file)[0]["Get_order_END_POINT"] + str(order_details['id'])
        response = self.delete_request(end_point, order_details['accessToken'])
        assert response.status_code == 204


run1 = Test_Simple_books()
run1.test_getting_access_token()
run1.test_create_order()
run1.test_get_book()
run1.test_deleting_a_book()