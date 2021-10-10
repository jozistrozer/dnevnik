# Generiranje statične HTML strani + pdf

import os
from podatki import funVrniVse


def funUstvariDir(varImeDatoteke):
    varDirectory = os.path.dirname(os.path.realpath(__file__)) + "/izvoz"

    # Iz JS funkcije pridobimo ime datoteke.
    varNazivIzvoza = varDirectory + "/" + varImeDatoteke

    # Kreairanje direktorija za html strani.
    os.mkdir(varNazivIzvoza, 0o755)

    return varNazivIzvoza


def funUstvariHTML(varImeDatoteke):
    varPot = funUstvariDir(varImeDatoteke)

    dnevnik = funVrniVse()

    # index stran za navigiranje dnevnikov.
    index = open(varPot + '/index.html', 'w')
    indxDnevnik = "<html>" \
                  "<head><title>IME DNEVNIKA</title></head>" \
                  "<body><ul>"

    indxVsebina = "<html>" \
                  "<head><title>$$TITLE_DNEVNIK$$</title></head>" \
                  "<body>"

    for stran in dnevnik:
        indxDnevnik += "<li><a href='" + stran[0] + ".html'>" + stran[1] + "</a></li>"

        # Kreiranje samostojne html datoteke z vsebino za vsako 'stran'
        varTmp = open(varPot + '/' + stran[0] + '.html', 'w')
        indxVsebina.replace("$$TITLE_DNEVNIK$$", stran[1])

        indxVsebina += "<h1>" + stran[1] + "</h1>"
        indxVsebina += "<p>" + stran[2] + "</p>"

        indxVsebina += "</body></html>"

        varTmp.write(indxVsebina)
        varTmp.close()
        indxVsebina = "<html>" \
                      "<head><title>$$TITLE_DNEVNIK$$</title></head>" \
                      "<body>"

    indxDnevnik += "</ul></body></html>"

    index.write(indxDnevnik)
    index.close()