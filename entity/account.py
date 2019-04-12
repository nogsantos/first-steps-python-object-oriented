# -*- coding: utf-8 -*-


class Account:

    def __init__(self, number, client, balance, credit_limit):
        self.__number = number
        self.__client = client
        self.__balance = balance
        self.__credit_limit = credit_limit

    def set_credit_limit(self, value):
        self.__credit_limit = value

    def balance(self):
        return self.__balance

    def credit(self, value):
        self.__balance += value

    def debit(self, value):
        if self.__can_debit(value):
            self.__balance -= value
        else:
            print("The value {} passing the limit".format(value))

    def transfer(self, value, destiny):
        self.debit(value)
        destiny.credit(value)

    def __can_debit(self, value):
        available_value = self.__balance + self.__credit_limit
        return value <= available_value

    @property
    def credit_limit(self):
        return self.__credit_limit

    @credit_limit.setter
    def credit_limit(self, value):
        self.__credit_limit = value

    @staticmethod
    def banks_codes():
        return {
            "Brazil": "001",
            "Caixa": "003",
        }
