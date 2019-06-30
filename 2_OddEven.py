x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

val = x%y

if val == 0:
    print("Can be divided by y")

elif val == 0 and y == 2:
    print("x is even number")

else:
    print("x is neither even number nor can be divided by y")