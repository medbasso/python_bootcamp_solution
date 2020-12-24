age = input("what is your current age :  ")

age_left =  90 - int(age)

days = age_left * 365 
weeks = age_left * 52 
month = age_left * 12 
if (int(age)>= 0 and int(age)<= 90):
    print(f"you have {days} days, and {weeks} weeks, and {month} month left ")
else:
    print("wrong age you are dead")