function funIzvoz() {
    var varKontrola = false;
    var nazivDatoteke = document.getElementById("txtImeDatoteke").value;

    // Preverjanje dolžine naziva datoteke.
    if (nazivDatoteke.length < 3) {
        varKontrola = true;
    }

    // TODO: Implementiraj kontrolo za preverjanje, če dnenvik s tem imenom že obstaja.

    if (varKontrola == false) {
        eel.funIzvoziDnevnik(nazivDatoteke);
    } else {
        document.getElementById("txtError").innerHTML = "Ime datoteke je prekratko.";
        document.getElementById("txtError").style = "display: block;";
    }
}