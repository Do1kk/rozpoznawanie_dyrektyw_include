import sys

input = '''#include <errno.h>'''


# Deterministyczny automat skończony.
class das:

    # Wszystkie możliwe stany.
    # STAN, WARTOŚĆ, NOWY STAN
    przejścia = (
        ('A', '#', 'B'),
        ('B', 'i', 'C'),
        ('C', 'n', 'D'),
        ('D', 'c', 'E'),
        ('E', 'l', 'F'),
        ('F', 'u', 'G'),
        ('G', 'd', 'H'),
        ('H', 'e', 'I'),
        ('I', ' ', 'I'),
        ('I', '<', 'J'),
        ('I', '"', 'K'),
        ('J', 'abcdefghijklmnopqrstuvwxyz', 'J'),
        ('K', 'abcdefghijklmnopqrstuvwxyz', 'K'),
        ('J', '>', 'P'),
        ('K', '"', 'P'),
        ('J', '.', 'L'),
        ('K', '.', 'Ł'),
        ('L', 'h', 'M'),
        ('Ł', 'h', 'N'),
        ('M', '>', 'P'),
        ('N', '"', 'P'),
    )


output = ''
stan = das.przejścia[0][0]
for i in input:

    # Znajduje wszystkie możliwe przejścia dla stanu.
    lista = [item for item in das.przejścia if item[0] == stan]
    kolejnyStan = [item[2] for item in lista]

    # Zmiana stanu na kolejny porównując wartość z sczytanym znakiem.
    for j in range(len(lista)):
        if i in lista[j][1]:
            stan = lista[j][2]

    # Jeśli następny stan nie jest właściwy, zakończ program.
    if stan not in kolejnyStan:
        sys.exit(0)

    # Stan z nazwą nagłówka (J lub K), dodaj literę do zmiennej output.
    # Warunek porównuje do nowych stanów by nie brać znaku gdy jest . , " , >.
    if lista[0][0] in 'JK':
        output += i

    # Jeśli jest stan końcowy to podaj nagłówek.
    if stan == 'P':
        print(output[:-1])
        sys.exit(0)
