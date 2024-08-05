class Programmer:
    def __init__(self, name, language, age, salary):
        self.organization = "Microsoft"
        self.name = name
        self.language = language
        self.age = age
        self.salary = salary


Perry = Programmer("Perry", "Python", "18", "120000")
Garry = Programmer("Garry", "Python", "18", "12000")

print(Perry.name, Perry.age, Perry.language, Perry.salary, Perry.organization)
print(Garry.name, Garry.age, Garry.language, Garry.salary, Perry.organization)
