"""
Schreibe ein Programm, welches in der Eingabe einen String einliest 
und jeden Buchstaben samt seiner Frequenz im String als Schlüsselwertpaar 
in einem Dictionary speichert. 

Dabei wollen wir nur Buchstaben - keine Ziffer und keine Sonderzeichen 
berücksichtigen. 

Und Klein- und Großbuchstaben gleichbehandeln. 

"Murilo 2021 !%&" <- String
{'m': 25, 'hello': ''world'}


>>> Enter String: 

    'Hello hell 100!' 

>>> {'h':2, 'e':2, 'l':4, 'o':1} 
"""

stringInput = 'Hello hell 100!'
#buchset = set(stringInput.lower())

leerDict = {}
for char in stringInput:
    if char.isalpha():
        if char in leerDict:
            leerDict[char] = leerDict[char] + 1 # stringOutput[char] +=1
        else:
            leerDict.setdefault(char, 1)
    
    print(leerDict)