age = int(input("Enter your aage : "))
Child = 150
Adult = 300
Senior = 200
if(0<age<=12):
    num = int(input("Enter Number of child : "))
    tktprice = Child*num
    print("Your payble amout is ₹",tktprice)
if(12<age<=59):
    num = int(input("Enter Number of Adult : "))
    tktprice = Child*num
    print("Your payble amout is ₹",tktprice)
if(59<age<100):
    num = int(input("Enter Number of Senior : "))
    tktprice = Child*num
    print("Your payble amout is ₹",tktprice)
    

