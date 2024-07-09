a = "Make a lot of money"
b = "buy now"
c = "subcsribe this"
d = "click this"
print(a, b, c, d)
comment = input("Enter your comment: ")

if(a in comment or b in comment or c in comment or d in comment):
    print("Your comment has been blocked.")

else:
    print("Your comment has been posted")    