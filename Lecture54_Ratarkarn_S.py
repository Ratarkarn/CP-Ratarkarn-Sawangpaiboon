def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        print("Done !")
        showMenu()
    else:
        print("User or Password unsuccess")
def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    menuSelect()
def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1 :
        print("Vat :",vatCalculator(int(input("Input Number : "))))
    elif userSelected == 2 :
        print("Price Included vat :",priceCalculator())
def vatCalculator(totalprice):
    vat = 7
    result = totalprice + (totalprice * vat / 100)
    return result
def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)
login()
