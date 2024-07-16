def greatest_number():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))

    if a > b and a > c:
        print("The greatest number is:",a)
    if b > c and b > a:
        print("The greatest number is:",b)
    if c > a and c > b:
        print("The greatest number is:",c)
greatest_number()
