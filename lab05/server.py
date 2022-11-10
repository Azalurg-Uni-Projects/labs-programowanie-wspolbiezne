import sysv_ipc
import signal
import sys
import time


def handler(signum):
    print(' Obsługa sygnału ', signum)


def handler1(signum):
    print(' Inna obsługa  sygnału ', signum)
    print("Server stop")
    serverq.remove()
    clientq.remove()
    sys.exit(0)


signal.signal(signal.SIGINT, handler1)

signal.signal(signal.SIGUSR1, handler1)

dictionary = {
    "dog": "pies",
    "cat": "kot",
    "fish": "ryba",
    "lion": "lew",
    "python": "pyton"
}

server_key = 123
client_key = 321

print("Server start")

serverq = sysv_ipc.MessageQueue(server_key, sysv_ipc.IPC_CREAT)
clientq = sysv_ipc.MessageQueue(client_key, sysv_ipc.IPC_CREAT)

for i in range(3):
    m, pid = serverq.receive(True, 0)
    m = m.decode()
    response = dictionary.get(m, "Nie znam takiego słowa")
    clientq.send(response.encode(), True, pid)
    time.sleep(2)

print("Server stop")
serverq.remove()
clientq.remove()
