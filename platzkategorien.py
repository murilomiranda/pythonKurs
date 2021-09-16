plazkategorien = {
    'loge': 50,
    'parkett' : 39,
    'vorparkett' : 29,
    'rang' : 19
}

eingabe = input("\nWelche Kategorie möchten Sie sehen? ")
preis = plazkategorien[eingabe.lower()]

personen = int(input("Wie viele Personen gibt es? (min. 1 - max. 25) "))

if personen > 0 and personen <=25:
    if personen >= 3 and personen <= 10:
        total = personen * preis * 0.8 # 20% Rabatt
    elif personen > 10 and personen <= 25:
        total = personen * preis * 0.7 # 30% Rabatt
    
    print("\nJeder Person muss {0:.2f} zahlen.\n".format(total/personen))
else:
    print("\nDie Anzahl der Personen wurde nicht erkannt. Bitte Geben Sie eine Zahl zwischen 1 und 25 ein.\n")
