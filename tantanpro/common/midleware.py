from django.utils.deprecation import MiddlewareMixin

from common import errors
from libs.http import render_json
from user.models import User


class Midleware(MiddlewareMixin):
    def process_request(self,request):
        '''
        path('login/',login,name='login'),
        path('verify_phone/',verify_phone,name='verify_phone'),

        :param request:
        :return:
        '''
        WHITE_LIST = [
            'app/login/',
            'app/verify_phone'
        ]
        if request.path in WHITE_LIST:
            return
        uid = request.session.get('uid')
        if not uid:
            return render_json(code=errors.LOGIN_NOUID_ERROR)
        request.user = User.objects.get(pk =uid)