from microbit import *
import log

def echelle(value, in_min, in_max, out_min, out_max):
  valeur = (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
  return int(valeur)
    

@run_every(s=15)
def log_data():
    log.add({
        'humidité': pin0.read_analog(),
        'temperature': temperature(),
        'lumiere': display.read_light_level()
    })    


while True:
    
    
    
    #display.set_pixel(x,y,valeur_lumiere)
    
    if button_a.is_pressed():
        display.scroll(temperature())

    if button_b.is_pressed():
        
        humid= echelle(pin0.read_analog(),0,480,0,9)
        display.show(humid)
    
    if button_a.is_pressed() and button_b.is_pressed():
        lumiere = echelle(display.read_light_level(), 0, 255, 0, 9)
        print (lumiere)
        display.show(lumiere)


