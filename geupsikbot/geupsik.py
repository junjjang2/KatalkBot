from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime

def schulMillParsing(year, month):

    page="http://stu.ice.go.kr"
    page+="/sts_sci_md00_001.do?"
    page+="schulCode=E100000286&"
    page+="schulCrseScCode=4&"
    page+="schulKndScCode=04&"
    page+="schYm="+str(year)+str(month) +"&"
    #print(page)
    html=urlopen(page)
    source=html.read()
    html.close()

    #source = re.sub('<br>', ' ', source)
    soup=BeautifulSoup(source, 'html.parser')

    soup=soup.select('tbody')

    data=[]
    for tr in soup[0].select('tr'):
        tr=tr.select('td')
        for td in tr:
            #data.append(td.text)
            #str.find()
            #td.find('<br/>')
            for i in td:
                arr=[]
                i=str(i)
                i=i.replace('<div>'," ")
                i=i.replace('</div>'," ")
                t=i.strip().split('<br/>')
                #print(t)
                if t[0] is not '' :
                    data.append(t)
    return(data)
#y=input()
#m=input()
#d=input()
def menuParsing(year, month, day):
    data=schulMillParsing(year, month)
    for i in data:
        if int(i[0]) is not day:
            pass
        else:
            try:
                nlunch = i.index('[중식]')
            except:
                nlunch = -1
            try:
                ndinner = i.index('[석식]')
            except:
                ndinner = -1

            slunch = ""
            sdinner = ""

            if nlunch is not -1:
                lunch = i[nlunch + 1:ndinner]
                for menu in lunch:
                    slunch += menu + " "
            else:
                slunch = ''

            if ndinner is not -1:
                dinner = i[ndinner + 1:]
                for menu in dinner:
                    sdinner += menu + " "
            else:
                sdinner = ''

            f=open("menuPaper.txt", 'w')
            f.write("%d-%d-%d" %(year, month, day) +"!"+slunch+"!"+sdinner )
            f.close()
            arr=[]
            arr.append(slunch)
            arr.append(sdinner)
            return arr

f=open("menuPaper.txt", 'w')
for i in range(1, 32):
    #l=menuParsing(2017,12,i)

    l=menuParsing(2017,12,i)
    sd = l[1]
    sl = l[0]
    date=datetime(2017, 12 ,i)
    f.write(str(date.date()) + "!" + sl + "!" + sd + "\n")

f.close()