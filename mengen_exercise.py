# Gegeben ist die Menge "obst"

obst = {'apfel', 'orange'}

# Jemand hat aus Versehen die Methode "update()"
# wie Folgendes angewendet, um eine "banane" in die Menge einzutragen

obst.update('banane')

# Dadurch werden die Buchstaben 'b', 'a' und 'n' als drei Elemente eingetragen
# Schreibe ein Programm, um diese drei aus der Menge zu entfernen und dann die 'banane'
# als ein einziges Objekt in die Menge einzutragen.

print(obst)
new = []
obst.add('banane')
for i in obst:
    if len(i) <= 1:
        new.append(i)

# print(new)
print(obst - set(new))

#obst.difference_update({'b', 'a', 'n', 'e'})
# print(obst)

# obst.update(['banane'])
# print(obst)