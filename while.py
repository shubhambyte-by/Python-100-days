#Table of any number 
x = int(input("Enter number for making table : "))
for i in range(1,11):
    table = x*i
    print(x ,"X ", i , " = " ,table)
    i = i + 1
