a = int(input("Enter your specified number: "))

for i in range(2, a):
    i = i + 1
    if(a%i == 0):
        print(a,"is not a prime number")
        break

else:
    (a, "is a prime number")
