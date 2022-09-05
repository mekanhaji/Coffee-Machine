from promp import getIn,getch

def report():
    print("\t---REPORT---")
    print(f"Water : {store['water']} ml")
    print(f"Milk : {store['milk']} g")
    print(f"Coffee : {store['coffee']} g")
    getch()

store = {
    'water' : 1000,
    'milk' : 1000,
    'coffee' : 1000
}

def change(price, money):
    change = price - money
    if change < 0:
        print("Your change", abs(change), "₹")
    elif change == 0:
        pass
    else:
        print("Not Enough Money", money, "₹")

def charge(item, price) :
    five = ten = twenty = fifty = hundred = 0
    print(f"Price for {item} is {price} ₹")
    five = getIn("No of Five coins : ")
    ten = getIn("No of Ten coins : ")
    twenty = getIn("No of Twenty coins : ")
    fifty = getIn("No of Fifty coins : ")
    hundred = getIn("No of Hundred coins : ")

    amount = (5 * five) + (10 * ten) + (20 * twenty) + (50 * fifty) + (100 * hundred)

    return amount
