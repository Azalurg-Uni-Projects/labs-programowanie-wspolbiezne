import time
import random
from datetime import datetime

print("server started")

responses = ["yes", "no", "I don't know", "maybe"]

while True:
    path = ""
    message = ""
    with open("buffer.txt", "r") as file:
        path = file.readline()[:-1]
        message = file.readline()

    if len(path) > 0:
        with open(path, "w") as file:
            file.writelines([f"response: {random.choice(responses)} \n", f"message: {message}"])
            print(datetime.now().strftime("%H:%M:%S"), "\u0332".join(f"{message}"))

        with open("buffer.txt", "w"):
            pass

    time.sleep(0.5)
