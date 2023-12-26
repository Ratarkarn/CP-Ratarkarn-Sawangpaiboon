def addnumber(x,y) :
    print(x,"+",y,"=",x + y)
def subnumber(x,y) :
    print(x,"-",y,"=",x - y)
def multipnumber(x,y) :
    print(x,"x",y,"=",x * y)
def divisnumber(x,y):
    print(x,"/",y,"=",x / y)
a = int(input("number 1 : "))
b = int(input("number 2 : "))
while a or b != 0 :
    print("Addnumber : 1")
    print("Subnumber : 2")
    print("Multipnumber : 3")
    print("Divisnumber : 4")
    print("Exit : 0")
    c = int(input(">>>>>>"))
    if c == 1 :
        addnumber(a,b)
        print("**********")
    elif c == 2 :
        subnumber(a,b)
        print("**********")
    elif c == 3 :
        multipnumber(a,b)
        print("**********")
    elif c == 4 :
        if a and b != 0 :
            divisnumber(a,b)
            print("**********")
        else:
            print(a,"/",b,"= 0")
    else :
        print("You Exit for Application")
        break
