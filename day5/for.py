# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
students = 0 
for s in student_heights:
    students = students + s 
#n == height of list we add one because start with 0
n = n + 1 
average = count / n 
average_final = int(round(average, 0))
print(average_final)
  
  
