import json
import time
import random
import math
from pycoingecko import CoinGeckoAPI
from datetime import datetime

cg = CoinGeckoAPI()
ping = json.dumps(cg.ping())
status = json.loads(ping)


if(status["gecko_says"] == "(V3) To the Moon!"):
    print("API Loaded")
    now = datetime.now()
    log = open("logs/" + str(now.strftime("%m-%d-%y %H:%M:%S")) + ".txt", "x")
    log.write("[" + str(now.strftime("%H:%M")) + "] Connected to CoinGecko API\n")
    coin = json.dumps(cg.get_price(ids='bitcoin', vs_currencies='usd'))
    usd = json.loads(coin)
    amount = str(usd["bitcoin"]["usd"])
    price = usd["bitcoin"]["usd"]
    money = 0
    btc = 10000 / price
    calculate_amount = 1
    randnum = random.randint(1, 100)
    choice = [randnum , "0", "0", "0", "0"]
    print("[")
    print("[" + now.strftime("%H:%M") + "]" + "BUY: $" + amount + " (" + str(randnum) + ")")
    print("-$10000")
    print("+" + str(btc) + " BTC")
    print("]")
    now = datetime.now()
    log.write("[" + str(now.strftime("%H:%M")) + "] Bought " + str(btc) + " BTC\n")
    time.sleep(70-int(now.strftime("%S")))
    while True:
        now = datetime.now()
        randnum = random.randint(1, 100)
        coin = json.dumps(cg.get_price(ids='bitcoin', vs_currencies='usd'))
        usd = json.loads(coin)
        amount = str(usd["bitcoin"]["usd"])
        price = usd["bitcoin"]["usd"]
        if calculate_amount <= 3:
            choice[calculate_amount] = randnum
            print("[" + now.strftime("%H:%M") + "]: $" + amount + " (" + str(randnum) + ")")
            calculate_amount+=1
        else:
            result = (int(choice[0]) + int(choice[1]) + int(choice[2]) + int(choice[3]) + int(choice[4])) / 5
            result = math.ceil(result)
            if result <= 59:
                if(btc > 0):
                    money = btc * price
                    print("[")
                    print("[" + now.strftime("%H:%M") + "]" + "SELL: $" + amount + " (" + str(result) + ")")
                    log.write("[" + str(now.strftime("%H:%M")) + "] Sold $" + str(money) + "\n")
                    print("-" + str(btc) + " BTC")
                    print("+$" + str(money))
                    print("PROFITS: $" + str((money - 10000)))
                    print("]")
                    btc = 0
                    choice[0] = result
                    calculate_amount = 1
                else:
                    btc = money/price
                    print("[")
                    print("[" + now.strftime("%H:%M") + "]" + "BUY: $" + amount + " (" + str(result) + ")")
                    log.write("[" + str(now.strftime("%H:%M")) + "] Bought " + str(btc) + " BTC\n")
                    print("+" + str(btc) + " BTC")
                    print("-$" + str(money))
                    print("]")
                    money = 0
                    choice[0] = result
                    calculate_amount = 1
            elif result == 60:
                    choice[0] = result
                    calculate_amount = 1
                    print("[")
                    print("[" + now.strftime("%H:%M") + "]" + "NO SALE: $" + amount + " (" + str(result) + ")")
                    log.write("[" + str(now.strftime("%H:%M")) + "] No Sale\n")
                    print("$" + str(money))
                    print(str(btc) + " BTC")
                    print("]")
            else:
                    if(money > 0):
                        btc = money/price
                        print("[")
                        print("[" + now.strftime("%H:%M") + "]" + "BUY: $" + amount + " (" + str(result) + ")")
                        log.write("[" + str(now.strftime("%H:%M")) + "] Bought " + str(btc) + " BTC\n")
                        print("+" + str(btc) + " BTC")
                        print("-$" + str(money))
                        print("]")
                        money = 0
                        choice[0] = result
                        calculate_amount = 1
                    else:
                        money = btc * price
                        print("[")
                        print("[" + now.strftime("%H:%M") + "]" + "SELL: $" + amount + " (" + str(result) + ")")
                        log.write("[" + str(now.strftime("%H:%M")) + "] Sold $" + str(money) + "\n")
                        print("-" + str(btc) + " BTC")
                        print("+$" + str(money))
                        print("PROFITS: $" + str((money - 10000)))
                        print("]")
                        btc = 0
                        choice[0] = result
                        calculate_amount = 1
        time.sleep(60-int(now.strftime("%S")))
else:
    print("ERROR: API not loading")
    log.write("[" + str(now.strftime("%H:%M")) + "] Could not connect to CoinGecko API")
log.close()
