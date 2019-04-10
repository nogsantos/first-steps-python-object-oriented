# -*- coding: utf-8 -*-


def create_account(number, client, balance, credit_limit):
    account = {
        "number": number,
        "client": client,
        "balance": balance,
        "credit_limit": credit_limit,
    }
    return account
