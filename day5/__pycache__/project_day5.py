#password generator project
import random 
letters = ['a', 'b', 'c', 'd', 'e', 'f',
'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '£', '(', ')', '*', '+']

print("welcom to the PyPassword  Generator!")
nr_letters = int(input("how many letters would you like in your password\n "))
nr_symbols = int(input("how many symbols would you like\n"))
nr_numbers = int(input("how many symbols would you like\n"))

password = []
for char in range(1, nr_letters + 1):
    password+=random.choice(letters)
for char in range(1, nr_letters + 1):
    password+=random.choice(numbers)
for char in range(1, nr_letters + 1):
    password+=random.choice(symbols)
random.shuffle(password) 
print(*password, sep="")
 