from django_url_framework.controller import ActionController
from Translator.util.TplHelper import *
from Translator.model.translate_messages import TranslateMessages

class TranslateTaskController(ActionController):

    def index(self,request):
        messages = TranslateMessages.objects.filter(message_translate='',del_flag=False).order_by('message_id')[0:10]

        return getTpl({'messages':messages},'translate_task/index')
