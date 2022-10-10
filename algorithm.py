import json
import os
import time
import random
import math
from pycoingecko import CoinGeckoAPI
from datetime import datetime

def startAlgo(algorithmPath, moneyAmount, timeAmount):
    if algorithmPath == str("RandomAlgo"):
        cg = CoinGeckoAPI()
        ping = json.dumps(cg.ping())
        status = json.loads(ping)

        if(status["gecko_says"] == "(V3) To the Moon!"):
            now = datetime.now()
            randnum = random.randint(1, 10)
            log = open("logs/" + str(now.strftime("%m-%d-%y %H:%M:%S")) + ".txt", "x")
            log.write("[" + str(now.strftime("%H:%M")) + "] Connected to CoinGecko API\n")
            cryptoCoin = json.dumps(cg.get_price(ids='bitcoin', vs_currencies='usd'))
            cryptoUSD = json.loads(cryptoCoin)
            cryptoPrice = cryptoUSD["bitcoin"]["usd"]
            cryptoAmount = int(moneyAmount) / cryptoPrice
            print("*********************************************************")
            print("[" + now.strftime("%H:%M") + "]" + "BUY: $" + str(cryptoPrice))
            print("-$" + moneyAmount)
            print("+" + str(cryptoAmount) + " BTC")
            print("*********************************************************")
            moneyAmount = 0
            steps = 1
            botCommand = 0
            randomChoice = [randnum]
            prices = [cryptoPrice]
            i=0
            while i < int(timeAmount):
                randomChoice.append("0")
                prices.append("0")
                i+=1
            time.sleep(70-int(now.strftime("%S")))
            while True:
                now = datetime.now()
                randnum = random.randint(1, 10)
                cryptoCoin = json.dumps(cg.get_price(ids='bitcoin', vs_currencies='usd'))
                cryptoUSD = json.loads(cryptoCoin)
                cryptoPrice = cryptoUSD["bitcoin"]["usd"]
                if steps <= (int(timeAmount) - 2):
                    randomChoice[steps] = randnum
                    prices[steps] = cryptoPrice
                    print("[" + now.strftime("%H:%M") + "]: $" + str(cryptoPrice))
                    steps+=1
                else:
                    priceCheck = 0
                    i = 0
                    for x in prices:
                        priceCheck += float(prices[i])
                        i+=1
                    priceCheck = priceCheck/(int(timeAmount)-1)
                    decision = 0
                    i = 0
                    for x in randomChoice:
                        decision += int(randomChoice[i])
                        i+= 1
                    decision = decision/int(timeAmount)
                    decision = math.ceil(decision)
                    if priceCheck != prices[0]:
                        if decision == 2:
                            botCommand = 2
                        elif decision % 2 == 0:
                            if moneyAmount > 0:
                                botCommand = 1
                            else:
                                botCommand = 2
                        elif decision % 1 == 0:
                            if cryptoAmount > 0:
                                botCommand = 3
                            else:
                                botCommand = 2
                    else:
                        botCommand = 2
                if botCommand == 1:
                    cryptoAmount = moneyAmount/cryptoPrice
                    print("*********************************************************")
                    print("[" + now.strftime("%H:%M") + "]" + "BUY: $" + str(cryptoPrice))
                    print("-$" + str(moneyAmount))
                    print("+" + str(cryptoAmount) + " BTC")
                    print("*********************************************************")
                    log.write("[" + str(now.strftime("%H:%M")) + "] Bought " + str(cryptoAmount) + " BTC\n")
                    moneyAmount = 0
                    randomChoice[0] = decision
                    prices[0] = cryptoPrice
                    steps = 1
                elif botCommand == 2:
                    print("*********************************************************")
                    print("[" + now.strftime("%H:%M") + "]" + "NO SALE: $" + str(cryptoPrice))
                    print("$" + str(moneyAmount))
                    print(str(cryptoAmount) + " BTC")
                    print("*********************************************************")
                    log.write("[" + str(now.strftime("%H:%M")) + "] No Sale\n")
                    randomChoice[0] = decision
                    prices[0] = cryptoPrice
                    steps = 1
                elif botCommand == 3:
                    moneyAmount = cryptoAmount*cryptoPrice
                    print("*********************************************************")
                    print("[" + now.strftime("%H:%M") + "]" + "SOLD: $" + str(cryptoPrice))
                    print("+$" + str(moneyAmount))
                    print("-" + str(cryptoAmount) + " BTC")
                    print("*********************************************************")
                    log.write("[" + str(now.strftime("%H:%M")) + "] Sold: $" + str(moneyAmount) + "\n")
                    cryptoAmount = 0
                    randomChoice[0] = decision
                    prices[0] = cryptoPrice
                    steps = 1
                botCommand = 0
                time.sleep(60-int(now.strftime("%S")))
