import json
import os
import configparser
from pycoingecko import CoinGeckoAPI
from datetime import datetime
from algorithm import *

cg = CoinGeckoAPI()
ping = json.dumps(cg.ping())
status = json.loads(ping)
option = 0
while option <= 2:
    os.system("clear")
    print("CryptoBot 0.8\n")
    print("1) Simulation\n2) Settings \n3) Exit")
    option = int((input()))
    if option == 1:
        while option < 2:
            os.system("clear")
            config = configparser.ConfigParser()
            config.read("config.ini")
            moneyAmount = config.get("temp", "moneyAmount")
            algorithmPath = str(config.get("temp", "algorithmPath"))
            timeAmount= config.get("temp", "timeAmount")
            print("Begin with these settings?\n")
            print("Starting Amount: $" + moneyAmount + "\n")
            print("Algorithm: " + algorithmPath + "\n")
            print("Decision time: " + timeAmount + "m\n\n")

            print("1)Go\n")
            print("2)Back\n")
            option = int(input())
            if option == 1:
                os.system("clear")
                startAlgo(algorithmPath, moneyAmount, timeAmount)

    elif option == 2:
        while option <= 3:
            os.system("clear")
            config = configparser.ConfigParser()
            config.read("config.ini")
            moneyAmount = config.get("temp", "moneyAmount")
            algorithmPath = config.get("temp", "algorithmPath")
            timeAmount= config.get("temp", "timeAmount")
            print("1) Set Money(" + str(moneyAmount) + ")\n")
            print("2) Set Alogrithm(" + str(algorithmPath) + ")\n")
            print("3) Set Time(" + str(timeAmount) + "m)\n")
            print("4) Go Back")
            option = int((input()))
            if option == 1:
                print("Enter new amount")
                newSetting = input()
                config.set("temp", "moneyAmount", str(newSetting))
                with open("config.ini", "w") as configfile:
                    config.write(configfile)
            elif option == 2:
                print("Enter new path")
                newSetting = input()
                config.set("temp", "algorithmPath", str(newSetting))
                with open("config.ini", "w") as configfile:
                    config.write(configfile)
            elif option == 3:
                print("Enter new time")
                newSetting = input()
                config.set("temp", "timeAmount", str(newSetting))
                with open("config.ini", "w") as configfile:
                    config.write(configfile)
        option = 0
    elif option == 3:
        os.system("clear")
        exit()
option = 0

