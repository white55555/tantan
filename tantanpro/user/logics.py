from django.core.cache import cache
from common import cache_keys
from common import utils
from libs import sms
from libs.http import render_json


def send_verify_code(phone_num):
    #生成验证码
    code = utils.gen_random_code(6)
    #发送验证码
    ret = sms.send_verify_code(phone_num,code)
    if ret:
        ret = cache.set(cache_keys.CACHE_CODE_KEYS.format(phone_num))
    return ret

