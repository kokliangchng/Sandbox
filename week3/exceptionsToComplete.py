finished=False
result=0
while not finished:
    try:
        result = int(input("Enter a number"))
        finished=True
        pass
    except ValueError:
        print("Please enter a valid number")
print("Valid result is :",result)