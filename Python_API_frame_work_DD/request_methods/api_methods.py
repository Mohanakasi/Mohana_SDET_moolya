import requests
import json
import re

class Rest_api_methods:
    base_url = ''
    END_payload_file = ''
    test_data_file_path = ''

    def get_request(self, end_point_key, authentication_key='', Extra_path=''):
        if not authentication_key:
            json_EP_data  = self.json_data_reading(self.END_payload_file)
            response = requests.get(self.base_url+json_EP_data[end_point_key]+Extra_path)
            return response
        elif authentication_key:
            json_EP_data = self.json_data_reading(self.END_payload_file)
            json_test_data = self.json_data_reading(self.test_data_file_path)
            Acc_token = {'Authorization': 'Bearer ' + json_test_data[authentication_key]}
            response = requests.get(self.base_url+json_EP_data[0][end_point_key]+Extra_path, headers=Acc_token)
            return response


    def post_requests(self, end_point_key, body_key, authentication_key='', extra_path=''):
        if not authentication_key:
            json_EP_body_data = self.json_data_reading(self.END_payload_file)
            response = requests.post(self.base_url+json_EP_body_data[0][end_point_key]+extra_path,json=json_EP_body_data[1][body_key])
            return response

        elif authentication_key:
            json_test_data = self.json_data_reading(file_name=self.test_data_file_path)
            Acc_token = {'Authorization': 'Bearer ' + json_test_data[authentication_key]}
            json_EP_body_data = self.json_data_reading(self.END_payload_file)
            response = requests.post(self.base_url+json_EP_body_data[0][end_point_key]+extra_path,json=json_EP_body_data[1][body_key], headers=Acc_token)
            return response


    def delete_request(self, end_point_key, authentication_key='',extra_path=''):
        json_EP_data = self.json_data_reading(self.END_payload_file)
        json_test_data = self.json_data_reading(self.test_data_file_path)
        Acc_token = {'Authorization': 'Bearer ' + json_test_data[authentication_key]}
        response = requests.delete(self.base_url+json_EP_data[0][end_point_key]+extra_path, headers=Acc_token)
        return response

    def extra_path_parametrization(self, test_data_file, key):
           res = self.json_data_reading(test_data_file)
           return res[key]

    def randam_email_update(self):
        data_dict = self.json_data_reading(self.END_payload_file)
        email = data_dict[1]["Gen_token_body"]['clientEmail'].split('@')
        string_ = ''.join(re.findall(r"[a-zA-Z]", email[0]))
        number_= int(''.join(re.findall(r"\d", email[0])))+1
        res = string_+str(number_)+'@'+email[1]
        data_dict[1]["Gen_token_body"].update(clientEmail=res)
        self.json_data_writing(self.END_payload_file, data_dict)


    def json_data_reading(self, file_name):
        with open(fr"{file_name}", 'r') as json_file2:
            data = json.load(json_file2)
            return data


    def json_data_writing(self, file_name, data, new_data_key='', value = ''):
        if new_data_key or value:
            res = self.json_data_reading(file_name)
            res.update({new_data_key:value})
            with open(fr"{file_name}", 'w') as json_file1:
                json.dump(res, json_file1)

        elif not new_data_key or value:
            with open(fr"{file_name}", 'w') as json_file1:
                json.dump(data, json_file1)
