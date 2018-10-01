'''
Python script to connect to Tor via Stem and Privoxy, requesting a new connection (hence a new IP as well) as desired.
'''
import requests
import stem
import stem.connection

import time
import urllib2

from stem import Signal
from stem.control import Controller


proxie1 = {'http': 'socks5://127.0.0.1:9350', 'https': 'socks5://127.0.0.1:9350'}

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
    '''def _set_urlproxy():
        proxy_support = urllib2.ProxyHandler({"http" : "127.0.0.1:8118"})
        opener = urllib2.build_opener(proxy_support)
        urllib2.install_opener(opener)

    # request a URL
    # via the proxy
    _set_urlproxy()
    request=urllib2.Request(url, None, headers)
    return urllib2.urlopen(request).read()'''
    IP = requests.get(url, proxies=prox)
    return IP.content

# signal TOR for a new connection
def renew_connection(adrs='127.0.0.1', prt = 9351):
    with Controller.from_port(address= adrs, port = prt) as controller:
        controller.authenticate(password = '123456')
        controller.signal(Signal.NEWNYM)
        controller.close()
def GetIP(prt = 9351,prx = proxie1 ,listIp = []):
    # first pass
    #oldIP = request("http://icanhazip.com/", prx)
    # renew the TOR connection
    renew_connection(prt = prt )
    # obtain the "new" IP address
    newIP = request("http://icanhazip.com/",prx)

    # zero the
    # elapsed seconds
    seconds = 2

    # loop until the "new" IP address
    # is different than the "old" IP address,
    # as it may take the TOR network some
    # time to effect a different IP address
    #while oldIP == newIP:
    #print(listIp)
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
        # signal that the program is still awaiting a different IP address
        #print ("%d seconds elapsed awaiting a different IP address." % seconds)
        #print(newIP)
    # output the
    # new IP address
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
    """newIP = request("http://icanhazip.com/")
    newIP = newIP.replace('\n', '')
    listIp.append(newIP)"""
    """renew_connection(prt = 9351)
    #print (request("http://icanhazip.com/",proxie1))

    # if it's the first pass
    if newIP == "0.0.0.0":
        # renew the TOR connection
        renew_connection()
        # obtain the "new" IP address
        newIP = request("http://icanhazip.com/")
        newIP = newIP.replace('\n', '')
    # otherwise
    else:
        # remember the
        # "new" IP address
        # as the "old" IP address
        oldIP = newIP
        # refresh the TOR connection
        renew_connection()
        # obtain the "new" IP address
        newIP = request("http://icanhazip.com/")
        newIP = newIP.replace('\n', '')

    # zero the
    # elapsed seconds
    seconds = 0

    # loop until the "new" IP address
    # is different than the "old" IP address,
    # as it may take the TOR network some
    # time to effect a different IP address
    if newIP not in listIp:
        print(newIP)
    #while oldIP == newIP:
    while newIP not in listIp:
        # sleep this thread
        # for the specified duration
        time.sleep(seconds)
        # track the elapsed seconds
        seconds += secondsBetweenChecks
        # obtain the current IP address
        newIP = request("http://icanhazip.com/")
        newIP = newIP.replace('\n','')
        # signal that the program is still awaiting a different IP address
        #print ("%d seconds elapsed awaiting a different IP address." % seconds)
    # output the
    # new IP address
    #print ("")"""
    newIP = request("http://icanhazip.com/")
    newIP = newIP.replace('\n', '')
    listIp.append(newIP)
    print(listIp)
    #print ("newIP: %s" % newIP)