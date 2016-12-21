def main():
    number=[]
    for a in range(0,5):
        number.append(int(input("Insert Number: ")))
    print("The first number is: ",number[0])
    print("The last number is:",number[-1])
    print("The smallest number is:" , min(number))
    print("The largest number is:",max(number))
    print("The average of the number is:",sum(number)/5)

main()

# def main():
#     number=[]
#     for i in range(0,5):
#         number.append(int(input("Insert Number:")))
#     print("The first number is:",number[0])
#     print("The last number is",number[-1])
# main()