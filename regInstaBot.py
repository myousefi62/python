#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import datetime
import requests
import time
import  string
from random import *
import json
from codecs import open

def passGen():
    char = u'ضصثقفغعهخحجچگکمنتالبیسشظطزرذدپو'
    char += string.ascii_letters + string.punctuation + string.digits
    password = "".join((choice(char) for x in range(randint(16, 16))))
    return password #requests.request("post", URL2, data=params, headers=headers).content
def userGen():
    char = string.ascii_letters + string.digits
    userName = "".join((choice(char) for x in range(randint(10, 10))))
    return userName
def emailGen(User):
    return User+'@teret.krf'

fileu = codecs.open("UserlistCreated.txt", "w", "utf-8")
fileu.writelines('\nusername\t:\tpassword\t:\temail\t:\taccount_created\t:\tdate_time')
fileu.close()
fileu = codecs.open("Erorlist.txt", "w", "utf-8")
fileu.writelines('\nusername\t:\tpassword\t:\temail\t:\taccount_created\t:\terrors\t:\terror_type\t:\tstatus\t:\tdate_time')
fileu.close()
count = 0
while(count <=1):
    if count != 0 :
        time.sleep(120)
    username = userGen()
    password = passGen()
    email    = emailGen(username)
    params = ({'email': email, 'password': password, 'username': username,'first_name': username, 'seamless_login_enabled': '1'})
    headers = {"cookie": ":mid=WoryBAAEAAF5OgzPEWhTMsF8Fjiz; ig_pr=1; ig_vh=960; ig_or=landscape-primary; mcd=1; ig_vw=901; rur=ASH; csrftoken=dPm04Fw5saxvk0b5eg2QmBwQhbN27eLI; urlgen=\"{\"time\": 1519578855}:1eq50X:_1QCQGdXWZSMecl9es8-WxVTR_A\"","referer": "https://www.instagram.com/", "x-csrftoken": "dPm04Fw5saxvk0b5eg2QmBwQhbN27eLI","Content-type": "application/x-www-form-urlencoded"}
    URL2 = "https://www.instagram.com/accounts/web_create_ajax/"
    print(params)

    result = requests.request("post", URL2, data=params, headers=headers).content
    result = json.loads(result)
    if result["account_created"]:
        fileu = codecs.open("UserlistCreated.txt", "a", "utf-8")
        fileu.writelines('\n' + str(username) + '\t:\t' + password + '\t:\t' + str(email) + '\t:\t' + str(result["account_created"])+'\t:\t'+str(datetime.datetime.now()))
        fileu.close()
    else :
        fileu = codecs.open("Erorlist.txt", "a", "utf-8")
        fileu.writelines('\n'+username+'\t:\t'+password+'\t:\t'+email+'\t:\t'+str(result["account_created"])+'\t:\t'+str(result["errors"])+'\t:\t'+str(result["error_type"])+'\t:\t'+str(result["status"])+'\t:\t'+str(datetime.datetime.now()))
        fileu.close()
    count += 1
print("The End Script")