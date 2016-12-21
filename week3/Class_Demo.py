# Use try except to handle problematic situattion
#Error occurs when the normal fllow of program is disrupted
#Value Error occur when the inout does not tally with the expected type.
#there are 2 parts to exception:Try the risky code
#
#                                        Except,manage/contain the error,could have multiple except
""
# flag=True#none stop
#
# while (flag):
#   try:
#    print("1")#try program is running or not
#    user_input=int(input("Give me Number Please:"))
#    print("You Have Entered{}".format(user_input))
#   except ValueError:
#     print("Please enter a value number.")
# print("finish.")
#
# try:
#     numerator=int(input("Enter the numerator:"))
#     denominator=int(input("Enter the denominator(Enter a non zero):"))
#     while denominator==0:
#         print("Cannot divide by zero.")


#"""
# 1.When will a Value Error occur?When a non-numetric is entered
# 2.When will a zerodivisionError occur?When a zero is entered as denominator
# 3.Could you change the code to avoid the possibility of a ZeroDivisonError?
#
# # """
# # Get a filename from user with extension.
# # Try open the file using the filename.
# # Prompt error message if the file does not exist.
# # Or else, read out the content of the file.
# # """
# """
# open(),close(),try,except,print()
# """
# flag=True
# while(flag):
#  try:
#      filename=input("Enter the file name")
#      filepointer=open(filename)
#      for each in filepointer:
#          print(each)
#      filepointer.close()
#      flag=False
#  except FileNotFoundError:
#     print("Enter a valid filename")



"""
1.name**- meaningful,lowercase
2.input argument-optional,can be up to any number
3.return-optional,usually only one

"""
def get_number():
    user_input=int(input("prompt"))
    return user_input

def get_name(prompt="Default enter:"):
    user_input=str(input(prompt))
    return user_input

def check_calories(item1,item2):
    ITEM1_CALORIE=50
    ITEM2_CALORIE=100
    TOTAL_CALORIE=item1*ITEM1_CALORIE+item2*ITEM2_CALORIE
    if TOTAL_CALORIE>500:
        return "Watch your diet"
    elif TOTAL_CALORIE>300:
        return "You are the borderline"
    else:
        return"Safe"


#get_number()#function call
#get_name("Enter a kind of food:")
food1Qty=get_number("Enter how quality food1")
food2QTY=get_number("Enter how quality food2")
print(check_calories(food1Qty,food2QTY))
