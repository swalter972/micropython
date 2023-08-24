from microbit import *
import log
import power


def echelle(value, in_min, in_max, out_min, out_max):
  valeur = (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
  return int(valeur)
    

@run_every(min=15)
def log_data():
    log.add({
        'humidite': pin0.read_analog(),
        'temperature': temperature(),
        'lumiere': display.read_light_level()
    })    


while True:
    
    
    
    #display.set_pixel(x,y,valeur_lumiere)

    if button_a.is_pressed() and button_b.is_pressed():
        lumiere = echelle(display.read_light_level(), 0, 255, 0, 9)
        print (lumiere)
        display.show(lumiere)
    
    if button_a.is_pressed():
        display.scroll(temperature())

    if button_b.is_pressed():
        
        humid= echelle(pin0.read_analog(),0,800,0,9)
        display.show(humid)

    # To go sleep, wake up when button A is pressed, and ensure the
    # function scheduled with run_every still executes in the background
    power.deep_sleep(wake_on=button_a, run_every=True)
    
