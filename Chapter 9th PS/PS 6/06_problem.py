file = open("PS 6/finepython.txt")
data = file.read()
readable_data = data.lower()

if "python" in readable_data:
    print("Python word detected.")
else:
    print("Python word not detected")
