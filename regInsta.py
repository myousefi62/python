#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import time
import  string
from random import *
import json
from codecs import open

def passGen():
    char = u'ضصثقفغعهخحجچگکمنتالبیسشظطزرذدپو'
    char += string.ascii_letters + string.punctuation + string.digits
    password = "".join((choice(char) for x in range(randint(18, 20))))
    return password #requests.request("post", URL2, data=params, headers=headers).content
def userGen():
    char = string.ascii_letters + string.digits
    userName = "".join((choice(char) for x in range(randint(8, 10))))
    return userName
def emailGen(User):
    return User+'@teret.krf'
count = 0
while(count <=10):
    username = userGen()
    password = passGen()
    email    = emailGen(username)
    params = ({'email': email, 'password': password, 'username': username,'first_name': username, 'seamless_login_enabled': '1'})
    headers = {"cookie": ":mid=WoryBAAEAAF5OgzPEWhTMsF8Fjiz; ig_pr=1; ig_vh=960; ig_or=landscape-primary; mcd=1; ig_vw=901; rur=ASH; csrftoken=dPm04Fw5saxvk0b5eg2QmBwQhbN27eLI; urlgen=\"{\"time\": 1519578855}:1eq50X:_1QCQGdXWZSMecl9es8-WxVTR_A\"","referer": "https://www.instagram.com/", "x-csrftoken": "dPm04Fw5saxvk0b5eg2QmBwQhbN27eLI","Content-type": "application/x-www-form-urlencoded"}
    URL2 = "https://www.instagram.com/accounts/web_create_ajax/"
    print(params)

    result = requests.request("post", URL2, data=params, headers=headers).content
    print result
    count +=1

    with open('listUser.json', 'a', encoding='utf-8') as fp:
        json.dump(params, fp, ensure_ascii=False)
        json.dump(result, fp, ensure_ascii=False)
    f = open("listUser.txt", "a")
    str = "Username: " + username + " Password: " + password +  " Email: " + email
    print type(str)
    print(params)
    f.writelines(params)
    f.writelines(result)
    time.sleep(60)
print("The End Script")