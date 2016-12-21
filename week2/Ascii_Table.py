# lower = 10
# upper = 100
# print("Enter a number ({}-{}):".format(lower,upper))
# #2
# for i in range(10, 120, 1):
#     print("{} {:>5}".format(i, chr(i)))
def method_name():
    pass
    # while (flag):


# flag=True
method_name()
#   try:
#    print("1")#try program is running or not
#    user_input=int(input("Give me Number Please:"))
#    print("You Have Entered{}".format(user_input))
#   except ValueError:
#     print("Please enter a value number.")
# print("finish.")

def get_number(lower,upper):
    flag=True
    while(flag):
        try:
            user_input = int(input("Enter a number {} - {}".format(lower, upper)))
            while user_input<10 or user_input>50:
                print("Please type again")
                user_input = int(input("Enter a number {} - {}".format(lower, upper)))
            return user_input
            flag = False
        except ValueError:
            print("Try Again")
def main():
    user_input=get_number(10,50)
    print("Your Number is: ",user_input)
main()
