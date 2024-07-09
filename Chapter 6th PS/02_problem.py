a = int(input("Enter first subject marks:"))
b = int(input("Enter second subject marks:"))
c = int(input("Enter third subject marks:"))

if a / 100 >= 33 / 100:
    print("Student has passed in first subject:")
else:
    print("Student has failed in first subject")

if b / 100 >= 33 / 100:
    print("Student has passed in second subject:")
else:
    print("Student has failed in second subject")

if c / 100 >= 33 / 100:
    print("Student has passed in third subject:")
else:
    print("Student has failed in third subject")

if (a + b + c) / 300 >= 120 / 300:
    print("Student has passed!")
else:
    print("Better luck next time!")
