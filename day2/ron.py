print("welcom to the tips calculator")
bill = float(input("what was the total bill? $"))
tips = int(input("how match tips would you like to give, 10 or 12 or 15?$ "))
people = int(input("how many people to splite this bill ? : "))

tips_person = tips / 100 
bill_tips = bill * tips_person
total_bill = bill + bill_tips
bill_person = total_bill / people
final_amount = round(bill_person, 2)

print("each person should pay $", final_amount)

