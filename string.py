"""
Entwickle ein Programm für einen imaginären E-Mail-Service-Anbieter, 
welches den Vornamen und Namen in die Eingabe bekommt und in der Ausgabe 
eine E-Mail-Adresse wie max.mustermann@company.com ausgibt. 
"""
import random as rd

def aufgabe1():
    emailServer = ['max.mustermann@company.com']

    vorname = input("Vorname(n): ")
    name = input("Name(n): ")

    email = str(vorname.lower().strip() + "." + name.lower().strip() + "@company.com").replace(" ", "")

    ### Verify if E-Mail Server has the email with those name and vorname
    #### If so, a random number is generated and included at the end of user name
    if email in emailServer:
        nummer = rd.randint(1, 100)
        email = str(vorname.lower().strip() + "." + name.lower().strip() + str(nummer) + "@company.com").replace(" ", "")

    emailAnswer = input(f"Vielleicht möchten Sie diese {email} haben? (ja/nein): ")

    ### If the user likes the suggested e-mail, it's added to email Server
    #### If no, the user can suggest a new email
    if emailAnswer not in ['ja', 'yes', 'j']:
        emailAnswer = True
        while emailAnswer:
            email = input(f"Geben Sie eine E-Mail ein: ")

            if "@" not in email:
                email += "@company.com"

            if email not in emailServer:
                emailAnswer = False
            else:
                print(f"Sorry, diese E-Mail gehört bereits einem anderen Benutzer.", end=" ")

    emailServer.append(email)
    print(f"Willkommen, {vorname.title()} {name.title()}! Ihre E-Mail ist {email}")


#aufgabe1()

"""
Aufgabe (2) Trump Tweetz (Niveau: mittel) 

Folgende Listen sind gegeben. Entwickle ein Python Programm, 
welches aus jeder Liste in der gegebenen Reihenfolge durch 
Zufall ein Wort auswählt und aus allen Wörtern ein Trump-Tweet bildet. 
"""
def aufgabe2():
    part1 = ["Putin", "Hillary", "Obama", "Fake News", "Mexico", "Arnold Schwarzenegger", "Democrats"] 
    part2 = ["no talent", "on the way down", "really poor numbers", "nasty tone", "looking like a fool", "bad hombre"] 
    part3 = ["got destroyed by my ratings.", "rigged the election.", "had a much smaller crowd.", "will pay for the wall.", "", ""] 
    part4 = ["So sad", "Apologize", "So true", "Media won't report", "Big trouble", "Fantastic job", "Stay tuned"] 

    print(f"{rd.choice(part1)} {rd.choice(part2)} {rd.choice(part3)} {rd.choice(part4)}")
    print(f"{rd.choice(part1)} {rd.choice(part2)} {rd.choice(part3)} {rd.choice(part4)}")
    print(f"{rd.choice(part1)} {rd.choice(part2)} {rd.choice(part3)} {rd.choice(part4)}")
    print(f"{rd.choice(part1)} {rd.choice(part2)} {rd.choice(part3)} {rd.choice(part4)}")

#aufgabe2()
"""
Aufgabe (3) Polnische Taschenrechner (Niveau: fortgeschritten)
Polnische Notation (PN), auch Normale Polnische Notation (NPN) 
genannt, ist (in der Informatik und mathematischen Logik) eine 
klammerfreie Schreibweise für Formeln bzw. allgemein für Ausdrücke, 
bei der der Operator vor seinen Operanden geschrieben wird.  

Früher hat man dieser Regel entsprechend, Taschenrechner gebaut, die 
keine '=' Taste hatten (siehe Bild). 

Beispielsweise, wenn man mit zwei Zahlen 3 und 4 eine Addition 
durchführen möchte, notiert man diese Operation wie Folgendes: 
+ 3 4 
Dann drückt man die Enter-Taste und bekommt in der Ausgabe das Ergebnis. 

Schreibe ein Programm, welches die Funktionalität eines polnischen 
Taschenrechners simuliert. Zwischen Eingaben muss ein Leerzeichen 
eingetragen werden und der Taschenrechner soll alle 4 Operationen 
unterstützen. Division mit 2 Stellen nach dem Komma unterstützen. 
"""
import re

def aufgabe3():
    while True:
        calc = input("Operator Zahl Zahl (z.B. + 3 4): ").lower().split()
        # Only string with 3 elements
        if len(calc) == 3:
            # Verify Operator
            # tuple ('+', '-', '*', '/') instead of list ['+', '-', '*', '/']
            if calc[0] in ['+', '-', '*', '/']:
                # Verify if the two strings only content numbers
                # calc[1].isdecimal() can be used instead of re.search('^[0-9.]+$', calc[1]) 
                if re.search('^[0-9.]+$', calc[1]) and re.search('^[0-9.]+$', calc[2]):
                    try:
                        ergebnis = eval(calc[1] + calc[0] + calc[2])
                        if calc[0] == '/':
                            ergebnis = round(ergebnis, 2)
                        
                        print(f"Ergebnis: {ergebnis}")
                    except ZeroDivisionError:
                        print("Ich kann nicht Division mit Null machen.")
                else:
                    print("Problem in Nummern gefunden.")
            else:
                print("Problem Operator nicht gefunden. Bitte benutzen Sie nur +, -, * oder /.")
        elif calc in [[], ['fertig'], ['done']]:
            break
        else:
            print("Ich habe nicht verstaden.\nWenn Sie fertig ist, geben Sie 'fertig' oder 'done' oder nur ein Enter ein")

aufgabe3()