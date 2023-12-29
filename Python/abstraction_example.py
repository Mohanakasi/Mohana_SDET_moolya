from abc import ABC, abstractmethod
class my_bank(ABC):

    """account data"""
    _ac_num = 5678
    ac_hol_name = 'Mohana'
    _mobile = 8886213059
    def __init__(self):
        self.register_cc_data()

    def register_cc_data(self):
        my_bank.__mpin = 1089
        my_bank.__cc_num = 9812
        my_bank.__cc_pin = 4657
        my_bank.__cc_bal = 5000
        my_bank.__class_access_pin = 1192

    #making class as abstract
    @abstractmethod
    def credit_card_data_fetch(self):
        pass

    #mpin validation
    def mpin_validation(self, pin):
        assert pin == my_bank.__mpin

    #granting autherization pin
    def authenticator(self, acc_num, mobile, mpin):
        assert acc_num == my_bank._ac_num
        assert mobile == my_bank._mobile
        assert mpin == my_bank.__mpin
        return my_bank.__class_access_pin

    #returning cc_details
    def get_the_cc_data(self, autherization_pin):
        assert my_bank.__class_access_pin == autherization_pin
        return my_bank.__cc_num, my_bank.__cc_bal


class user_access(my_bank):
    #user data creation
    def __init__(self, acc_num, mobile, mpin):
        super().__init__()
        self.acc_num = acc_num
        self.mobile = mobile
        self.__mpin = mpin
        self.mpin_validation(self.__mpin)


    #getting autheration pin
    def credit_card_data_fetch(self):
        _pin = super().authenticator(self.acc_num, self.mobile, self.__mpin)
        return _pin

    #generating cc details
    def display_credit_card_details(self):
        access_pin = self.credit_card_data_fetch()
        print(super().get_the_cc_data(access_pin))


user_transaction1 = user_access(5678, 8886213059, 1089)
user_transaction1.display_credit_card_details()