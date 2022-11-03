import os
import random
import errno
import time

buffer = 'buffer'

fifo_name = f"fifo-{random.randint(1, 9999)}"
fifo_path = str(os.getcwd() + f"/{fifo_name}")
fifo_path_len = len(fifo_path)

ID = input("ID: ")

# stworzenie i otwarce kolejki czekania
try:
    os.mkfifo(fifo_name)
except OSError as oe:
    if oe.errno != errno.EEXIST:
        raise

# zapisanie się do kolejki servera
out = os.open(buffer, os.O_WRONLY)
os.write(out, f'{fifo_path_len}{ID}{fifo_path}'.encode())
os.close(out)


fifo_in = os.open(fifo_name, os.O_RDONLY)
fifo_out = os.open(fifo_name, os.O_WRONLY|os.O_NDELAY)

# oczekiwanie na odpowiedz
while True:
    message_len = os.read(fifo_in, 2)
    if len(message_len) > 0:
        message_len = int(message_len)
        message = os.read(fifo_in, message_len).decode()
        print("Message: ", message)
        break

    time.sleep(5)

os.close(fifo_in)
os.remove(fifo_path)
