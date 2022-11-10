import sysv_ipc
import os
import random

server_key = 123
client_key = 321
pid = os.getpid()

wocabulary = ["dog", "cat", "fish", "lion", "python", "js", "html", "css"]

serverq = sysv_ipc.MessageQueue(server_key)
clientq = sysv_ipc.MessageQueue(client_key)

input("pres enter to start...")

for i in range(3):
    to_send = random.choice(wocabulary)
    serverq.send(to_send.encode(), True, pid)
    m, t = clientq.receive(True, pid)
    m = m.decode()
    print(f"{to_send}: {m}")
