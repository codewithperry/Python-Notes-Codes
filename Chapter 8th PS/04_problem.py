number_of_natural_number = int(input("Enter the number of natural numbers you want to add: "))
a = 0
def Natural_Number_Add(a):
    for i in range (1, number_of_natural_number+1):
        a = a + i
    print(a)
Natural_Number_Add(a)    

#Recursive Function to add

'''
3 
3+2+1
4
4+3+2+1

sum(n) = 1 + 2 + 3 + 4...n
sum(n) = 1 + 2 + 3 + 4...(n-1) + n
'''
def sum(number_of_natural_number):
    if number_of_natural_number==0:
        return 0
    return number_of_natural_number + sum(number_of_natural_number-1)
print(sum(number_of_natural_number))
