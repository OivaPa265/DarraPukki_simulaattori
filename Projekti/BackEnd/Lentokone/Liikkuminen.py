# kattoo jos kentässä on jotain
    goal = Kentan_tehtava(peli_id, current_icao)
    if goal:
        print(f"\nSaavutua kentälle löysit:  {goal['name']}")
        print(f" {goal['money']}ml alkoholia")
        vastaus = input("Haluatko sen? Kyllä/ei: ").upper()

        if vastaus == "KYLLÄ":
            # Lisää tehtävän listaan ja päivitää merkit ja alkoholin määrän
            current_alcohol += goal['money']
            currentgoal += 1

            cursor = Yhdiste.cursor(dictionary=True)
            sql = "UPDATE game SET alcohol = %s WHERE id = %s"
            cursor.execute(sql, (current_alcohol, peli_id))

            print("=" * 30)
            print(f"Otit merkin : {currentgoal}/{numofgoals}")
            print(f"Sinulla on nyt {current_alcohol}ml alkoholia")
            print("=" * 30)

            # Kysyy pelaajalta haluaako pelata minipelia
            minigame_choice = input("Valitse minipeli: 1 Noppa, 2 Blackjack: taikka entter jos et halua pelata")
            print("=" * 30)
            if minigame_choice == "1":
                voitit = miniPelit.Noppa.play_noppa()
                if voitit:
                    currentgoal += 1
                    print("Voitit minipelin! Sait lisämerkin.")
                    print("=" * 30)

            elif minigame_choice == "2":
                voitit = miniPelit.BlackJack.play_blackjack()
                if voitit:
                    currentgoal += 1
                    print("Voitit minipelin! Sait lisämerkin.")
                    print("=" * 30)

            else:
                print("Virheellinen valinta, ei pelata minipeliä.")

            if currentgoal >= numofgoals:
                voitto = True
                hävijö = False
                print("=" * 30)
                print(f"Sinulla on {currentgoal} merkkiä!")
                print("=" * 30)
                break