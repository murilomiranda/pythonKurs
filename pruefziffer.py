"""
(Eingabe)
ISBN: z1 z2 z3 z4 z5 z6 z7 z8 z9 z10 

(Verarbeitung)
s = 1*z1 + 2*z2 + 3*z3 + 4*z4 + 5*z5 + 6*z6 + 7*z7 + 8*z8 + 9*z9

z10 == s%11?

(Ausgabe)
ISBN ist richtig
oder
ISBN ist falsch
"""

# Eingabe
eingabe = input("Bitte geben Sie die ISBN mit 10 Ziffern ein: ")
#print(eingabe)

if(len(eingabe) == 10):
    summe = 0
    z10 = int(eingabe[9])
    #print(str(z10) + "\n")
    
    # Verarbeitung
    for x in range(0, 9):
        #print("x = {}, eingabe = {}".format(x, eingabe[x]))
        summe += int(eingabe[x]) * (x+1)

    print(5*"\n*")
    #print("Sum: " + str(sume))
    
    # Ausgabe
    if(z10 == summe % 11):
        print("ISBN {} ist richtig".format(eingabe))
    else:
        print("ISBN {} ist falsch".format(eingabe))
else:
    print("ISBN hat keine 10 Ziffern")

