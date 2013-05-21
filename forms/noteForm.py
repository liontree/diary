#e# -*-coding:utf-8-*-

from lemonbook.functionlib.checkInfo import IsValid

class EditForm:
    def __init__(self, contents):
        self.contents = contents

    def checkSubmit(self):
        if self.contents == '':
            return IsValid(False, u'请输入文字')
        return IsValid(True, '')
