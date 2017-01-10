from django_url_framework.controller import ActionController
from Translator.util.TplHelper import *

class LoginController(ActionController):
    def hello(self,request):
        print("hello")
        return getTpl({},'login/hello')
