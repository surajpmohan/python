import calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a,"+",b,"=",calculator.add(a, b))
print(a,"-",b,"=",calculator.subtract(a, b))
print(a,"*",b,"=",calculator.multiply(a, b))
print(a,"/",b,"=",calculator.divide(a, b))