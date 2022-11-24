import random
import socket
import time

game_map = {0:"rock", 1:"paper", 2:"scissors", 3:"lizard", 4:"Spock"}

serwerAdresPort = ("127.0.0.1", 1234)
klientAdresPort = ("127.0.0.1", random.randint(1235, 80000))
bufSize = 1024

UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

i = 0
points = 0
when_end = random.randint(1, 20)

while True:
    time.sleep(random.random()*2)
    if when_end == i:
        print("I'm fine, time to end")
        UDPClientSocket.sendto("end".encode(), serwerAdresPort)
        break
    choise = random.randint(0, 2)
    print(f"I chose {game_map[choise]}")

    UDPClientSocket.sendto(str(choise).encode(), serwerAdresPort)
    response, adres = UDPClientSocket.recvfrom(bufSize)
    response = response.decode()

    if response == "end":
        print("Secound player ended game :-(")
        break
    elif response == "draw":
        print("It was draw...")
    elif int(response) == choise:
        print("I won this one")
        points += 1
    else:
        print("Unlucky, I lost...")
    i+=1

print(f"Final score {points}/{i}")




