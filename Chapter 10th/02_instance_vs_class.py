class user:
    name = "Perry"
    salary = 120000 * 12
    location = "England"


user.location = "India"
# Any guess what will be printed? England or India
print(user.location)
"""
Instance attributes are always upper than class attributes.
"""
