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
        if value > self.__balance:
            return False
        self.__balance -= value
        return True

    def transfer(self, value, destiny):
        if self.debit(value):
            destiny.credit(value)
