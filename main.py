import eel
import podatki
import izvoz

eel.init('web')


@eel.expose
def funVrniDnevnik():
    return podatki.funVrniVse()


@eel.expose
def funObstajaDanes():
    return podatki.funObstajaDanes()


@eel.expose
def funDodajDnevnik(datum, vsebina):
    podatki.funDodajDnevnik(datum, vsebina)

@eel.expose
def funIzvoziDnevnik(ime):
    izvoz.funUstvariHTML(ime)


eel.start('index.html')
