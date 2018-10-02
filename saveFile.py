import codecs
import datetime

print "Or like this: " ,datetime.datetime.now()
fileu = codecs.open("list", "w", "utf-8")
fileu.writelines('\nusername\t:\tpassword\t:\temail\t:\taccount_created')
fileu.close()
params = {'username': 'SSeXXjvE3', 'first_name': 'SSeXXjvE3', 'password': u'I\u0628\u0647-o\\\u062d\u06af]G8p\u062eT\u0628Y\u0628}k\u0647', 'email': 'SSeXXjvE3@teret.krf', 'seamless_login_enabled': '1'}
result={"account_created": "false", "errors": {"ip": ["The IP address you are using has been flagged as an open proxy. If you believe this to be incorrect, please visit http://help.instagram.com/"]}, "status": "ok", "error_type": "signup_block"}
print result["account_created"]
print type(result)


username= 'SSeXXjvE3'
password = u'I\u0628\u0647-o\\\u062d\u06af]G8p\u062eT\u0628Y\u0628}k\u0647'
email = 'SSeXXjvE3@teret.krf'
#fileu.writelines(str(params))
fileu = codecs.open("list", "a", "utf-8")
fileu.writelines('\n'+username + '\t:\t' + password + '\t:\t' + email + '\t:\t' + result["account_created"])
fileu.close()