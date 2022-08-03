#Zufallszahlen Bibliothek
import random

#variablen

zahl1=0
zahl2=0
zahl3=0
zahl1i=0
zahl2i=0
zahl3i=0
#Zufallszahlen erzeugen

zahl1=random.randint(1,45)
zahl2=random.randint(1,45)
zahl3=random.randint(1,45)



#input funktionen

zahl1i=int(input("Gib bitte deine 1 Zahl ein:"))
zahl2i=int(input("Gib bitte deine 2 Zahl ein:"))
zahl3i=int(input("Gib bitte deine 3 Zahl ein:"))


#Lösung

print(zahl1)
print(zahl2)
print(zahl3)

#Überprüfung

if zahl1==zahl1i:
    if zahl2==zahl2i:
        if zahl3==zahl3i:
            print("Du hast gewonnen")
        else:
            print("Du hast verloren")

    else:
        print('du hast verloren')

else:
    print("Du hast verloren")





