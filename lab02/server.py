import time
import random

print("server started")

responses = ["yes", "no", "I don't know", "maybe"]

while True:
    path = ""
    message = ""
    with open("buffer.txt", "r") as file:
        path = file.readline()
        message = file.readline()

    if len(path) > 0:
        with open(path, "w") as file:
            file.write(f"response: {random.choice(responses)}\n")
            file.write(f"message: {message}")

        with open("buffer.txt", "w"):
            pass

    time.sleep(0.5)
