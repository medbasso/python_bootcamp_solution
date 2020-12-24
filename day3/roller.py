print("do you want to take  a ride")
age = int(input("what is you age?: "))

if age < 12 :
    bill = 5 
    print("child ticket are $5")
elif age <=18:
    bill = 7 
    print("youth tickets are $7")
elif age >= 45 and age <= 55 :
    bill = 0 
    print("free ride ;) ")
else:
    bill = 12 
    print("adulte tickes are $12")

wants_photo = input("do you want a photo taken? y or n ? : ")
if wants_photo == 'y':
    if age >= 45 and age <= 55:
        bill = 0
    else:
        bill+=3


print(f"the total bill is {bill}")