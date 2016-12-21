Text="this is a collection of words of nice words this is a fun thing it is"
count={}
Text=Text.split(" ")
for each in Text:
    if each in count:#if it exist in count dict
        count[each] += 1
    else:#first time
        count[each]=1
for key in sorted(count):
    print("{} : {}".format(key,count[key]))
