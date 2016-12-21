num = int(input("Enter the num of item"))
while num<=0:
    print('Invalid number of items!')
    num =int(input("Enter item"))

cost=int(input("Enter the shipping cost:$"))
while num<=0:
    print('Invalid number of item!')
    num=int(input("Enter cost:$"))

price=num+cost
if price>=100:
    total=price*1.10
    print(total)
else:
    print(price)

# num=int(input("Enther the num of item"))
# while num<=0:
#     print("Error")
#