menuList = []
def showBill():
    totalPrice = 0
    print("---- My Food ----")
    for i in range(len(menuList)):
        print(menuList[i][0],menuList[i][1])
        totalPrice += int(menuList[i][1])
    print("Tolat Price : %d THB" %totalPrice)

while True :
    menuName = input("Please Enter Menu : ")
    if menuName.lower() == "exit" :
        break
    else:
        menuPrice = input("Price : ")
        menuList.append([menuName,menuPrice])

print(menuList)
showBill()
