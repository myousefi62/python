import requests
import time
proxie1 = {'http': 'socks5://127.0.0.1:9350', 'https': 'socks5://127.0.0.1:9350'}

proxie1 = {'http': 'socks5://127.0.0.1:9350', 'https': 'socks5://127.0.0.1:9350'}
params = ({'email': 'litre1hd4eh@teret.krf', 'password': 'qweqassda5646qwe', 'username': 'littorator1202','first_name': 'yomiurgenss', 'seamless_login_enabled': '1'})
headers = {"cookie": ":mid=WoryBAAEAAF5OgzPEWhTMsF8Fjiz; ig_pr=1; ig_vh=960; ig_or=landscape-primary; mcd=1; ig_vw=901; rur=ASH; csrftoken=dPm04Fw5saxvk0b5eg2QmBwQhbN27eLI; urlgen=\"{\"time\": 1519578855}:1eq50X:_1QCQGdXWZSMecl9es8-WxVTR_A\"","referer": "https://www.instagram.com/", "x-csrftoken": "dPm04Fw5saxvk0b5eg2QmBwQhbN27eLI","Content-type": "application/x-www-form-urlencoded"}
URL2 = "https://www.instagram.com/accounts/web_create_ajax/"
#print requests.request("post", URL2, data=params, headers=headers,proxies=proxie1).content
print requests.request("post", URL2, data=params, headers=headers).content