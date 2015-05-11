from django.http import HttpResponse
import json

class JsonResponse(HttpResponse):
    def __init__(self, content={}, mimetype=None, status=None,
             content_type='application/json'):
        super(JsonResponse, self).__init__(json.dumps(content), mimetype=mimetype,
                                           status=status, content_type=content_type)
                                           
@dajaxice_register
def dajaxice_example(request):
    resp_data = {'my_key': 'my value',}
    return JsonResponse(resp_data)