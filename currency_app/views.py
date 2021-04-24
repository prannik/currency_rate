from django.shortcuts import render
import requests

def index(request):
    url = 'https://www.nbrb.by/api/exrates/rates?periodicity=0'
    res = requests.get(url.format()).json()

    date = (str(res[0]['Date'])[:10:]).split('-')[::-1]
    date = '.'.join(date)

    list_currency = []
    for i in res:
        cur = {
            'scale': i['Cur_Scale'],
            'abr': i['Cur_Abbreviation'],
            'name': i['Cur_Name'],
            'rate': i['Cur_OfficialRate']
        }
        list_currency.append(cur)
    context = {'list_currency': list_currency, 'date': date}

    return render(request, 'currency/index.html', context)
