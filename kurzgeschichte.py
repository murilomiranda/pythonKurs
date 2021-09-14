"""Kurzgeschichte - Geschlecht-Richtung"""

message = "Dieses Programm schreibt eine Kurzgeschichte, in der Sie vorkommen."

print(message)

# Eingabe
geschlecht = input("Was ist Ihr Geschlecht? (weiblich/männlich) ")
name = input("Wie lautet Ihr Vorname? ")
monat = input("In welchem Monat ist Ihr Geburtstag? ")
haarfarbe = input("Ihre Haarfarbe: ")
wohnort = input("Ihr Wohnort: ")


# Ausgabe
if geschlecht == "männlich".lower():
    message = """\nDie Verabredung mit dem Kommissar\nEs war ein grauer Morgen im {0}. Die Sonne war gerade erst aufgegangen und es war noch wenig Betrieb im Stadtzentrum von {1}.\nHauptkommissar Hartmann stand vor dem Bistro und schaute auf die Uhr.\nWo bleibt {2} nur?, dachte er. Ist etwas schief gelaufen?\nVielleicht hatte {2}s Freundin Wind von der Sache bekommen und seine Pläne durchkreuzt.\nEine Person mit struwweligen {3}en Haaren näherte sich mit raschen Schritten.\nDer Kommissar atmete auf, als er den Menschen erkannte. Es war {2}. Jetzt konnte eigentlich nichts mehr passieren."""
elif geschlecht == "weiblich".lower():
    message = """\nDie Verabredung mit dem Kommissar\nEs war ein grauer Morgen im {0}. Die Sonne war gerade erst aufgegangen und es war noch wenig Betrieb im Stadtzentrum von {1}.\nHauptkommissar Hartmann stand vor dem Bistro und schaute auf die Uhr.\nWo bleibt {2} nur?, dachte er. Ist etwas schief gelaufen?\nVielleicht hatte {2}s Freund Wind von der Sache bekommen und ihre Pläne durchkreuzt.\nEine Person mit struwweligen {3}en Haaren näherte sich mit raschen Schritten.\nDer Kommissar atmete auf, als er den Menschen erkannte. Es war {2}. Jetzt konnte eigentlich nichts mehr passieren."""
else:
    message = """\nSorry, ich habe nicht Ihr Geschlecht verstanden."""

print(message.format(monat, wohnort, name, haarfarbe), sep="\n")
