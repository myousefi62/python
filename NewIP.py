'''
Python script to connect to Tor via Stem and Privoxy, requesting a new connection (hence a new IP as well) as desired.
'''
import requests
import time
from stem import Signal
from stem.control import Controller


proxie1 = {'http': 'socks5://127.0.0.1:9350', 'https': 'socks5://127.0.0.1:9350'}
print(type(proxie1))
# initialize some HTTP headers
# for later usage in URL requests
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent}

# initialize some
# holding variables
oldIP = "0.0.0.0"
newIP = "0.0.0.0"

# how many IP addresses
# through which to iterate?
nbrOfIpAddresses = 6

# seconds between
# IP address checks
secondsBetweenChecks = 2

# request a URL
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

    # zero the
    # elapsed seconds
    seconds = 0

    while newIP in listIp:
        # sleep this thread
        # for the specified duration
        time.sleep(seconds)
        # track the elapsed seconds
        seconds += secondsBetweenChecks
        # obtain the current IP address
        renew_connection(prt=prt)
        newIP = request("http://icanhazip.com/",prx)
        newIP = newIP.replace('\n', '')

    if newIP in listIp:
        print "in" , newIP , listIp
    else:
         print "not" , newIP , listIp
    return newIP
# cycle through
# the specified number
# of IP addresses via TOR
listIp = []
newIP = request("http://icanhazip.com/")
newIP = newIP.replace('\n', '')
listIp.append(newIP)
print type(newIP) , newIP
print type(listIp[0]) , listIp[0]
#listIp.append(oldIP)
for i in range(0, nbrOfIpAddresses):
    print(listIp)
    GetIP(listIp=listIp)
    newIP = request("http://icanhazip.com/")
    newIP = newIP.replace('\n', '')
    listIp.append(newIP)
    print(listIp)