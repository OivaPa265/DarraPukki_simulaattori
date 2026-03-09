# Kirjoitan funktio tai koodin, joka laskee etäisyyden appropiste1
#ja appropiste 2 väliltä, esim. piste 1k - piste 2k = väli/matka on 1k


import random

# Tässä Funktio laskee kahden pisteen välisen etäisyyden
def appropiste(piste1, piste2):
    if piste1 > piste2:              # Tarkistaa kumpi pisteistä on suurempi
        erotus = piste1 - piste2     # Laskee pisteiden välinen erotus
    else:
        erotus = piste2 - piste1     # Eli jos piste2 on suurempi niin lasketaan näin
    return erotus   # Palauttaa lasketun etäisyyden


#Arvotaan eka piste väliltä 1000-10000
appropiste1 = random.randint(1000,10000)

#Arvotaan toka piste väliltä 1000-1000
appropiste2 = random.randint(1000,10000)

#Tulostetaan pisteet
print(appropiste1)
print(appropiste2)

# Kutsutaan funktiota ja tallenetaan tulosta muuttujaan, joka on matka.
matka = appropiste(appropiste1, appropiste2)

#Tulostetaan pisteiden  välinen etäisyys
print("Erotus on", matka)


