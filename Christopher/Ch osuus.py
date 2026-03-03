# kirjoita miten alkoholi on polttoiane ja sen miten pelin häviää jos vaikka alkoholi loppuu.
# kirjoita myös mitä tapahtuu kun voitat eli keräät kaikki haalarimerkit.

# Alkoholi polttoaine ja miten häviää

def polttoaine_positiivinen():
    # pelaaja liikkuu jotenkin perkele
    return polttoaine_positiivinen

def polttoaine_negatiivinen():
    # pelaaja vittu häviää koska se on paska
    return polttoaine_positiivinen

def polttoaine_liikaa():
    # pelaaja taas vittu häivää koska se on vitun juoppo
    return polttoaine_liikaa

# -- Pääohjelma --

# määritä se vitun alkoholi

while alkoholi > 0:
    polttoaine_positiivinen(alkoholi)
    if alkoholi == 0:
        polttoaine_negatiivinen(alkoholi)
    if alkoholi > 100: # 100 on esimerkki
        polttoaine_liikaa(alkoholi)


# Voittaminen (Jos se ikinä vittu tapahtuu)

def voitto():
    # Kun pelaaja kerää kaikki haalarimerkit se voittaa ja tähän tulee koodi voitto ruudulle
    return voitto

# -- Pääohjelma --

if haalarimerkit == 100: # 100 on esimerkki luku voi muuttua vapaasti
    voitto()