def play_noppa():
    import random

    #noppa luvut
    noppa_N = 0
    noppa_H = 0
    Huomasi = 0

    # miten pukki heittää
    Valmis = input("Miten heität noppaasi\n"
                   " 1 = Reilusti Sääntöjä noudattaen\n"
                   " 2 = Huijaamalla heitä painotettu noppa (1/3 mahdollisuus että vastustaja huomaa)\n"
                   "Valintasi: ")

    #noppien heitot
    if Valmis == "1":
        noppa_N = random.randint(1, 6)
    elif Valmis == "2":
        noppa_H = random.randint(3, 6)
        Huomasi = random.randint(1, 3)

    Mikko = random.randint(1, 6)

    # Jos pukki on kiltisti eikä huijaa
    if Valmis == "1":
        if noppa_N > Mikko:
            print(f"Sait {noppa_N} ja Mikko sai {Mikko}. Voitit!")
            return True
        elif noppa_N < Mikko:
            print(f"Sait {noppa_N} ja Mikko sai {Mikko}. Hävisit.")
            return False
        else:
            print(f"Molemmat saivat {noppa_N}. Tasapeli.")
            return False

    # jos pukki ei ole kilitisi ja huijaa
    elif Valmis == "2":
        if Huomasi == 3:
            print(f"Sait {noppa_H}, mutta Mikko huomasi että huijasit! Hävisit pelin.")
            return False
        elif noppa_H > Mikko:
            print(f"Sait {noppa_H} ja Mikko sai {Mikko} eikä Mikko huomannut. Voitit!")
            return True
        elif noppa_H < Mikko:
            print(f"Sait {noppa_H} ja Mikko sai {Mikko}. Hävisit.")
            return False
        else:
            print(f"Molemmat saivat {noppa_H}. Tasapeli.")
            return False
