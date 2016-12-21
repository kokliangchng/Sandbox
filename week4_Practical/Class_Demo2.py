# import random
# from operator import itemgetter
# def get_day(num):
#     days=["Sun","mon","tues","wed","thur","fri","sat"]
#     print (days[num])
#     print(random.randint(0,10))
# get_day(0)
#
# foods=['Sandwich','burger','Chicken Rice','Udon','TC','sushi']
# print(list(range(7)))
# for i in range(7):
#     daily_meals=[]
#     for j in range(3):
#             rand_num=random.randint(0,len(foods)-1)
#             daily_meals.append(foods[rand_num])
#          print("{}:breakfast {};lunch {} .".format(get_day(i),daily_meals[0],daily_meals[1],daily_meals[2]))
#
#
#
# name_list=[["John",20,"Yellow"],["Jordan",25,"Red"],["Dunken",30,"Black"]]
# print("before sort:",foods)
# foods.sort()
# print("after sort:",name_list)
# name_list.sort(key=itemgetter(1,0))
# print("after sort:",name_list)
#
# def test(num1=0,num2=0,text=""):
#      print(num2)
#
# test(num1=99)
#
# print(foods)
#
# str1="**"
# str2="abcd"
# print(str1.join(foods))
# print(str2)
# print(sorted(str2))




# new_list=[]
# for each in range(100):
#     new_list.append(each*2)
#
# new_list_comp=[each*2 for each in range(100)]
# print(new_list_comp)



def print_header():
    print("""

    """)


def read_file():
    global file_list
    file_pointer=open(FILENAME,"r")
