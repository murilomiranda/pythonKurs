"""
Mögliche Datenstrukturen und Techniken: Dictionary und Iteration bzw. Verzweigungen 

Fußball WM 2010 

Für diese Aufgabe haben wir die Spielergebnisse von WM 2010 gruppenweise in einem Dictionary 
gespeichert. (Die Zahlen entsprechen eventuell NICHT der wahren Ergebnisse.) Für jede Gruppe 
haben wir ein Dictionary angelegt. (Siehe aufgabe_wm_2010.py) 

Schreibe ein Python-Programm, welches die Namen der Mannschaften aus jeder Gruppe mit dem 
Höchstpunkt (highest score) vermittelt. Es kann sein, dass in einer Gruppe mehrere Mannschaften 
einen Höchstpunkt haben. Dabei muss das Programm die beiden berücksichtigen. 

Schreibe ein Programm, welches die Mannschaft(en) mit dem Höchstpunkt aller Gruppen vermittelt. 

Schreibe ein Programm, welches in Eingabe den Namen einer Mannschaft einliest und in die Ausgabe, 
die zugeordnete Gruppe dieser Mannschaft und ihren Punkt vermittelt. 
"""

# aufgabe_wm_2010.py

# WM 2010 Spielergebnisse gruppenweise (fiktiv)
group_a = {'uruguay': 7, 'mexico': 3, 'south africa': 3, 'france': 1}
group_b = {'argentina': 9, 'south korea': 3, 'greece': 3, 'nigeria': 1}
group_c = {'usa': 5, 'england': 5, 'slovenia': 4, 'algeria': 1}
group_d = {'germany': 6, 'ghana': 4, 'australia': 4, 'serbia': 3}
group_e = {'netherlands': 9, 'japan': 6, 'denmark': 3, 'cameroon': 0}
group_f = {'paraguay': 5, 'slovakia': 4, 'new zealand': 3, 'italy': 2}
group_g = {'brazil': 7, 'portugal': 5, 'ivory coast': 4, 'north korea': 0}
group_h = {'spain': 6, 'chile': 6, 'switzerland': 4, 'honduras': 1}

group = {'a': group_a, 'b': group_b, 'c': group_c, 'd': group_d, 'e': group_e, 'f': group_f, 'g': group_g, 'h': group_h}

message = """--------------------------------------------------------------
                Highest Score pro Gruppe
--------------------------------------------------------------\n""".upper()
print(message)

for i, listLaender in group.items():
    points = max(listLaender.values())
    indices = [i for i, j in enumerate(listLaender.values()) if j == points]
    laender = ""

    for index in indices:
        laender += ((list(listLaender.keys())[index]).title() + " ")

    print("Group {} with {} points: {}".format(i.upper(), points, laender)) 
    print("")


message = """--------------------------------------------------------------
                Highest Score
--------------------------------------------------------------\n""".upper()
print(message)

points = []
laender = []
for i, listLaender in group.items():
    points += listLaender.values()
    laender += listLaender.keys()

maxPoint = max(points)
indices = [i for i, j in enumerate(points) if j == maxPoint]
print("Mannschaft(en) mit dem Höchstpunkt:")
for i in indices:
    print(laender[i].title())
print("")


message = """--------------------------------------------------------------
               Gruppe und Punkt
--------------------------------------------------------------\n""".upper()
print(message)

myLand = input("Geben Sie bitte ein Land ein: ").lower()

for i, listLaender in group.items():
    if myLand in listLaender.keys():
        break
print("{} is im Gruppe {} mit {} Punkt".format(myLand.title(), i.upper(), group[i][myLand]))
