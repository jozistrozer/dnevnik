import pickle
from datetime import datetime


def funDodajDnevnik(datum, vsebina):
    varDnevnik = None
    # Branje obstoječega dnevnika.
    try:
        with open('data.pickle', 'rb') as f:
            varDnevnik = pickle.load(f)
    except Exception as ex:
        print(ex)

    # Dodajanje novega dnevnika v polje.
    varDnevnik.append([datum.replace(".", "").replace(" ", ""), datum, vsebina])

    # Zapisovanje novega dnevnika.
    try:
        with open('data.pickle', 'wb') as f:
            pickle.dump(varDnevnik, f, protocol=pickle.HIGHEST_PROTOCOL)
        f.close()
    except Exception as ex:
        print("Error: ", ex)


def funVrniVse():
    try:
        with open('data.pickle', 'rb') as f:
            output = pickle.load(f)
            return output
    except Exception as ex:
        print("Error: ", ex)


def funObstajaDanes():
    dnevniki = funVrniVse()
    varObstaja = False

    varDate = datetime.now()
    varDanasnjiDatum = ("%d.%d.%d"%(varDate.day, varDate.month, varDate.year)).replace(".", "")

    for dnevnik in dnevniki:
        if dnevnik[0] == varDanasnjiDatum:
            varObstaja = True

    return varObstaja