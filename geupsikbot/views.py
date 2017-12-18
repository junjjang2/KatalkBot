from _datetime import datetime
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from geupsikbot.models import Menu

tday=datetime.now().date()

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
    today_date =str(tday.month)+ "." + str(tday.day)

    return JsonResponse({
        'message': {
            'text': today_date + '의' + geupsik_time+ '메뉴입니다.' + get_menu(tday)
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
    get_menu(tday)
    f= open("menuPaper.txt", 'r')
    lines = f.readlines()
    sl=""
    sd=""
    for l in lines:
        l=l.split("!")
        if l[0] is datetime.date():
            sl=l[1]
            sd=l[2]

    create_menu_db(tday, sl, sd)
    return 0


def create_menu_db(today, slunch, sdinner):
    Menu.objects.create(
        date=today,
        lunch=slunch,
        dinner=sdinner
    )
def get_menu(today):
    sl=Menu.objects.get(date=today).lunch
    sd=Menu.objects.get(date=today).dinner

    return "---------------\n" + "중식\n"+ sl \
           + "---------------\n" + "석식\n" + sd \
           + "---------------"