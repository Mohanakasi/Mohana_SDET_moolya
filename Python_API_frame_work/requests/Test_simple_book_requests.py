from practice_11_11.API_frame_work.request_methods.api_methods import Rest_api_methods
from random import randint
class Test_Simple_books(Rest_api_methods):
    Rest_api_methods.base_url = r'https://simple-books-api.glitch.me'
    json_test_file = r"C:\Kasi_python_moolya\practice_11_11\API_frame_work\Data_retrieve\test_data.json"
    def test_getting_access_token(self):
        body = {
           "clientName": "Postman",
           "clientEmail": f"kasimohana{randint(1000,1218)}robo@gmail.com"
        }
        token_data = self.post_requests(r"/api-clients/", body)
        self.json_tets_data_returning(self.json_test_file,token_data.json())

    def test_create_order(self):
        body = {
          "bookId": 4,
          "customerName": "Kasi's History"
        }
        json_file_data = self.json_data_retrieving(self.json_test_file)
        response = self.post_requests(r"/orders/", body, json_file_data['accessToken'])
        json_file_data.update(id=response.json()['orderId'])
        self.json_tets_data_returning(self.json_test_file, json_file_data)
        print(response.json())

    def test_get_book(self):
        order_id = self.json_data_retrieving(self.json_test_file)['id']
        end_point = fr"/orders/{order_id}"
        json_file_data = self.json_data_retrieving(self.json_test_file)
        res = self.get_request(end_point, json_file_data['accessToken'])
        print(res.json())
        return res

    def test_deleting_a_book(self):
        json_file_data = self.json_data_retrieving(self.json_test_file)
        order_id = self.json_data_retrieving(self.json_test_file)['id']
        end_point = fr"/orders/{order_id}"
        response = self.delete_request(end_point, json_file_data['accessToken'])
        print(response)
        print(self.test_get_book())

#
# a = Test_Simple_books()
# a.test_getting_access_token()
# a.test_create_order()
# a.test_get_book()
# a.test_deleting_a_book()