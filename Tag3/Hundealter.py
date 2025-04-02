# Hundealter

# Hundeliebhaber stellen sich häufig die Frage,
# wie alt ihr Hund wohl wäre, wenn er kein Hund, sondern ein Mensch wäre.
# Landläufig rechnet man Hundejahre in Menschenjahre um,
# indem man das Alter des Hundes mit 7 multipliziert.
# Je nach Hundegröße und Rasse sieht die Umrechnung jedoch etwas komplizierter aus,
# z.B.:
# - Ein einjähriger Hund entspricht in etwa einem 14-jährigen Menschen.
# - 2 Jahre eines Hundes entsprechen 22 Jahre eines Menschen.
# - Ab dann entspricht ein Hundejahr jeweils 5 Menschenjahren.

# Schreibe ein Programm, das das Alter eines Hundes erfragt und dann nach obiger
# Methode berechnet, welchem Alter in Menschenjahren das entspricht.

hundealter=int(input("Wie alt  ist dein Hund?: "))

if  hundealter <=0:
    menschenjahre=0

elif hundealter==1:
        menschenjahre=14
else:
    menschenjahre=22+(hundealter-2)*5


print(f"Ein {hundealter} Jahre alte Hunde wäre {menschenjahre} Menschenjahre alt!")