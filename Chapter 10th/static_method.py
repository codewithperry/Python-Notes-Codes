# We can use static method to define a call which doesnt require passing a object such as "self"


class Developer:

    # name = "Perry"
    age = 19
    language = "Python"

    # now for example I just want to print "Have a good day!"
    def greet2(self):
        print("Hello World")

    # Now if we do the same process without non static method
    @staticmethod
    def greet():
        print("Have a nice day")


Perry = Developer()
Perry.greet()
Perry.greet2()
