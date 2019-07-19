from django.core.cache import cache

from common import utils
from libs import sms

CACHE_CODE_KEYS = 'verify_code:{}'

# def send_verify_code(phone_num):
#     code = utils.gen_random_code(6)
#     ret = sms.send_verify_code(phone_num,code)
#     if ret:
#         ret = cache.set('verify_code:13843834819',code,3*60)
#     return ret