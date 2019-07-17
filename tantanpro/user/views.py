from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from common.utils import is_phone_num
from common import errors, cache_keys
from libs.http import render_json
from user import logics
from user.models import User


def login(request):
    phone_num = request.POST.get("phonenum",'')
    code = request.POST.get("code",'')
    phone_num = phone_num.strip()
    code = code.strip()
    cache_code = cache.get(cache_keys.CACHE_CODE_KEYS.format(phone_num))
    if cache_code !=code:
        return render_json(code =errors.VERIFY_CODE_ERROR)
    user,created = User.objects.get_or_create(phonenum=phone_num)

    request.session['uid'] = user.id

    return render_json(data=User.to_dict(phone_num))





def verify_phone(request):
    #获取号码
    phonenum = request.POST.get('phonenum')
    #判断是否为数字
    if is_phone_num(phonenum):

        #发送验证码
        logics.send_verify_code(phonenum)

        #返回JSON数据
        return render_json()
    else:
        return render_json(code=errors.PHONE_NUM_ERROR)


