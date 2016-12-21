"""
week 4 demo
midterm-
format:12 MCQ(12 marks)+5 written(12 marks)
Evaluate expression(precedence of operator)
predict the output::Explain how the code start,where does it branch to...
finally write the output at the bottom.
-write code:function!!!FIle IO!!!Except!!Know when different type of except come out.
String:format()
Lecture 1-4

"""
# # # find vowel
name=input("Name:")
vowel=("aeiouAEIOU")
count=0
for each in name:
    if each in vowel:
        count+=1
print("Out of {:2} letters {} has {} vowel".format(len(name),name,count))
print("Out of ", len(name),"letters ", name, "has ", count,"vowel")#next example


# #names=[]
# names=["Alice","Tom","John"]#list of string
# ages=[12,13,15]#list of int
# print(names[-1])
# print(names[1])#print 2nd data
#
# while True:
#     name=input("Enter a name:")
#
#     if name=="":
#         break#exit while loop
#     names.append(name)#show your data
# print(names)
# print(names[0:1])
# print(names+names+names)#same with *3
# print(names*3)#repeat
# print(len(names))#show got how many in list
#
# """
# List is mutable(any changes,reflects on the original list)string is immutable.
# -ordered(0,1,2,3)
# name=["Tom","Liang","asdasd"]
# name=[0:1]:slicing
# names+names:
# names*10:repeat
# len:get total length
# name=input(name)for user input
# #
# # """
#
#
# """
# write a function takes in a number the return the corresponding day of the week
# eg.get_day(0) should return "Sun"
# """



