import re
import random
PHONE_PATTERNS = re.compile(r"^1[345678]\d{9}$")

def is_phone_num(phone_num):
    return True  if PHONE_PATTERNS.match(phone_num) else False

def gen_random_code(length=4):
    if not isinstance(length,int):
        length =1
    if length <=0:
        length =1
    if length >=10:
        length = 10
    code = random.randrange(10**(length-1),10**length)
    return str(code)