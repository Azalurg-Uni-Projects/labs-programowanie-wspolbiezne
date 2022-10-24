import time
import random
import os
import errno

is_lock = True

message = input("Message: ")

file_id = random.randint(1, 123456789)
file_path = str(os.getcwd() + f"/message-{file_id}.txt")

with open(file_path, "w") as file:
    file.close()

while True:
    if not os.path.exists("lockfile"):
        lock = os.open("lockfile", os.O_CREAT | os.O_EXCL | os.O_RDWR)
        print("Create lockfile")
        break
    else:
        if is_lock:
            print("I'm lock :-(")
            is_lock = not is_lock
        time.sleep(1)

with open("buffer.txt", "w") as file:
    file.write(file_path)
    file.write("\n")
    file.write(message)

for x in range(5, -1, -1):
    print(x, end=" ")
    time.sleep(1)
print("GO!")

with open(file_path, "r") as file:
    print(file.read())

if os.path.exists(file_path):
    os.remove(file_path)
    print(f"file {file_id} removed")
else:
    print("The file does not exist")

os.close(lock)
os.unlink("lockfile")
