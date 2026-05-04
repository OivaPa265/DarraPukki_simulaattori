console.log("Ristinolla peli käynnistyi")

// Pelaaja on X ja botti on O.
let pelaaja = "X"
let peliOhi = false

let aani = new Audio("sounds/ting.mp3")
let voittoAani = new Audio("sounds/gameover.mp3")
let taustaMusiikki = new Audio("sounds/music.mp3")
taustaMusiikki.loop = true
taustaMusiikki.volume = 0.5
let musiikkiAlkanut = false

// Näistä riveistä voi tulla voitto.
let voittorivit = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

// Tällä katsotaan tuliko voitto tai tasapeli.
function tarkistaVoitto() {
    let ruudut = document.getElementsByClassName("boxtext")

    // Lisätään voittoviiva
    let line = document.querySelector(".line")
    for (let i = 0; i < voittorivit.length; i++) {
        let a = voittorivit[i][0]
        let b = voittorivit[i][1]
        let c = voittorivit[i][2]

        if (
            ruudut[a].innerText != "" &&
            ruudut[a].innerText == ruudut[b].innerText &&
            ruudut[b].innerText == ruudut[c].innerText
        ) {
            if (ruudut[a].innerText == "X") {
                document.querySelector(".info").innerText = "Sinä voitit!"
                document.querySelector(".imgbox img").src = "images/win.gif"
            } else {
                document.querySelector(".info").innerText = "Botti voitti!"
                document.querySelector(".imgbox img").src = "images/lose.gif"
            }

            peliOhi = true
            voittoAani.play()
            document.querySelector(".imgbox img").style.width = "350px"

            if (a == 0 && b == 1 && c == 2) {
                line.style.width = "300px"
                line.style.top = "50px"
            }

            if (a == 3 && b == 4 && c == 5) {
                line.style.width = "300px"
                line.style.top = "150px"
            }

            if (a == 6 && b == 7 && c == 8) {
                line.style.width = "300px"
                line.style.top = "250px"
            }
            return
        }
    }

    // jos kaikki ruudut on täynnä tulee tasapeli
    let tasapeli = true

    for (let i = 0; i < ruudut.length; i++) {
        if (ruudut[i].innerText == "") {
            tasapeli = false
        }
    }

    if (tasapeli) {
        document.querySelector(".info").innerText = "Tasapeli!"
        peliOhi = true
    }
}

// Tällä botti etsii hyvän paikan.
function etsiPaikka(merkki) {
    let ruudut = document.getElementsByClassName("boxtext")

    for (let i = 0; i < voittorivit.length; i++) {
        let a = voittorivit[i][0]
        let b = voittorivit[i][1]
        let c = voittorivit[i][2]

        if (ruudut[a].innerText == merkki && ruudut[b].innerText == merkki && ruudut[c].innerText == "") {
            return c
        }

        if (ruudut[a].innerText == merkki && ruudut[b].innerText == "" && ruudut[c].innerText == merkki) {
            return b
        }

        if (ruudut[a].innerText == "" && ruudut[b].innerText == merkki && ruudut[c].innerText == merkki) {
            return a
        }
    }

    return -1
}

// Nyt botti pelaa.
function botinVuoro() {
    let ruudut = document.getElementsByClassName("boxtext")

    if (peliOhi || pelaaja != "O") {
        return
    }

    let valinta = etsiPaikka("O")

    if (valinta == -1) {
        valinta = etsiPaikka("X")
    }

    if (valinta == -1 && ruudut[4].innerText == "") {
        valinta = 4
    }

    if (valinta == -1) {
        for (let i = 0; i < ruudut.length; i++) {
            if (ruudut[i].innerText == "") {
                valinta = i
                break
            }
        }
    }

    ruudut[valinta].innerText = "O"
    aani.play()
    tarkistaVoitto()

    if (!peliOhi) {
        pelaaja = "X"
        document.querySelector(".info").innerText = "Sinun vuoro: X"
    }
}

// tähän otetaan kaikki ruudut
let boxit = document.getElementsByClassName("box")

// Tästä pelaaja painaa ruutua.
Array.from(boxit).forEach(box => {
    let teksti = box.querySelector(".boxtext")

    box.addEventListener("click", () => {
        if (teksti.innerText == "" && !peliOhi && pelaaja == "X") {
            if (!musiikkiAlkanut) {
                taustaMusiikki.play()
                musiikkiAlkanut = true
            }

            teksti.innerText = "X"
            aani.play()
            tarkistaVoitto()

            if (!peliOhi) {
                pelaaja = "O"
                document.querySelector(".info").innerText = "Botti miettii hetken..."
                setTimeout(botinVuoro, 500)
            }
        }
    })
})

// Tästä pelin saa alusta.
document.getElementById("reset").addEventListener("click", () => {
    document.querySelectorAll(".boxtext").forEach(ruutu => {
        ruutu.innerText = ""
    })

    pelaaja = "X"
    peliOhi = false
    document.querySelector(".info").innerText = "Sinun vuoro: X"
    document.querySelector(".imgbox img").style.width = "0px"
    document.querySelector(".imgbox img").src = ""
    document.querySelector(".line").style.width = "0px"
})