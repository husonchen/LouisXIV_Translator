from django_url_framework.controller import ActionController
from Translator.util.TplHelper import *
from Translator.model.translator_user import TranslatorUser
from Translator.model.trans_money import TransMoney
from Translator.model.translate_messages import TranslateMessages
from Translator.model.settings import getSetting

class SettingController(ActionController):

    def user_info(self,request):
        user = request.session['user']
        return getTpl({'user':user},'setting/userInfo')

    def trans_money(self,request):
        user = request.session['user']
        lastTransMoney = TransMoney.objects.filter(translator_id=user.translator_id).order_by('-trans_id')
        if len(lastTransMoney) == 0:
            lastTranslateMessageId = 0
        else:
            lastTranslateMessageId = lastTransMoney[0].last_translate_message_id
        count = TranslateMessages.objects.filter(translator_id=user.translator_id,message_id__gt=lastTranslateMessageId).count()
        price = float(getSetting('money','per_price'))
        total = price * count
        return getTpl({'count':count,'price':price,'total':total},'setting/transMoney')

    def trans_money_confirm(self,request):
        user = request.session['user']
        price = float(getSetting('money', 'per_price'))
        # trans before ?
        lastTransMoney = TransMoney.objects.filter(translator_id=user.translator_id).order_by('-trans_id')
        if len(lastTransMoney) == 0: # first to trans
            lastTranslateMessageId = 0
        else:
            lastTranslateMessageId = lastTransMoney[0].last_translate_message_id
        count = TranslateMessages.objects.filter(translator_id=user.translator_id,
                                                 message_id__gt=lastTranslateMessageId).count()
        nowTranslateMessateId = TranslateMessages.objects.filter(translator_id=user.translator_id).order_by('-message_id')[0].message_id
        transMoney = TransMoney(translator_id=user.translator_id,
                                last_translate_message_id=nowTranslateMessateId,
                                money_amount=price * count,
                                alipay_account=user.alipay_account)

        transMoney.save()
        return HttpResponse("true")