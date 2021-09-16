"""
Das Programm soll die Menge des Getränkes, sein Alkohols Volumen in % und das Geschlecht sowie 
das Gewicht (in Kg) in die Eingabe einlesen und am Ende den Blutalkoholspiegel berechnen und ausgeben. 
Bei einem Wert über 0,5 Promille soll dann das Programm dazu eine Warnung (als Text-Message) ausgeben. 

Dazu verwenden wir die Formel von Erik Widmark: c = a / (m*r) 

c: Alkohol-Konzentration im Blut 
m: Körpermaße in Kilogramm 
r: ändert sich nach Geschlecht. Für männliche Personen gleich 0.7 und für weibliche Personen 0.6 
a: Menge des konsumierten Alkohols. Diese berechnet man mit Hilfe der folgenden Formel: 

a = v * e * p 

v: die Menge des Getränkes in ml 
e: Alkohol-Volumen in Prozent (z. B. 4% für Bier) 
p: 0.8 g/ml (Alkohols Dichte) – ist ein fester Wert. 
"""

konzentration = 0.0
koepermasse = float(input("Köpermaße (Kg): "))
geschlecht = input("Geschlecht (m/M oder f/F): ")
menge = float(input("Menge des Getränkes (ml): "))
alkoholVolumen = float(input("Alkohol-Volumen (%): "))

konsumiertAlkohol = menge * alkoholVolumen *0.01 * 0.8

if geschlecht.lower() == "f":
    geschlecht = 0.6
elif geschlecht.lower() == "m":
    geschlecht = 0.7
else: 
    print("\nGeschlecht ist falsch! Bitte führen Sie das Programm aus.\n")
    quit()

konzentration = konsumiertAlkohol/(koepermasse * geschlecht)

if konzentration > 0.5:
    print("\nAlkohol-Konzentration im Blut ist zu hoch ({0:.2f})".format(konzentration))
else:
    print("\nCongratulations! You passed the test. ^^")