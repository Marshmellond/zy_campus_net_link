import json
import requests
from configparser import ConfigParser

USERNAME = ""
PASSWORD = ""
NETWORK = ""
NETCODE = ""
# 电信@telecom 9159 联通@unicom 8379 移动@cmcc 3488
NETDATA = {"1": ["@telecom", "9159"], "2": ["@unicom", "8379"], "3": ["@cmcc", "3488"]}


def get_ini():
    global USERNAME, PASSWORD, NETWORK, NETCODE
    conf = ConfigParser()
    conf.read("config.ini", encoding="utf-8")
    USERNAME = conf["account"]["username"]
    PASSWORD = conf["account"]["password"]
    net = conf["account"]["net"]
    NETWORK = NETDATA[net][0]
    NETCODE = NETDATA[net][1]


def connect_network():
    url = "http://172.18.2.6/drcom/login"
    params = {
        "callback": "dr1003",
        "DDDDD": f"{USERNAME}{NETWORK}",
        "upass": f"{PASSWORD}",
        "0MKKey": "123456",
        "R1": "0",
        "R2": "",
        "R3": "0",
        "R6": "0",
        "para": "00",
        "v6ip": "",
        "terminal_type": "1",
        "lang": [
            "zh-cn",
            "zh"
        ],
        "jsVersion": "4.2",
        "v": f"{NETCODE}"
    }
    r = requests.get(url, params=params)
    res = dict(json.loads(r.text.split("(")[1].split(")")[0]))
    if res["result"] == 1:
        print("登录成功")
    else:
        print("登录失败")


if __name__ == '__main__':
    get_ini()
    print(USERNAME, PASSWORD, NETWORK, NETCODE)
    connect_network()
