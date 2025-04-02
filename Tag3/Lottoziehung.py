
# Lottoziehung

"""
Schreibe ein Programm,
das sechs VERSCHIEDENE Lottozahlen (6 aus 49) zieht
und in einer Liste abspeichert.
"""
from random import randint

#1. Step: Liste erzeugen
#2. Step: logik operatoren
#3. Step: Ausgabe


lottozahlen=[]

while len(lottozahlen)<6:
    zahl=randint(1,50)
    if zahl not in lottozahlen:
        lottozahlen.append(zahl)
        lottozahlen.sort()

print(lottozahlen)
