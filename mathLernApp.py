"""
In diesem Projekt möchten wir ein Python-Skript entwickeln, welches einem Schüler /einer Schülerin 
helfen soll, anhand einfacher Aufgaben arithmetische Operationen mit kleinen Aufgaben zu üben. 

Das Programm soll zuerst fragen, wie viele Aufgaben der/die Schüler/in bekommen möchte. 
Für jede richtige Antwort soll einen Punkt vergeben werden und am Ende den Gesamtpunkt anzeigen. 
Der Gesamtpunkt ist am Anfang gleich Null. Der maximale Gesamtpunkt ist gleich Anzahl der Aufgaben. 
Z.B. der maximale Gesamtpunkt für 10 Aufgaben beträgt 10. 

Jede Aufgabe soll durch Zufall erstellt werden. Bei jeder Aufgabe sollen zwei ganze Zahlen durch Zufall 
und zwischen 1 (Bitte keine 0) und 20 (optional) generiert werden und diese dann nochmals durch Zufall 
mit einem der vier Operatoren (+, -, *, /) kombiniert werden. 

Die eingegebene Antwort für jede Aufgabe soll dann geprüft werden. Bei richtigen Antworten einen 
Punkt vergeben. Bei falschen Antworten einen Hinweis zusammen mit der richtigen Antwort. 
Für falsche Antworten ziehen wir keine Punkte ab (keine negativen Punkte vergeben). 

Am Ende soll unser Programm ein Fazit ziehen und in der Ausgabe den Gesamtpunkt anzeigen. 
"""
import random as rd

"""
Auxiliary Functions
"""

def addition(a, b):
    return a + b

def subtraktion(a, b):
    return a - b

def multiplikation(a, b):
    return a * b

def division(a, b):
    return a//b

def operationen():
    a = rd.randint(1, 20)
    b = rd.randint(1, 20)
    op = rd.randint(0, 3)

    if op == 0:
        return([a, op, b, addition(a, b)])
    elif op == 1:
        return([a, op, b, subtraktion(a, b)])
    elif op == 2:
        return([a, op, b, multiplikation(a, b)])
    else:
        return([a, op, b, division(a, b)])

"""
Body code
"""
operationList = [' + ', ' - ', ' * ', ' / ']

active = True
while active:
    gesamtpunkt = 0
    count = 0
    nummerAufgabe = int(input("Wie viele Aufgabe möchtest du haben? "))

    while count < nummerAufgabe:
        aufgabe = operationen()
        textAufgabe = "{})\t{} {} {} = ??? ".format(count + 1, aufgabe[0], operationList[aufgabe[1]], aufgabe[2])
        result = int(input(textAufgabe))

        if result == aufgabe[3]:
            gesamtpunkt += 1
        else:
            print("Die richtige Antwort ist {}.".format(aufgabe[3]))
        
        count += 1
    
    message = "Dein Ergebnis ist: {0:.1f}%".format(gesamtpunkt/nummerAufgabe*100)
    print(message)

    mehrUeben = input("Möchtest du mehr üben? ")
    if mehrUeben.lower() not in ['true', '1', 'yes', 'ja', 'jep', 'sim']:
        active = False
