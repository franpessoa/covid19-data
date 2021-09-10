import requests
import json

api_uris = {
    'brestado' : 'https://covid19-brazil-api.now.sh/api/report/v1',
    'brpais' : 'https://covid19-brazil-api.now.sh/api/report/v1/brazil',
    'allcountries' : 'https://covid19-brazil-api.now.sh/api/report/v1/countries'
}

def getdata():
    # Get per BR states #
    covid = json.loads(requests.get(api_uris['brestado']).text)

    estados = {
        'nome' : [],
        'casos' : [],
        'mortes' : [],
        'casos-mortes' : []
    }

    for states in covid['data']:
        
        estados['nome'].append(states['state'])
        estados['casos'].append(states['cases'])
        estados['mortes'].append(states['deaths'])
        estados['casos-mortes'].append(float(int(states['deaths'])/int(states['cases']*100)))
        
    brasil = getbrasil()
    estados['nome'].append('Total Brasil:')
    estados['casos'].append(brasil['casos'])
    estados['mortes'].append(brasil['mts'])
    estados['casos-mortes'].append(brasil['casos-mts'])

    data = []
    for i in range(0, len(estados['nome'])):
        data_tuple = (estados['nome'][i], str(estados['casos'][i]), str(estados['mortes'][i]), str(estados['casos-mortes'][i]))
        data.append(data_tuple)
    return tuple(data)

def getbrasil():
    covid = json.loads(requests.get(api_uris['brpais']).text)
    brtotal = {
        'casos' : covid['data']['confirmed'],
        'mts' : covid['data']['deaths'],
        'casos-mts' : int(covid['data']['deaths']) / int(covid['data']['confirmed']*100) 
    }
    return brtotal