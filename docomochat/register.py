import requests
import json
from .apikey import APIKEY


def register():
    endpoint = 'https://api.apigw.smt.docomo.ne.jp/naturalChatting/v1/registration?APIKEY=' + APIKEY
    header = {'Content-Type': 'application/json;charset=UTF-8'}
    reqbody = {
        'botId': 'Chatting',
        'appKind': 'ZeroyukaAlpha0.1'
    }
    response = requests.post(
        endpoint,
        data=json.dumps(reqbody),
        headers=header
    )
    if response.status_code is 200:
        return response.json()['appId']
    else:
        print("error occurd(status code:"+str(response.status_code)+")")
        print(json.dumps(response.json()))
        response.raise_for_status()
