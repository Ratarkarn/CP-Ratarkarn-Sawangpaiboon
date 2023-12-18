userInput = input("Username : ")
passwordInput = input("Password : ")
if userInput == "Name" and passwordInput == "Pass":
    print("       Welcome       ")
    print("------Kuma-Shop------")
    print("1.Banana Price 30 THB")
    print("2.Apple  price 20 THB")
    print("3.Egg    price  5 THB")
    print("4.Soap   price 20 THB")
    item = int(input(">> "))
    amount = int(input("Amount : "))
    total = 0
    if item == 1 :
        total = 30*amount
        print("Banana x",amount,":",total,"THB")
        print("Thank You")
    elif item == 2 :
        total = 20*amount
        print("Apple x",amount,":",total,"THB")
        print("Thank You")
    elif item == 3 :
        total = 5*amount
        print("Egg x",amount,":",total,"THB")
        print("Thank You")
    elif item == 4 :
        total = 20*amount
        print("Soap x",amount,":",total,"THB")
        print("Thank You")
else:
    print("You entered the wrong information")
