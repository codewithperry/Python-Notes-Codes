'''
***
**
*
'''

'''
****
***
**
*
'''

'''
7
6
5
4
3
2
1
'''
number = int(input("Enter the number: "))
def star_print(number):
    if number == 0 :
        return
    star_print(number - 1)
    star = number * "*"
    print(star)
    
star_print(number)
# star_print(number)

