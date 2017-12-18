import datetime
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from geupsikbot import geupsik
from geupsikbot.models import Menu


def keyboard(request):

    return JsonResponse({
        'type' : 'buttons',
        'buttons' : ['중식', '석식', '외식']
    })

@csrf_exempt

def answer(request):
    json_str = ((request.body).decode('utf-8)'))
    received_json_data = json.loads(json_str)
    geupsik_time = received_json_data['content']
    today_date =datetime.date.today().strftime("%m월 %d일")

    return JsonResponse({
        'message': {
            'text': today_date + '의' + geupsik_time+ '메뉴입니다.' #+ get_menu(geupsik_time)
        },
        'keyboard': {
            'type': 'buttons',
            'buttons': ['중식', '석식', '외식']
        }

    })


def crawl(request):
    menu_db = Menu.objects.all()
    menu_db.delete()

    #menus = geupsik.menuParsing(datetime.date.year, datetime.date.month, datetime.date.day)
    f=open('menuPaper.txt','r')
    menus=[]
    menus.append(f.read())
    menus.append(f.read())
    create_menu_db(menus[0], menus[1])
    return 0


def create_menu_db(slunch, sdinner):
    Menu.objects.create(
        lunch=slunch,
        dinner=sdinner
    )

def get_menu(time):
    f = open('menuPaper.txt', 'r')
    menus = []
    menus.append(f.read())
    menus.append(f.read())
    #if time is '중식':
    #    menus=Menu.object.lunch.split()
    #
    #elif time is '석식':
    #    menus = Menu.object.dinner.split()

    str='-------------\n'
    for i in menus:
        str+=i+"\n"
    return str
