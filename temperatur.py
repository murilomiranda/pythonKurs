
"""
Folgende Liste enthält einige Temperaturwerte in Celsius-System. 

Schreibe ein Python-Programm, um diese Werte in Fahrenheit zu konvertieren 
und diese dann in einer neuen Liste zu speichern. In der Ausgabe soll dann 
die neue Liste ausgegeben werden. 

Achtung: die erste Liste enthält manche ungültige Werte. Für diese Werte 
soll in die neue Liste einfach den Wert None eingetragen werden. 

Formel: fahrenheit = celsius * 1.8 + 32 
"""

def temperatur(lw = [], *werte):
    newWerte = []

    werte = list(werte)
    werte = lw + werte

    for wert in werte:
        if type(wert) in [int, float]:
            newWerte.append(round(wert * 1.8 + 32, 2))
        else:
            newWerte.append(None)
    
    return newWerte


if __name__ == '__main__':
    print(temperatur([], 25, 15.35, True, 45, 44, None, 'einundzwanzig', ''))
    print(temperatur([], 16, 'Ola', 5.5, False, True, 1986, None, ''))

    celsiusTemperature = [25, 15.35, 16, 'Ola', 5.5, False, 1986]   
    print(temperatur(celsiusTemperature))
    print(temperatur(celsiusTemperature, 25, 15.35, True, None))