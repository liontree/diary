#!/usr/bin/env python
# -*-coding:utf-8-*-

from lemondiary.Info.loginInfo import LoginValid

class LoginForm:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def checkValid(self):
        if self.email == '':
            return LoginValid(False, "请输入正确的邮箱/手机号")
        if self.password == '':
            return LoginValid(False, "请输入密码")
        return LoginValid(True, '')
