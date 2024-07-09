username = input("Enter your username: ")

username_lenth = len(username)

if(username_lenth>10):
    print("Username contains more than 10 characters")

elif(username_lenth==10):
    print("username contains 10 characters")

elif(username_lenth<10):        
    print("Username contains less than 10 characters")
    print("Your account has been created on mooscript.com uwu!")


print("Thanks for registering.")    