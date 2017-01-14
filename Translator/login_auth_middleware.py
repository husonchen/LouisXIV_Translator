# check user is login ,otherwish redirect it to login page
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

class LoginAuthMiddleware(MiddlewareMixin):
    def process_request(self,request):
        if request.path != '/index/' and request.path.split('/')[1] != 'login' :
            if 'user' not in request.session:
                return HttpResponseRedirect('/login/')