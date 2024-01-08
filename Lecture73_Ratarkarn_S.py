systemMenu = {"ข้าวหมกไก่":50,"ข้าวมันไก่":40,"ข้าวไก่ทอด":45,"ข้าวไก่ผสม":50,"ข้าวมันไก่พิเศษ":50}
menuList = []
def showMenu():
    print("---- Menu ----")
    for i in systemMenu:
        print(i,systemMenu[i])

def showBill():
    print("---- My Food ----")
    totalBill = 0
    for num in range(len(menuList)):
        print(menuList[num][0], menuList[num][1])
        totalBill += int(menuList[num][1])
    print("Tolat Price : %d THB" %totalBill)

showMenu()
while True:
    menuName = input("Plese Enter Menu : ")
    if menuName.lower()== "exit":
        break
    else :
        menuList.append([menuName,systemMenu[menuName]])
showBill()
