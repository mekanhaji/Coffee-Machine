from promp import help, clear, getch
from utils import change, charge, store, report
# Items
def espresso():
    requires = {
        "water": 50,
        "coffee": 18,
    }
    price = 250
    money = charge("espresso", price)
    if requires['coffee'] <= store['coffee'] and \
       requires['water'] <= store['water'] :
        if money >= price:
            store['coffee'] -= requires['coffee']
            change(price, money)
            getch("Enjoy Your espresso, ")
        else:
            change(price, money)
            getch()
    else:
        print("Nop, Can't make it!\n")
        getch()

def latte():
    requires = {
        'water': 200, 
        'milk': 150, 
        'coffee': 24
    }
    price = 150
    
    if requires['water'] <= store['water'] and \
       requires['milk'] <= store['milk'] and \
       requires['coffee'] <= store['coffee']:
        money = charge("Latte", price)
        if money >= price:
            store['water'] -= requires['water']
            store['milk'] -= requires['milk']
            store['coffee'] -= requires['coffee']
            change(price, money)
            getch("Enjoy Your latte, ")
        else:
            change(price, money)
            getch()
    else:
        print("Nop, Can't make it!\n")
        getch()


def cappuccino():
    requires = {
        'water': 250, 
        'milk': 100, 
        'coffee': 24
    }
    price = 120
    money = charge("cappuccino", price)
    if requires['water'] <= store['water'] and \
       requires['milk'] <= store['milk'] and \
       requires['coffee'] <= store['coffee']:
        if price >= money:
            store['water'] -= requires['water']
            store['milk'] -= requires['milk']
            store['coffee'] -= requires['coffee']
            change(price, money)
            getch("Enjoy Your cappuccino, ")
        else:
            change(price, money)
            getch()
    else:
        print("Nop, Can't make it!\n")
        getch()

    
# App
while True:
    clear()    
    promp = input("What u like To have,\n1. espresso\n2. latte\n3. cappuccino\n-->")
    if promp == 'off' or promp == "quit" or promp == "0": break
    elif promp == "1" or promp.lower() == "espresso":
        espresso()
    elif promp == "2" or promp.lower() == "latte":
        latte()
    elif promp == "3" or promp.lower() == "cappuccino":
        cappuccino()
    elif promp == "4" or promp.lower() == "report":
        report()
    elif promp == "4" or promp == "help":
        help()
    else:
        print("Can't understand U!('_')")
        help()
        getch()
print("ThankYou For Visiting US!")
print("Made with 🦾HardWork by Kanhaji😎")
