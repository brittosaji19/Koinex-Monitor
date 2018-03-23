#!/usr/bin/python3
import os
import time
import sys
import requests

Max = {'BTC': 1450000, 'ETH': 106000, 'XRP': 100, 'LTC': 21000, 'BCH': 260000}
Min = {'BTC': 600000, 'ETH': 70000, 'XRP': 85, 'LTC': 12000, 'BCH': 100000}

#METHODS
# def notify(Title, Body, Speak):
#     os.system("notify-send 'display notification \"%s\" with title \"%s\"'" % (Body, Title))
    # if Speak:
    #     os.system("say %s && say %s" % (Title, Body))


def Target():
    # for key in Max.keys():
    #     if float(price[key]) >= Max[key]:
    #         notify("Dear Lord! %s on Bull Run" % (key), "Currently @ %s Indian Rupees" % (price[key]), True)
    #         time.sleep(6)
            
    # for key in Min.keys():
    #     if float(price[key]) <= Min[key]:
    #         notify("Sheesh! %s going down" % (key), "Currently @ %s Indian Rupees" % (price[key]), True)
    #         time.sleep(6)
    while(True):
        ticker=""
        price = requests.request("GET", "https://koinex.in/api/ticker").json()["prices"]
        for key in Max.keys():
            ticker+="\n%s : %s \n"%(key,price[key])
        # print(ticker)
        os.system('notify-send -i ~/KoinexTicker/logo.jpeg -t 5000 "Koinex:" "%s"' %(ticker))
        time.sleep(600)
            
    
#MAIN
Target()