from django_url_framework.controller import ActionController
from Translator.util.TplHelper import *
from Translator.model.translator_user import TranslatorUser
from Translator.model.trans_money import TransMoney
from Translator.model.translate_messages import TranslateMessages

class SettingController(ActionController):

    def user_info(self,request):
        user = request.session['user']
        return getTpl({'user':user},'setting/userInfo')

    def trans_money(self,request):
        user = request.session['user']
        lastTransMoney = TransMoney.objects.filter(translator_id=user.translator_id).order_by('-trans_id')
        if len(lastTransMoney) == 0:
            lastTranslateMessageId = 0;
        else:
            lastTranslateMessageId = lastTransMoney[0].last_translate_message_id
        count = TranslateMessages.objects.filter(translator_id=user.translator_id,message_id__gt=lastTranslateMessageId).count()
        print count
        return getTpl({'count':count},'setting/transMoney')