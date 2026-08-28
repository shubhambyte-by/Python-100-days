# age = int(input("Enter your age : "))
# if (age < 18):
#     print("You are not eligible for vote")
# else:
#     print("You are eligible for vote ")    


#A price tag machine
appleprice = 200
budget = float(input("Enter your budget : "))
cout   = float(input("Which Kg apple you want to buy:"))


final_price = appleprice*cout


if (budget>= final_price):
    print("Alexa , add", cout, "kg apple in cart")
else: 
    print("You can choose different fruit")

remining_price = float(budget)-float(final_price)

print("Your remining money is : ", remining_price)
print("Do you want to buy something else ?")
yes = input(" if yes write Y ")
Y = yes 

orange = 300
if (yes == Y):
    print("Do you  want to buy orange ?")
    if (yes ==Y):
        print("which kg you want to buy :")
        couto = float(input())
        final_bill = couto*orange
        if (remining_price>= final_bill):
            print("Alexa add", couto,"Amount of orange in cart")
        else:
            print("You have not enough cash to buy orange ")
    elif(no == N):
        print("Thank you For coming this store! Have a great day ...")
no = input(" if no write N ")
N = no

if (no == N ):

    print ("Thank you , your remining amout is : ")        

    