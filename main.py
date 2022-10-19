import json
import requests
import os
import configparser
import time
from tradeogre import TradeOgre #https://github.com/Endogen/TradeOgrePy
from datetime import datetime
from cryptoScipts import *

config = configparser.ConfigParser()
config.read("config.ini")
moneyAmount = config.get("temp", "moneyAmount")
scriptPath = str(config.get("temp", "scriptPath"))
timeAmount = config.get("temp", "timeAmount")
apikey = str(config.get("temp", "apikey"))
apisecret = str(config.get("temp", "apisecret"))
buycoin = str(config.get("temp", "buycoin"))
sellcoin = str(config.get("temp", "sellcoin"))
trade_ogre = TradeOgre(key=apikey, secret=apisecret)
if (apikey and apisecret) != '':
    isSim = False
else:
    isSim = True

while True:
    try:
        os.system("clear")
        print("CryptoBot\n")
        print("1) Simulation\n2) Settings \n3) Exit")
        option = int((input()))
    except ValueError:
        continue
    else:
        if option == 1:
            while True:
                try:
                    os.system("clear")
                    print("Begin with these settings?\n")
                    print("Starting Amount: $" + moneyAmount + "\n")
                    print("Script: " + scriptPath + "\n")
                    print("Decision Time: " + timeAmount + "m\n")
                    print("Crypto Coins: (" + sellcoin + "/" + buycoin + ")\n")
                    print("Simulation Mode: " + str(isSim) + "\n\n")

                    print("1)Go\n")
                    print("2)Back\n")
                    option = int(input())
                except ValueError:
                    continue
                else:
                    if option == 1:
                        os.system("clear")
                        scriptDecision = 0
                        while scriptDecision == 0:
                            scriptDecision = startScripts(scriptPath, moneyAmount, timeAmount)
                            if scriptDecision == 1:
                                print("Bought")
                                scriptDecision = 0
                                #trade_ogre.buy(buycoin + "-" + sellcoin, 'quantity', 'price')
                            if scriptDecision == 2:
                                print("Sold")
                                scriptDecision = 0
                                #trade_ogre.sell(buycoin + "-" + sellcoin, 'quantity', 'price')
                            if scriptDecision == 3:
                                print("No Sale")
                                scriptDecision = 0
                            time.sleep(60 * int(timeAmount))
                    if option == 2:
                        option = 0
                        break
        if option == 2:
            while True:
                try:
                    os.system("clear")
                    config = configparser.ConfigParser()
                    config.read("config.ini")
                    moneyAmount = config.get("temp", "moneyAmount")
                    scriptPath = config.get("temp", "scriptPath")
                    timeAmount= config.get("temp", "timeAmount")
                    print("1) Set Money(" + str(moneyAmount) + ")\n")
                    print("2) Set Script(" + str(scriptPath) + ")\n")
                    print("3) Set Time(" + str(timeAmount) + "m)\n")
                    print("4) Set API Keys(Sim = " + str(isSim) + ")\n")
                    print("5) Back\n\n")
                    option = int((input()))
                except ValueError:
                    continue
                else:
                    if option == 1:
                        while True:
                            try:
                                print("Enter new amount")
                                newSetting = int(input())
                            except ValueError:
                                continue
                            else:
                                config.set("temp", "moneyAmount", str(newSetting))
                                with open("config.ini", "w") as configfile:
                                    config.write(configfile)
                                break
                    elif option == 2:
                        print("Enter new path")
                        newSetting = input()
                        config.set("temp", "scriptPath", str(newSetting))
                        with open("config.ini", "w") as configfile:
                            config.write(configfile)
                        continue
                    elif option == 3:
                        while True:
                            try:
                                print("Enter new time")
                                newSetting = int(input())
                            except ValueError:
                                continue
                            else:
                                config.set("temp", "timeAmount", str(newSetting))
                                with open("config.ini", "w") as configfile:
                                    config.write(configfile)
                                break
                    elif option == 4:
                        print("Enter your API key")
                        apikey = input()
                        print("Enter your Secret key")
                        apisecret = input()
                        config.set("temp", "apikey", str(apikey))
                        config.set("temp", "apisecret", str(apisecret))
                        with open("config.ini", "w") as configfile:
                            config.write(configfile)
                        continue
                    elif option == 5:
                        option = 0
                        break
        if option == 3:
            break
os.system("clear")
exit()
