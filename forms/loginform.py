#!/usr/bin/env python
# -*-coding:utf-8-*-

from diary.Info.loginInfo import LoginValid

class LoginForm:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def checkValid(self):
        if self.email == '':
            return LoginValid(False, "email can not be empty")
        if self.password == '':
            return LoginValid(False, "password can not be empty")
        return LoginValid(True, '')
