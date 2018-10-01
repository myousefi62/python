import requests
import time
from stem import Signal
from stem.control import Controller

proxie1 = {'http': 'socks5://127.0.0.1:9350', 'https': 'socks5://127.0.0.1:9350'}

def request(url,prox = proxie1):
    # communicate with TOR via a local proxy (privoxy)
    IP = requests.get(url, proxies=prox)
    return IP.content
# signal TOR for a new connection

def renew_connection(adrs='127.0.0.1', prt = 9351):
    with Controller.from_port(address= adrs, port = prt) as controller:
        controller.authenticate(password = '123456')
        controller.signal(Signal.NEWNYM)
        controller.close()

def GetIP(prt = 9351,prx = proxie1 ,listIp = []):
    renew_connection(prt = prt )
    newIP = request("http://icanhazip.com/",prx)
    newIP = newIP.replace('\n', '')

    while newIP  in listIp:
        renew_connection(prt=prt)
        newIP = request("http://icanhazip.com/",prx)
        newIP = newIP.replace('\n', '')
    return newIP

listIp = []
newIP = request("http://icanhazip.com/")
newIP = newIP.replace('\n', '')
listIp.append(newIP)

#listIp.append(oldIP)
for i in range(0, 4):
    #print(listIp)
    GetIP(listIp=listIp)
    newIP = request("http://icanhazip.com/")
    newIP = newIP.replace('\n', '')
    listIp.append(newIP)
    print(listIp)
    print     requests.request("get","http://icanhazip.com/",proxies=proxie1).content
    params =({'@email': 'mir1jre1hd4eh@teret.krf', '@password': 'qweqassda5646qwe', '@username': 'your41iegen5438','@first_name': 'yourgenss', '@seamless_login_enabled': '1'})
    headers = {
        "cookie": ":mid=WoryBAAEAAF5OgzPEWhTMsF8Fjiz; ig_pr=1; ig_vh=960; ig_or=landscape-primary; mcd=1; ig_vw=901; rur=ASH; csrftoken=dPm04Fw5saxvk0b5eg2QmBwQhbN27eLI; urlgen=\"{\"time\": 1519578855}:1eq50X:_1QCQGdXWZSMecl9es8-WxVTR_A\"",
        "referer": "https://www.instagram.com/", "x-csrftoken": "dPm04Fw5saxvk0b5eg2QmBwQhbN27eLI",
        "Content-type": "application/x-www-form-urlencoded"}
    URL2 = "https://www.instagram.com/accounts/web_create_ajax/"
    print requests.request("post",URL2,data=params,headers=headers,proxies=proxie1).content
    time.sleep(60)
