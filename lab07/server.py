import socket

game_map = {0: "rock", 1: "paper", 2: "scissors", 3: "lizard", 4: "Spock"}
rps_table = [[-1, 1, 0], [1, -1, 2], [0, 2, -1]]
rpsls_table = [[-1, 1, 0, 0, 4], [1, -1, 2, 3, 1], [0, 2, -1, 2, 4], [0, 3, 2, -1, 3], [4, 1, 4, 3, -1]]

IP = "127.0.0.1"
port = 1234
bufSize = 1024

UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPServerSocket.bind((IP, port))

print(f"Server started on addres {IP}:{port}")

while True:
    komA, addressA = UDPServerSocket.recvfrom(bufSize)    # zapisywanie graczy
    komB, addressB = UDPServerSocket.recvfrom(bufSize)

    player_a = addressA   # rozpoczynanie rozgrywki
    player_b = addressB
    player_a_score = 0
    player_b_score = 0
    i = 0

    while True:

        if addressA == player_a:      # rozpozpoznawanie graczy
            move_a = komA.decode()
            move_b = komB.decode()
        else:
            move_a = komB.decode()
            move_b = komA.decode()

        message = ""

        if move_a == "end" or move_b == "end":      # sprawdzanie komunikatów od graczy
            message = "end"
            UDPServerSocket.sendto(message.encode(), player_a)
            UDPServerSocket.sendto(message.encode(), player_b)
            print(f"Rounds: {i}. Player A score: {player_a_score}. Player B score: {player_b_score}")
            break
        else:
            winner = rps_table[int(move_a)][int(move_b)]

            if winner == int(move_a):       # sprawdzanie kto wygrał
                message = f"{winner}"
                player_a_score += 1
            elif winner == int(move_b):
                message = f"{winner}"
                player_b_score += 1
            else:
                message = f"draw"

        UDPServerSocket.sendto(message.encode(), player_a)      # wysyłanie odpowiedzi
        UDPServerSocket.sendto(message.encode(), player_b)
        i += 1
        komA, addressA = UDPServerSocket.recvfrom(bufSize)
        komB, addressB = UDPServerSocket.recvfrom(bufSize)
