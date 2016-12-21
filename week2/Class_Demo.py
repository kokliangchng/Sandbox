long_str="""
Line1
        Line2
Line3
"""
print(long_str)
###"""<<exactly same with design on the top\


#print timetable
print("My timetable.")
for each in range(10):
    print(each,"*5=",each*5)



    #escape character
    #\n New Line;\t a tab space
    print("\t1*1=1 \t1*2=2")



"""
 #ascii printing
 print(chr(97))#print the ascii character associated with ordinl number 97
 print(ord('a'))

 for num in range(32,125):
     print(str(num),"->",chr(num),end="\t")#<<if want add tab space
"""


# greet="How are you?"
# name="John"
# day="Monday"
# print("Original str:",greet)
# print("Position 1:",greet[1])
# print("Position 0-6:",greet[0:7])#slicing
# print("Position at odd number:",greet[1::2])#print starting from position 1 to the end,seperated by 2 position
# print("Negatife indexing-4:",greet[-4])
# print("In Between2,-2",greet[3:-4])
#
#
# #Given the string str1="abcdefghij"
# #a)'jihggfedcba
# #b)adgj
# #c)igeca
# str1="abcdefghij"
# print(str1[-1::-1])#<<Descending
# print(str1[::3])
# print(str1[-2::-2])
#
#
# """
# String Methods(function)
#
# """
# str1="howdy today"
# print(str1.capitalize())#capital in first alphabet
# print(str1.upper())#all capital
# print(str1)#IMMUtable string
# print(str1.isupper())
# print(len(str1))
#
# for index in (str1):
#     print(index)
#
# for index,letter in enumerate(str1):
#     print(index,"->",letter)
#
# print("to"in str1)#to check
#
# #string format
# greet="How are you?"#0
# name="John"#1
# day="Monday"#2
# new_str="{0}{1}.\n Good {1}{1}!".format(greet,name,day)
# print(new_str)
#
# short_str="This"
# print("{:20s} is Cp1201".format(short_str))###:20s=20 space   default alignment of string is left
# print("{:>20s} is CP1044.".format(short_str))#align to right
# print("{:^20s} are CP1231".format(short_str))#align center
#
#
# number1=523
# print("${}".format(number1))
# # print("${:.2f}".format(number1))#2 decimal
# print("${:010.4f}".format(number1))#zero pending