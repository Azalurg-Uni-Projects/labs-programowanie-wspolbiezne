import time

print("server started")

while True:
    k = "a"
    with open("input.txt", "r") as file:
        k = file.readline()
        if len(k) > 0:
            k = int(k)

    if type(k) == int:
        with open("output.txt", "w") as file:
            file.write(f"{k*2 + 3}")

        with open("input.txt", "w"):
            pass

    time.sleep(0.5)
