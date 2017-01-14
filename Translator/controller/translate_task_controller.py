from django_url_framework.controller import ActionController
from Translator.util.TplHelper import *
from Translator.model.translate_messages import TranslateMessages

class TranslateTaskController(ActionController):

    def task(self,request):
        messages = TranslateMessages.objects.filter(message_translate='',del_flag=False).order_by('message_id')[0:10]

        return getTpl({'messages':messages},'translate_task/task')

    def submit(self,request):
        user = request.session['user']
        messageId = request.GET['messageId']
        translateMsg = request.GET['translateMsg']

        effectRows = TranslateMessages.objects.filter(message_id=messageId,message_translate='').\
                update(message_translate=translateMsg,translator_id=user.translator_id)
        if effectRows == 0:
            return HttpResponse("false")
        else:
            return HttpResponse("true")

    def finished(self,request):
        user = request.session['user']
        messages = TranslateMessages.objects.filter(translator_id=user.translator_id,del_flag=False).order_by('message_id')[0:10]

        return getTpl({'messages':messages},'translate_task/finished')
