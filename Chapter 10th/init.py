# __init__ is a gurter function which is automatically called.

from mimetypes import init


class Developer:
    # name = "Perry"
    age = 19
    language = "Python"

    def __init__(self, salary, language, name):  # creating instacne variables
        # init is a gurter function
        pass
        self.salary = salary
        self.language = language
        self.name = name


# Gurter functions are the functions which are automatically called
# They don't need a function call
# Init is the only function which calls itself as soon as the object is
# created with the class

# We can do some crazy things such as defining instance variables easily
# with init function

Perry = Developer(12000, "Py", "Perry") #everytime we create a funciton now we have to define like this for init as its intialized everytime
print(Perry.name, Perry.age, Perry.language)
