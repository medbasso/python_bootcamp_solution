height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
MBI = weight / (height * height)
MBI_final = round(MBI, 2)
print(f"your MBI is: {MBI_final}")
