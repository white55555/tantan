import os
import time

from django.conf import settings
from django.core.cache import cache
from common.utils import is_phone_num
from common import errors, cache_keys
from libs.http import render_json
from user import logics
from user.form import ProfileForm
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

    return render_json(data=user.to_dict())





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


def get_profile(request):
    user = request.user

    return render_json(data=user.profile.to_dict(exclude=['auto_play']))


def set_profile(request):
    user = request.user
    form = ProfileForm(data=request.POST,instance=user.profile)

    if form.is_valid():
        form.save()
        return render_json()
    else:
        return render_json(data=form.errors)


def get_avatar(request):
    user = request.user
    avatar = request.FILES.get('avatar')
    file_name='avatat-{}'.format(int(time.time()))
    #file_path = os.path.join(settings.MADIA_URL,'madia')
    # with open(file_path,'wb+') as e:
    #     for chunk in avatar.chunks:
    #         e.writer(chunk)
    # return render_json()
    file_path = logics.upload_avatar(file_name,avatar)

    ret = logics.upload_qiniuyun(file_name,file_path)
    return ret