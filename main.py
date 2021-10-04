import eel
import podatki

eel.init('web')

@eel.expose
def funVrniDnevnik():
    return podatki.funVrniVse()

eel.start('index.html')