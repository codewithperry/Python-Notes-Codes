class getInfo:
    name = "Samy"
    salary = 100000 * 12
    location = "India"

    def india(self):
        print(
            f"The name of the developer is {self.name} and this amazing dev is from {self.location}. The salary is {self.salary}"
        )


perry = getInfo()
perry.india()
