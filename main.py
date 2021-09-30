import eel

eel.init('web')

@eel.expose
def funFunkcija():
    print("sam testiram")

eel.start('index.html')