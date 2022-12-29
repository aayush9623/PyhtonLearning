a=5
#b=2
b=2
try:
    print("resource open")
    print(a/b)
except ZeroDivisionError as e:
    print("Hey you divided by zero", e)
try:
    k = int(input("Enter the number : "))
    print(k)
except ValueError as e:
    print("Invalid value", e)
except Exception as e:
    print("Something went wrong")
finally:
    print("resource closed")


