# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combine = name1.lower() + name2.lower()

true_score = combine.count('t')+ combine.count('r')+combine.count('u')+combine.count('e')
love_score = combine.count('l')+ combine.count('o')+combine.count('v')+ combine.count('e')
final_score = str(true_score) + str(love_score)

if int(final_score) <  10 or  int(final_score) > 99:
    print(f"your final score is {final_score}, you go together like coke and mentos")
elif int(final_score) >= 40 and int(final_score) <= 50:
    print(f"your score is {final_score},  you alright toghether")
else:
    print(f'your final score is {final_score}')   