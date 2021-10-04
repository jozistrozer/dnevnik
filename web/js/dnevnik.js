async function funNaloziDnevnik() {
    var data = await eel.funVrniDnevnik()();

    for (var i = 0; i < data.length; i++) {
        var pnlMainDnevnik = document.getElementById("idDnevnik");

        var varDiv = document.createElement("div");
        varDiv.classList.add("tabList");
        varDiv.id = data[i][0];
        varDiv.setAttribute("onclick", "funOdpriDnevnik(this.id)");

        var varTextNode = document.createElement("p");
        varTextNode.innerHTML = data[i][1];

        varDiv.appendChild(varTextNode);
        pnlMainDnevnik.appendChild(varDiv);
    }
}

async function funOdpriDnevnik(id) {
    var data = await eel.funVrniDnevnik()();
    var vsebina;
    var datum;

    for (var i = 0; i < data.length; i++) {
        if (data[i][0] == id) {
            datum = data[i][1];
            vsebina = data[i][2];
        }
    }
    console.log(vsebina);

    // Modalno okno.
    document.getElementById("idModalOkno").style = "display: block;";
    document.getElementById("idModalDatum").innerHTML = datum;
    document.getElementById("idModalVsebina").innerHTML = vsebina;
}

function funZapriDnevnik() {
    document.getElementById("idModalOkno").style = "display: none;";
}
