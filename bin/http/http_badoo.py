import requests


class http:
    login = ""
    password = ""

    def __init__(self, login, password):
        self.login = str(login)
        self.password = str(password)

    @property
    def login(self):
        return self.login

    @login.setter
    def login(self, value):





