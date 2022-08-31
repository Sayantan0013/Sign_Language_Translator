const { ipcRenderer } = require("electron");

function howToUse() {
    let myModal = new bootstrap.Modal(document.getElementById('myModal'), {});
    myModal.show();
}

let btnStart = document.getElementById("btnStart");

btnStart.addEventListener("click", () => {
    ipcRenderer.send("openWebcamWindow");
});