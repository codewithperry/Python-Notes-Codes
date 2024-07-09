name_list = ["Moo", "Perry", "Ayan", "Rohan"]

a = input("Enter the username to check if it already exists: ")


if a in name_list or a in name_list or a in name_list or a in name_list:
    print("This name already exists")
else:
    print("This name will be added to the list and the updated list will be printed below.", name_list.append(a))
    print(name_list)

