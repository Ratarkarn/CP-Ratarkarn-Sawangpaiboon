def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result

price = int(input("Price you Included vat : "))
vat = vatCalculate(price)
print("Price Included vat :",vat)
