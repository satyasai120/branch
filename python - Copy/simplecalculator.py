

num1 = int(input("give 1st number: "))
num2 = int(input("give 2nd number: "))
operator = input("give me operator: ")
 
if operator == "+":
   print(f"addition of 2 numbers is {num1+num2}")
elif operator == "-":
   print(f"subraction of 2 numbers is {num1-num2}")
elif operator == "/":
   print(f"division of 2 numbers is {num1/num2}")
else:
  
  print("invalid operator")

