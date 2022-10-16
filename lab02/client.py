import time
import random
import os

message = input("Message: ")

file_id = random.randint(1, 123456789)
file_path = str(os.getcwd() + f"/message-{file_id}.txt")
file_name = str(f"message-{file_id}.txt")

with open(file_name, "w") as file:
    file.close()

with open("buffer.txt", "w") as file:
    file.write(file_path)
    file.write("\n")
    file.write(message)

time.sleep(2)

with open(file_name, "r") as file:
    print(file.readlines())

if os.path.exists(file_name):
  os.remove(file_name)
  print(f"file {file_id} removed")
else:
  print("The file does not exist")


