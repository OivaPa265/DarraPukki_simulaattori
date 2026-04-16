print("=" * 30)

    try:
        valinta = int(input("Valintasi (numero): ")) - 1
        if 0 <= valinta < len(kaikki_kentat):
            uusi_kentta = kaikki_kentat[valinta]['ident']

            # Jos pelaaja kirjoitaa nykyisen sijaintinsa tämän määränpääksi printaa tämän ja kysyy uudestaan
            if uusi_kentta == current_icao:
                print("Et voi lentää kentälle jossa jo olet")
                continue

            # Lasketaan etäisyys kahden kentän välillä
            old_info = get_airport_info(current_icao)
            new_info = get_airport_info(uusi_kentta)

            lat1, lon1 = old_info[0]['latitude_deg'], old_info[0]['longitude_deg']
            lat2, lon2 = new_info[0]['latitude_deg'], new_info[0]['longitude_deg']

            # Etäisyys metreinä
            distance = int(((lat2-lat1)**2 + (lon2-lon1)**2)**0.5 * 300)

            # Tarkistaa jos pelaajan liikumis pituus on tarpeeksi
            if distance > current_range:
                print(f"Valitsemasi lentokenttä on liian kaukana. Matka kentälle on : {distance}m, maksimi pituus jota vpoit matkustaa on: {current_range}m")
                continue

            # Kun pelaaja liikkuu kenttien välillä vähenetään alkoholin määrää
            alcohol_used = max(200, int(distance / 10))
            new_alcohol = current_alcohol - alcohol_used

            cursor = Yhdiste.cursor(dictionary=True)
            sql = "UPDATE game SET location = %s, alcohol = %s WHERE id = %s"
            cursor.execute(sql, (uusi_kentta, new_alcohol, peli_id))

            print(f"\nLensit {distance}m ja käytit {alcohol_used}ml alkoholia")
            print(f"Sinulla on nyt {new_alcohol}ml alkoholia\n")
        else:
            print("Kirjoitamasi numero/luku ei ole listalla yritälkää uudestaan.")

    # printää tän jos pelaaja kirjoittaa jotain joka ei ole listassa
    except ValueError:
        print("Ooko nää juonu ku ei ossaa luke numeroita listasta")
