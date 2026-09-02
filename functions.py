# We are using and making funcation because sometimes  i need same things with very big , so insted of type same things multiple times ,
# we make function of that thing , when we need we just call it function and perform a code 
# so it make code very less line and less time .

# for example we want to just calculate mean of fuction of just AM , i am taking example of Arithmetic mean of some numbers

# let

a = float(input("Enter first number : "))
b = float(input("Enter second number : "))
c = float(input("Enter third number : "))
mean1 = (a+b+c)/3   # here we are writing same things multiple times 
print(mean1)

d = float(input("Enter fourth number : "))
e = float(input("Enter fifth number : "))
f = float(input("Enter sixth number : "))
mean2 = (d+e+f)/3 # here we are writing same things multiple times 
print(mean2)



# making function 
def mean(a,b,c):
    mean = (a+b+c)/3
    print(mean)

# now 

mean(a,b,c) # Calling function and passing values of a,b,c to function mean() and it will calculate mean of a,b,c and print it
mean(d,e,f) # same things but it shorter and faster 
def maxmin(a,b,c):
    max_value = max(a,b,c)
    min_value = min(a,b,c)
    print("Maximum value is:", max_value)
    print("Minimum value is:", min_value)

maxmin(a,b,c)
maxmin(d,e,f)

