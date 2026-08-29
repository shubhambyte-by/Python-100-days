# ----------------------This code is for Calculation of Electricity bill ---------------------



unitconsumed = float(input("Enter which number of unit you have consumed : "))

# There are 4 types of price distribution programm
# if your bil is more than 1000 , than you will more 10% more

if (unitconsumed<100):
    bill = unitconsumed*1.50
    print("Your electricity bill is ₹", bill)
    if(bill>1000):  # this is for when bill is more then 1000
        bill = bill*10/100 + bill
        print("Your electricity bill PAYABLE AMOUNT  is ₹ ",bill)

if (100<=unitconsumed<200):
    bill = unitconsumed*2.50
    print("Your electricity bill is ₹", bill)
    if(bill>1000):# this is for when bill is more then 1000
        bill = bill*10/100 + bill
        print("Your electricity bill PAYABLE AMOUNT  is ₹ ",bill)    

if (200<=unitconsumed<300):
    bill = unitconsumed*4.00
    print("Your electricity bill is ₹", bill)
    if(bill>1000):# this is for when bill is more then 1000
        bill = bill*10/100 + bill
        print("Your electricity bill PAYABLE AMOUNT  is ₹ ",bill)    

if (300<=unitconsumed):
    bill = unitconsumed*6.00
    print("Your electricity bill is ₹ ", bill)
    if(bill>1000): # this is for when bill is more then 1000
        bill = bill*10/100 + bill
        print("Your electricity bill PAYABLE AMOUNT  is ₹ ", bill)    







