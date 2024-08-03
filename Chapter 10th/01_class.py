class Developer:

    language = "Python"  # this is a class attribute as they belong to this class
    salary = 1200000000000000  # this is a class attribute as they belong to this class
    qualifications = (
        "Btech in CSE"  # this is a class attribute as they belong to this class
    )

    titles = (
        "Senior Developer"  # this is a class attribute as they belong to this class
    )


a = Developer()
b = Developer()

a.name = "Perry"  # this is a instance attributer
print(a.name, a.salary)

b.name = "Dhariye"  # this is a instance attributer
print(b.name, b.salary)
