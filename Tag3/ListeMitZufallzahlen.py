# Liste mit Zufallszahlen initialisieren und auswerten

# Initialisiere eine Liste mit 50 Zufallszahlen
# zwischen 0 (inklusive) und 10 (inklusive).
# Berechne dann die Summe aller Elemente.
# Zähle, wie oft der Wert 0 vorkommt.
# Ermittel, an welcher Position die erste 0 erscheint.
# (Es kann passieren, dass die Zahl gar nicht vorkommt.)
# Formuliere zur Auswertung der Liste eigenen Code mit Schleifen und Bedingungen.
# Vermeide den Einsatz fertiger Listenfunktionen wie count() und index().

from random import randint
zufallzahlen=[]
summe=0
anzahl_null=0
erste_null_index=-1
null_list=[]
while len(zufallzahlen)<50:
    zahl=randint(0,11)
    zufallzahlen.append(zahl)
    #zufallzahlen.sort()
    print(zufallzahlen)
"""

for i in zufallzahlen:
    if i==0:
        print(zufallzahlen.index(0))
    summe +=i"""


for index in range(len(zufallzahlen)):
    wert = zufallzahlen[index]
    summe += wert

    if wert == 0:
        anzahl_null += 1
        null_list.append(wert)
        if erste_null_index == -1:  # erste null
            erste_null_index = index


print("Summe aller Zahlen:", summe)
print("Anzahl der Nullen:", anzahl_null)
print(null_list)
if erste_null_index != -1:
    print("Erste Null an Position:", erste_null_index)
else:
    print("Keine Null vorhanden.")




