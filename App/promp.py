from os import system, name
# for clearing Screen
def clear():
   # for windows
   if name == 'nt':
      _ = system('cls')

   # for mac and linux
   else:
       _ = system('clear')

# wait for input
def getch(promp = ''):
    input(f"{promp}Press Enter to contiue ")

def help():
    print("\t---Wellcome To Coffee Machine---")
    print("> 'help' or 4: To see all commands")
    print("> 'espresso' or 1 : To buy espresso")
    print("> 'latte' or 2: To buy latte")
    print("> 'cappuccino' or 3 : To buy cappuccino")
    print("> 'off' or 0: To Turn off Machine")
    print("> 'report' or 5: To check the storege")
    getch()

def getIn(msg):
    promp = 0
    try:
        promp = int(input(msg))
    except:
        print("invalid input!")
        getIn(msg)
    return promp
