$(document).ready(function(){
    // Povezave v footerju.
    $("#lnkDodaj").click(function(){
        location.href = "index.html";
    });

    $("#lnkDnevnik").click(function(){
        location.href = "dnevnik.html";
    });

    $("#lnkIzvoz").click(function(){
        location.href = "izvozDnevnika.html";
    });

    $("#lnkMe").click(function(){
        window.open('https://github.com/jozistrozer', '_blank');
    });
});

async function funKontrolaDatuma() {
    var varObstajaDanes = await eel.funObstajaDanes()();
    if (varObstajaDanes == true) {
        document.getElementById("idDodajDnevnik").style = "display: none";
        document.getElementById("idObstaja").style = "display: block;";
    }
}

function funOdpriDnevnik() {
    location.href = "dnevnik.html";
}

function funDodajDnevnik() {
    var datum = (document.getElementById("idDanasnjiDatum").textContent).replace(/\s/g, '');
    var vsebina = document.getElementById("txtareaDnevnik").value;

    eel.funDodajDnevnik(datum, vsebina);

    location.reload();
}