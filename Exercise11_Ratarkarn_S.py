x = int(input("Add Namber Layer : "))
y = x
v = 1
for i in range(x):
    y -= 1
    print((" "*y)+("*"*v))
    v += 2
