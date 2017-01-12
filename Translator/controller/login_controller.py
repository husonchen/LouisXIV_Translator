from django_url_framework.controller import ActionController
from Translator.util.TplHelper import *
from Translator.model.translator_user import TranslatorUser

class LoginController(ActionController):

    def hello(self,request):
        print("hello")
        for user in TranslatorUser.objects.all():
            print user
        return getTpl({},'login/hello')

    def index(self,request):
        return getTpl({},'login/login')

    def login(self,request):
        password = request.GET['password']
        email = request.GET['email']
        try :
            translator = TranslatorUser.objects.get(mail_address=email,user_password=password,del_flag=False)
        except :
            return HttpResponse("false");

        request.session['user'] = translator
        return HttpResponse("true")

    def register(self,request):
        username = request.GET['username']
        password = request.GET['password']
        email = request.GET['email']
        translator = TranslatorUser(user_name=username,user_password=password,mail_address=email)
        translator.save()
        return HttpResponse("true")
