for i in range(1, 21):
    # print(i)
    with open(f"tables/{i}Table.txt" , "w") as generate:
        with open(f"tables/{i}Table.txt", "a") as f:
            for a in range(1,11):
                f.write(f"{i} X {a} = {i*a}\n")
