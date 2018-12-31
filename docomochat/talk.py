from requests import post
from json import dumps
from datetime import datetime
from .apikey import APIKEY
from .userdata import recvuser, getconfigpathuser


def talk(text, user):
    appId = user['appId']
    option = user['option']
    appRecvTime = user['appRecvTime']
    endpoint = 'https://api.apigw.smt.docomo.ne.jp/naturalChatting/v1/dialogue?APIKEY=' + APIKEY
    header = {'Content-Type': 'application/json;charset=UTF-8'}
    reqbody = {
        'language': 'ja-JP',
        'botId': 'Chatting',
        'appId': appId,
        'voiceText': text,
        'clientData': {
            'option': option
         },
        'appRecvTime': appRecvTime,
        'appSendTime': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    response = post(
        endpoint,
        data=dumps(reqbody),
        headers=header
    )
    resjson = response.json()
    recvuser(getconfigpathuser(), user)
    return resjson['systemText']['expression']
