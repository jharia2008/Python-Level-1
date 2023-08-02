number1= int(input("put in the first number"))
number2= int(input("put in the second number"))
operation= input("put in the operation to use")
if operation == "+":
    print(number1 + number2)
elif operation == "-":
    print(number1 - number2)
elif operation == "*":
    print(number1 * number2)
elif operation == "/":
    print(number1 / number2)
else :
    print("Error")