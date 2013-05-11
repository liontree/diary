#!/usr/bin/env python
# -*-coding:utf-8-*-

from lemondiary.Info.checkInfo import IsValid

class LoginForm:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def checkValid(self):
        if self.email == '':
            return IsValid(False, "请输入正确的邮箱")
        if self.password == '':
            return IsValid(False, "请输入密码")
        return IsValid(True, '')

class RegisterForm:
    def __init__(self, email, password, username):
        self.email = email
        self.password = password
        self.username = username

    def checkValid(self):
        if self.email == '':
            return IsValid(False, "请输入正确的邮箱")
        if self.password == '':
            return IsValid(False, "请输入密码")
        if self.username == '':
            return IsValid(False, "你忘了留下名号了")
        return IsValid(True, '')
