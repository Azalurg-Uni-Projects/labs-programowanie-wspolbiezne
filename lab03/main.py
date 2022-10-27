import os


def count(p, s, toGo, went) -> int:
    suma = 0
    went += 1

    with open(p, "r") as f:                             # czytanie pliku
        content = f.read()

    for line in content.split("\n"):
        for word in line.split(" "):                    # liczenie słów
            if word == s:
                suma += 1

        if "\input" in line:                            # szukanie inputów
            l = len(line)
            toGo.append(line[7:l - 1])

    if len(toGo) == went:                               # sprawdzenie czy trzeba się gdzieś jeszcze zagłębiać
        return suma

    pid = os.fork()                                     # fork

    if pid > 0:
        status = os.wait()                              # proces macierzysty
        if os.WIFEXITED(status[1]):
            return suma + os.WEXITSTATUS(status[1])

    else:
        os._exit(count(toGo[went], s, toGo, went))      # syn


print(count("1.txt", "Linia", [], -1))
