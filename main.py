import eel
import podatki

eel.init('web')


@eel.expose
def funVrniDnevnik():
    return podatki.funVrniVse()


@eel.expose
def funObstajaDanes():
    return podatki.funObstajaDanes()


@eel.expose
def funDodajDnevnik(datum, vsebina):
    print(datum, vsebina)
    podatki.funDodajDnevnik(datum, vsebina)


eel.start('index.html')
