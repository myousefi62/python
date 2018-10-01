#!/usr/bin/python
# importing the requests library
#import requests
import http.client, urllib.parse
# api-endpoint
#URL = "http://api.open-notify.org/iss-now.json"
#r = requests.get(url = URL)
params = urllib.parse.urlencode({'@email':'mirjrehdeh@teret.krf' ,'@password':'qweqassda5646qwe','@username':'yourgen5438','@first_name':'yourgenss','@seamless_login_enabled':'1'})
headers = {"cookie":":mid=WoryBAAEAAF5OgzPEWhTMsF8Fjiz; ig_pr=1; ig_vh=960; ig_or=landscape-primary; mcd=1; ig_vw=901; rur=ASH; csrftoken=dPm04Fw5saxvk0b5eg2QmBwQhbN27eLI; urlgen=\"{\"time\": 1519578855}:1eq50X:_1QCQGdXWZSMecl9es8-WxVTR_A\"","referer":"https://www.instagram.com/","x-csrftoken":"dPm04Fw5saxvk0b5eg2QmBwQhbN27eLI","Content-type": "application/x-www-form-urlencoded"}
URL2 = "https://www.instagram.com/accounts/web_create_ajax/"
conn = http.client.HTTPSConnection("instagram.com/accounts/web_create_ajax")
conn.request("POST", "/", params, headers)
response = conn.getresponse()
print(response.status, response.reason)
#r = requests.post(url = URL2 ,params,headers )
data = response.json()
print (data)



