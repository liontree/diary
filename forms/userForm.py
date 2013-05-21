#!/usr/bin/env python
# -*-coding:utf-8-*-

from lemonbook.functionlib.checkInfo import IsValid

class LoginForm:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def checkValid(self):
        if self.email == '':
            return IsValid(False)
        if self.password == '':
            return IsValid(False)
        return IsValid(True)

class RegisterForm:
    def __init__(self, email, password, username):
        self.email = email
        self.password = password
        self.username = username

    def checkValid(self):
        if self.email == '':
            return IsValid(False)
        if self.password == '':
            return IsValid(False)
        if self.username == '':
            return IsValid(False)
        return IsValid(True)
