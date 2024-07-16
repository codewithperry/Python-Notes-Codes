def greet(name):
    print(f"{name} have a good day.")
greet("Perry")
greet("Harry")
#Giving name through argument.
#Perry is the argument passed as name

def user_data(name,age):
    print(f"{name} is {age} years old")
user_data("Perry",18)
user_data("Harry",21)

#Perry is being passed as name argument 
#18 being as age argument

def explaining_return():
    return "Bro you cannot return me haha."
#return is used to return a value of a function.
#Either you can customize it like this,
#or put a real value in it
a = explaining_return()
print(a)


first_digit = 1
second_digit = 2
def explaining_return():
    sum = first_digit + second_digit
    print(sum)
    return "10"
explaining_return() #function call
a = explaining_return()
print(a) #return variable
"""
Output:
3
3
10 
"""
#Two times 3 because a a is calling the function.
#But both the return and the print(sum).