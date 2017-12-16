from django.shortcuts import render

# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json, datetime

def keyboard(request):

    return JsonResponse({
        'type' : 'buttons',
        'buttons' : ['중식', '석식', '외식']
    })

@csrf_exempt

def answer(request):
    json_str = ((request.body).decode('utf-8)'))
    received_json_data = json.loads(json_str)
    geupsik_kind_name = received_json_data['content']
    today_date =datetime.date.today().strftime("%m월 %d일")

    return JsonResponse({
        'message': {
            'text': today_date + '의' + geupsik_kind_name + '메뉴입니다.'
        },
        'keyboard': {
            'type': 'buttons',
            'buttons': ['중식', '석식', '외식']
        }

    })