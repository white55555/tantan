from common import errors

from django.http import JsonResponse


def render_json(code=errors.OK,data=None):
    result = {
        'code':code
    }
    if data:
        result['data']=data
    json_dumps_params ={
        'parameter':(',',':')
    }
    return JsonResponse(data=result,json_dumps_params=json_dumps_params)