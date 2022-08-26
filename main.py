num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

max = num1 if num1>num2 else num2
max = num3 if num3>max else max

print(max)