function znaki(typPola = "input"){
    document.getElementById("pole1").innerHTML = "";
    document.getElementById("pole2").innerHTML = "";
    document.getElementById("pole3").innerHTML = "";
    const inputy = document.getElementsByTagName("input");
    for (let i = 0; i<inputy.length; i++){
        const left = inputy[i].getAttribute("maxlength") - inputy[i].value.length;
        const pos = i +1;
        const pole = document.getElementById("pole"+pos);
        pole.innerHTML += "<div>Dla pola "+ pos +" pozostało "+left+" </div>";
        pole.style.color = left === 0 ? "red" : "lightgreen";
    }
}