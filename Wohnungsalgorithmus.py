
raumZaehler = 0
wohnungsGroeße = 0
quadratImRaumZaehler= 0
raumAnzahl = int(input("Wie viele Räume sind es? "))
raumNamenListe = []
raumGroeßenListe = []
raumGroeße = 0

while raumZaehler < raumAnzahl:
    print("---------------")
    raumName = input("Wie ist der Raumname? ")
    raumNamenListe.append(raumName)
    anzahlQuadrate = int(input("Zimmer " + str(raumZaehler+1) +  ": Wie viele Quadrate sind im Raum? "))
    raumGroeße = 0
    while quadratImRaumZaehler < anzahlQuadrate:
        print("---------------")
        print("Zimmer " + str(raumZaehler+1) + " - Quadrat " + str(quadratImRaumZaehler+1))
        laenge = int(input("Geben sie die Raumlänge ein "))
        breite = int(input("Geben sie die Breite ein "))
        raumGroeße += laenge * breite
        quadratImRaumZaehler += 1
    wohnungsGroeße += raumGroeße
    raumGroeßenListe.append(raumGroeße)
    quadratImRaumZaehler = 0
    raumZaehler += 1
durchschnittsRaumgroeße = wohnungsGroeße / raumAnzahl
print("\n---------------\n")
raumPrintZaehler = 0
while raumPrintZaehler < raumAnzahl:
    print(str(raumNamenListe[raumPrintZaehler]) + ": " + str(raumGroeßenListe[raumPrintZaehler]) + "qm")
    raumPrintZaehler += 1
print("Wohnungsgröße: " + str(wohnungsGroeße) + "qm - Durchschnittliche Zimmergröße: " + str(durchschnittsRaumgroeße) + "qm")
