'''
* * *
*   *
* * *
'''

star = "*"
number = int(input("Enter number: "))
for i in range (number+1):

    print(i*"*")
    if (i == 3):
        print(f({star}, {star}, {star}))
    elif( i == 2):
        print(f({star}, {star}))
    if (i == 3):
        print(f({star}, {star}, {star}))
    
