a = float(input("Enter first number : "))
b = float(input("Enter second number : "))
c = float(input("Enter third number : "))
print ("Enter operation you want to perform :")
operation = input()
def sum(a,b,c):
    sum = a+b+c
    print("Sum of three numbers is : ",sum)
def multiplication(a,b,c):
    multiplication = a*b*c
    print("Multiplication of three numbers is : ",multiplication)
def division(a,b,c):
    division = a/b/c
    print("Division of three numbers is : ",division)
def subtraction(a,b,c):
    subtraction = a-b-c
    print("Subtraction of three numbers is : ",subtraction)


    
if operation == "sum":
    print(sum(a,b,c))   
elif operation == "multiplication":
    print(multiplication(a,b,c))
elif operation == "division":
    print(division(a,b,c))
elif operation == "subtraction":
    print(subtraction(a,b,c))




# x = "Python"  
# print('y' in x)