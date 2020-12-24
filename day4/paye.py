# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#finals_names = random.choice(names)
#print(f"{finals_names} is going to buy the meal today!")
names_item = len(names)
generate_numbers = random.randint(0, names_item - 1)
final_step = names[generate_numbers]
print(final_step  + " who will buy the meal")
#elif len(names)== 5 :
    #print(f"{names[3]} is going to pay")

