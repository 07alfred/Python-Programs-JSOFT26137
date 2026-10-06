#ALGORITH FOR CHECHKING LARGEST OF THREE NUMBERS
#Start
#Read three numbers: a, b, and c.
#If a > b and a > c, then display a is the largest.
#Else if b > a and b > c, then display b is the largest.
#Else, display c is the largest.
#Stop

a = float(input("Enter  number a:"))
b = float(input("Enter  number b:"))
c = float(input("Enter  number c:"))
if a >= b and a >= c:
  print(a, "is the largest number.")
elif b >= a and b >= c:
  print(b, "is the largest number.")
else:
  print(c, "is the largest number.")
