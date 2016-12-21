#In memory space.it create an object with the name of
#function
#create docstring:documentation of your code
#annotation is an arbitrarty piece of information that can be associated with a
        #parameter(:type) or return value(->)
        #call by : function_name.__annotiation__
        #Other attribute:
        # - __name__
        #-__dict__
#passing of argument:
        #mutable:it changes from source
        #immutable : it dosent change the source value(string)
def subject(subject_code:str="CP1404",subject_name:str="Intro")->str:
    """

    :param subject_code:the code associated with the subject,
    :param sunject_name:the full name of subject
    :return:string equivalent
    """
    string_msg="This subject{}refer to {}".format(subject_code,subject_name)
    return string_msg,"ipio"
print(subject("CP1404","Programming I"))
print(subject.__doc__)
print(subject.__annotations__)
print(subject.__dict__)
(x,y)=subject()
tup=subject()




#Mutable list
my_list=[1,2,3]
my_list[1]=100
print(my_list)


"""
when def is evaluated,it is done only once.
the associationis preserved btw invocation
"""