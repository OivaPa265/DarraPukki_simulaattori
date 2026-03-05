# Kirjoita funktio / (koodi) joka laskee etäisyyden appropiste1
#ja appropiste 2 välillä, esim. piste 1k - piste 2k = väli/matka on 1k


import random

def appropiste(piste1, piste2):
    if piste1 > piste2:
        erotus = piste2 - piste1
    else:
        erotus = piste2 - piste1
    return erotus

appropiste1 = random.randint(1000,10000)

appropiste2 = random.randint(1000,10000)

print(appropiste1)
print(appropiste2)

matka = appropiste(appropiste1, appropiste2)

print("Erotus on", matka)


