import os

crypto_graphics = "#############################################################################\n#############################################################################\n##   ___ _____   _____ _____ ___    ___  ___ _____   __   ______  __       ##\n##  / __| _ \ \ / / _ \_   _/ _ \  | _ )/ _ \_   _|  \ \ / /__ / /  \      ##\n## | (__|   /\ V /|  _/ | || (_) | | _ \ (_) || |     \ V / |_ \| () |     ##\n##  \___|_|_\ |_| |_|   |_| \___/  |___/\___/ |_|      \_/ |___(_)__/      ##\n##                                                                         ##\n#############################################################################\n#############################################################################"

def DisplayMenu():
    print(crypto_graphics)
    print("1. Start")
    print("2. Settings")
    print("3. Bot Settings")
    print("4. Exit")

def DisplaySettings():
    print(crypto_graphics)
    print("1. Buy Threshold")
    print("2. Sell Threshold")
    print("3. Bank Balance")
    print("4. Wait Time")
    print("5. Crypto Symbol")
    print("6. Return")

def DisplayBots():
    print(crypto_graphics)
    '''
    for bot in bot_list:
        print("[bot_id]\n[bot_name]\n[bot_balance]\n[bot_crypto]\n")
    '''
    
    print('#############################################################################')
    print("1. Create Bot")
    print("2. Edit Bot")
    print("3. Delete Bot")
    print("4. Return")
    
def BotSelection():
    print(crypto_graphics)
    '''
    for bot in bot_list:
        i = 0
        i++
        print("[i]. [bot_id]\n[bot_name]\n[bot_balance]\n[bot_crypto]\n[status]")
    '''
    print("1. test123 | Bitcoin Bot | $100.00 | ₿0.00000000 | Idle")
    print("Select idle bot to load")

def InfoMenu(bank_balance, action, profit, crypto_balance, trade_history):
    
    print(crypto_graphics)
    print('##                      #############################                      ##')
    print('## ${:20}'.format('{:.2f}'.format(bank_balance)) + '##{:{align}{width}}'.format(action, align='^', width='25') + '## ' + ('-$' if profit < 0 else ' $') + '{:19}'.format('{:.2f}'.format(abs(profit))) + '##')
    print('##                      #############################                      ##')
    print('#############################################################################')
    print('##{:{align}{width}}'.format(('₿{:.8f}'.format(crypto_balance)), align='^', width='73') + '##')
    print('#############################################################################')
    print('#############################################################################')
    for trade in trade_history:
        print('## ' + '{:72}'.format(trade) + '##')
    print('#############################################################################')
