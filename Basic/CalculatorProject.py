first = input("Enter first number :")
operator = input("Enter input operator (+, - , * , / , %) :")
second = input("Enter second number :")

if(operator == "+"):
    print(int(first) + int(second))
elif (operator == "-"):
    print(int(first) - int(second))
elif(operator == "*"):
    print(int(first) * int(second))
elif(operator == "/"):
    print(int(first) / int(second))
elif(operator == "%"):
    print(int(first) % int(second))
else:
    print("invalid operator")
    