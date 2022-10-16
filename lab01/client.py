import time
a = int(input("Number: "))

with open("input.txt", "w") as file:
    file.write(str(a))

time.sleep(1)

with open("output.txt", "r") as file:
    print(f"Result: {file.readline()}")

with open("output.txt", "w"):
    pass
