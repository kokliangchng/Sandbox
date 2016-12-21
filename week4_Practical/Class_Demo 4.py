# words={}
# word["avalanche"]="""
#
# """
#
# #palnt={}#key is name,value os the color
# plants={"carrot":"orange",
#        "raddish":"white",
#        "beetroot":"red"
#        }
# plants["mango"]="yellow"
#
# for each in plants:#return to keys
#     print("Getting plant:{},value:{}".format(each,plants[each]))
# #print(plants)
#
# #print(plants.item())
# for key,value in plants.items():
#     print("{:10s}->{:10s}".format(key,value))
#
# for value in plants.values():
#     print(value)



names=["john","john","ann","jane"]#list of name
#count the occurence of each name
count={}#jogn=2

for each in names:
    if each in count:#if it exist in count dict
        count[each]+=1
    else:#first time
        count[each]=1
        print(count)