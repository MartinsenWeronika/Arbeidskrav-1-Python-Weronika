study_sessions = [
    {
        "topic": "Python basics",
        "duration_minutes": 60,
        "status": "completed"
    },
    {
        "topic": "Functions",
        "duration_minutes": 45,
        "status": "completed"
    },
    {
        "topic": "Git",
        "duration_minutes": 30,
        "status": "planned"
    },
    {
        "topic": "Dictionaries",
        "duration_minutes": 50,
        "status": "planned"
    },
    {
        "topic": "Loops",
        "duration_minutes": 40,
        "status": "completed"
    }
]


def print_session(session):
    print(
        f"Topic: {session['topic']}, "
        f"Duration: {session['duration_minutes']} min, "
        f"Status: {session['status']}"
    )


def register_session():
    while True:
        topic = input("Topic: ").strip()

        if topic == "":
            print("Topic kan ikke være tomt.")
            continue

        break

    while True:
        try:
            duration_minutes = int(input("Duration in minutes: "))

            if duration_minutes <= 0:
                print("Duration må være større enn 0.")
                continue

            break

        except ValueError:
            print("Duration må være et heltall.")

    while True:
        status = input("Status (planned/completed): ").strip().lower()

        if status not in ["planned", "completed"]:
            print("Status må være planned eller completed.")
            continue

        break

    new_session = {
        "topic": topic,
        "duration_minutes": duration_minutes,
        "status": status
    }

    study_sessions.append(new_session)

    print("Studieøkten ble registrert.")


def show_all_sessions():
    for session in study_sessions:
        print_session(session)


def show_completed_sessions():
    completed_sessions = []

    for session in study_sessions:
        if session["status"] == "completed":
            completed_sessions.append(session)

    if len(completed_sessions) == 0:
        print("Ingen fullførte studieøkter.")
        return

    for session in completed_sessions:
        print_session(session)


def search_sessions():
    while True:
        search_word = input("Søk etter tema: ").strip().lower()

        if search_word == "":
            print("Søket kan ikke være tomt.")
            continue

        break

    matches = []

    for session in study_sessions:
        if search_word in session["topic"].lower():
            matches.append(session)

    if len(matches) == 0:
        print("Ingen studieøkter funnet.")
        return

    for session in matches:
        print_session(session)


def get_duration(session):
    return session["duration_minutes"]


def sort_sessions_by_duration():
    sorted_sessions = sorted(
        study_sessions,
        key=get_duration,
        reverse=True
    )

    for session in sorted_sessions:
        print_session(session)


def show_completed_statistics():
    completed_sessions = []

    for session in study_sessions:
        if session["status"] == "completed":
            completed_sessions.append(session)

    if len(completed_sessions) == 0:
        print("Ingen fullførte studieøkter.")
        return

    total_duration = 0

    for session in completed_sessions:
        total_duration += session["duration_minutes"]

    average_duration = total_duration / len(completed_sessions)

    print(f"Samlet varighet: {total_duration} minutter")
    print(f"Gjennomsnittlig varighet: {average_duration:.1f} minutter")


def show_menu():
    while True:
        print("\n--- STUDIEØKTER ---")
        print("1. Registrer studieøkt")
        print("2. Vis alle studieøkter")
        print("3. Vis fullførte studieøkter")
        print("4. Søk etter tema")
        print("5. Sorter etter varighet")
        print("6. Vis statistikk for fullførte økter")
        print("7. Avslutt")

        choice = input("Velg et alternativ (1-7): ")

        if choice == "1":
            register_session()

        elif choice == "2":
            show_all_sessions()

        elif choice == "3":
            show_completed_sessions()

        elif choice == "4":
            search_sessions()

        elif choice == "5":
            sort_sessions_by_duration()

        elif choice == "6":
            show_completed_statistics()

        elif choice == "7":
            print("Programmet avsluttes.")
            break

        else:
            print("Ugyldig valg. Velg et tall fra 1 til 7.")


show_menu()