b = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, %): ")
a = float(input("Enter second number: "))

if operator == "+":
  print("Result:", a + b)
elif operator == "-":
  print("Result:", a - b)
elif operator == "*":
  print("Result:", a * b)
elif operator == "%":
  print("Result:", a % b)
else:
  print("Invalid operator")
