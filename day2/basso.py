print("welcom to the tips calculator")
bill = float(input("what was the total bill? $"))
split = int(input("how many peopel to split the bill ? "))
tips = int(input("what porcentage tips would you like to give , 10 or 12 or 15: "))
bill_par_person = bill / split
tips_par_person = bill_par_person * tips   / 100 
total_bill_each_person = bill_par_person + tips_par_person 
final_amount = round(total_bill_each_person, 2)
print(f"each person should pay : ${final_amount}")
