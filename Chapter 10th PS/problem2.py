class calculator:
    @staticmethod
    def greet():
        print("Hello...")

    @staticmethod
    def calc():
        user_input = int(input("Enter a number: "))
        print(f"Square root of: {round(user_input**(1/2),2)}")


mycalculator = calculator()
mycalculator.greet()
mycalculator.calc()
