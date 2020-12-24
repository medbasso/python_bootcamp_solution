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
nr_numbers = int(input("how many numbers would you like\n"))

 

letters_f = random.sample(letters, nr_letters)
numbers_f = random.sample(numbers, nr_letters)
symbols_f = random.sample(symbols, nr_symbols)
password = letters_f + numbers_f + symbols_f
print(*password, sep="")