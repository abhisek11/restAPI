import json
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render
from django.views.generic import View

from restapi.mixin import JsonResponseMixin
from .models import Update
# Create your views here.

def update_model_detail_view(request):

    data ={
        "count":1000,
        "content":"some new content"
    }
    json_data=json.dumps(data)
    return HttpResponse(json_data,content_type='application/json')
    # return JsonResponse(data)

class JsonCBV(View):
    def get(self,request,*args,**kwargs):

        data ={
            "count":1000,
            "content":"some new content"
        }
        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin,View):
    def get(self,request,*args,**kwargs):

        data ={
            "count":1000,
            "content":"some new content"
        }
        return self.render_to_json_response(data)