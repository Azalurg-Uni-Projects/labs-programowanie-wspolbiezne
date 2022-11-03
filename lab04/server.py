import os
import errno
import time

FIFO = 'buffer'
DB = {
    "01": {"name": "Karmel!", "len": "07"},
    "02": {"name": "Ciastko!!", "len": "09"},
    "03": {"name": "Czekolada!!!", "len": "12"}
}


try:
    os.mkfifo(FIFO)
except OSError as oe:
    if oe.errno != errno.EEXIST:
        raise

fifo_in = os.open(FIFO, os.O_RDONLY)

fifo_out = os.open(FIFO, os.O_WRONLY|os.O_NDELAY)

while True:
    message_len = os.read(fifo_in, 2)
    if len(message_len) > 0:
        message_len = int(message_len)
        db_id = os.read(fifo_in, 2).decode()
        path = os.read(fifo_in, message_len).decode()
        print(message_len, db_id, path)

        response = os.open(path, os.O_WRONLY)
        os.write(response, f'{DB[db_id]["len"]}{DB[db_id]["name"]}'.encode())
        os.close(response)
    time.sleep(5)
