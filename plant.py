"""Premire version"
from microbit import *

def echelle(value, in_min, in_max, out_min, out_max):
  valeur = (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
  return int(valeur)


    
while True:
    valeur_lumiere = int(echelle(display.read_light_level(), 0, 255, 0, 9))
    print (valeur_lumiere)
    display.show(valeur_lumiere)

    sleep(2000)
    display.clear()

