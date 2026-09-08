def calculate_study_time():
    while True:
        try:
            study_sessions = int(input("Antall studieøkter: "))

            if study_sessions <= 0:
                print("Antall studieøkter må være større enn 0.")
                continue

            break

        except ValueError:
            print("Ugyldig input. Du må skrive inn et heltall.")

    while True:
        try:
            minutes_per_session = int(input("Minutter per økt: "))

            if minutes_per_session <= 0:
                print("Antall minutter må være større enn 0.")
                continue

            break

        except ValueError:
            print("Du må skrive inn et positivt heltall.")

    total_minutes = study_sessions * minutes_per_session

    hours = total_minutes // 60
    minutes = total_minutes % 60

    print(f"Samlet tidsbruk: {hours} timer og {minutes} minutter")


calculate_study_time()







