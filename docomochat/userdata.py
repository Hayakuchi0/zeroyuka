import json
import os
import copy
from os import makedirs
from os.path import expanduser, dirname, abspath, isdir
from datetime import datetime
from .register import register


def readuser(path):
    text = ''
    with open(path, encoding='utf-8', mode='r') as f:
        text = f.read()
    ret = json.loads(text)
    return ret


def createoption(
        nickname,
        nicknameY,
        sex,
        bloodtype,
        birthdateY,
        birthdateM,
        birthdateD,
        age,
        constellations,
        place,
        mode):
    option = {}
    option["nickname"] = nickname
    option["nicknameY"] = nicknameY
    option["sex"] = sex
    option["bloodtype"] = bloodtype
    option["birthdateY"] = birthdateY
    option["birthdateM"] = birthdateM
    option["birthdateD"] = birthdateD
    option["age"] = age
    option["constellations"] = constellations
    option["place"] = place
    option["mode"] = mode
    return option


def createuser(path, option):
    userjson = {}
    userjson['appId'] = register()
    userjson['option'] = option
    return recvuser(path, userjson)


def recvuser(path, userjson):
    outjson = copy.deepcopy(userjson)
    outjson['appRecvTime'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    writeuser(path, outjson)
    return outjson


def writeuser(path, userjson):
    configdirpath = dirname(abspath(path))
    if not isdir(configdirpath):
        makedirs(configdirpath)
    with open(path, encoding='utf-8', mode='w+') as f:
        f.write(json.dumps(userjson))


def getconfigpath():
    return expanduser("~") + os.sep + '.zeroyuka'


def getconfigpathuser():
    return getconfigpath() + os.sep + 'userconfig.json'


def gettoolpath():
    return getconfigpath() + os.sep + 'tools'
