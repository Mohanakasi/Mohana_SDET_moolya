import random

from request_methods.api_methods import Rest_api_methods
from random import randint
class Test_Simple_books_class(Rest_api_methods):
    Rest_api_methods.base_url = r'https://simple-books-api.glitch.me'
    Rest_api_methods.END_payload_file = r"../json_files/pay_load_file.json"
    Rest_api_methods.test_data_file_path = r"../json_files/test_data.json"


    def test_getting_access_token(self):
        self.randam_email_update()
        response = self.post_requests("Gen_token_END_POINT", "Gen_token_body")
        self.json_data_writing(self.test_data_file_path,response.json())
        print(response.json())
        assert response.status_code == 201

    def test_create_order(self):
        response = self.post_requests("Create_order_END_POINT", "create_order_body", "accessToken")
        self.json_data_writing(self.test_data_file_path, response, new_data_key="id", value=response.json()["orderId"])
        print(response.json())
        assert response.status_code == 201


    def test_get_book(self):
        order_id = self.extra_path_parametrization(self.test_data_file_path, 'id')
        response = self.get_request(f"Get_order_END_POINT", 'accessToken', Extra_path=order_id)
        print(response.json())
        assert response.status_code == 200


    def test_deleting_a_book(self):
        order_id = self.extra_path_parametrization(self.test_data_file_path, 'id')
        response = self.delete_request("Get_order_END_POINT", "accessToken", extra_path=order_id)
        assert response.status_code == 204


#
# run1 = Test_Simple_books_class()
# run1.test_getting_access_token()
# run1.test_create_order()
# run1.test_get_book()
# run1.test_deleting_a_book()