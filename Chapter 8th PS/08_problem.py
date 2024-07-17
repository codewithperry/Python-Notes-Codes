a = int(input("Enter the number whose multiplication table is required: "))

def multiplication_table():
    for i in range (1,11):
        print(f"{a} X {i} = {a*i}")
multiplication_table()