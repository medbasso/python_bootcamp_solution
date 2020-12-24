fizz = 'fizz'
buzz = 'buzz'
 
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        i = fizz + buzz
    elif i % 3 == 0:
        i = fizz
    elif i % 5 == 0 :
        i = buzz
    print(i)
