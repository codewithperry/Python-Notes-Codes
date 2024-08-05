import random


class Train:
    starting_destination = input("Enter the starting destination of your journey: ")
    ending_destination = input("Enter the last destination of your journey: ")
    available_seats = random.randint(40000, 50000)
    fare = random.randint(500000, 700000)


information = Train()
print(f"The current available seats are: {information.available_seats}")
print(
    f"The fare from {information.starting_destination} to {information.ending_destination} is {information.fare} only"
)
