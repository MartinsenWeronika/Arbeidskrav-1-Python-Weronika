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


# calculate_study_time()


def analyze_text():
    while True:
        user_input = input("Tast inn en tekst: ")

        if user_input.strip() == "":
            print("Teksten kan ikke være tom. Prøv igjen.")
            continue

        break

    characters_with_spaces = len(user_input)

    text_without_spaces = user_input.replace(" ", "")
    characters_without_spaces = len(text_without_spaces)

    lowercase_text = user_input.lower()
    reversed_text = user_input[::-1]

    contains_python = "python" in lowercase_text

    print(f"Antall tegn med mellomrom: {characters_with_spaces}")
    print(f"Antall tegn uten mellomrom: {characters_without_spaces}")
    print(f"Tekst med små bokstaver: {lowercase_text}")
    print(f"Tekst baklengs: {reversed_text}")

    if contains_python:
        print("Teksten inneholder ordet 'python'.")
    else:
        print("Teksten inneholder ikke ordet 'python'.")


# analyze_text()



def analyze_number_range():
    while True:
        try:
            start_value = int(input("Startverdi: "))
            end_value = int(input("Sluttverdi: "))

            if start_value > end_value:
                print("Startverdien kan ikke være større enn sluttverdien.")
                continue

            break

        except ValueError:
            print("Ugyldig input. Du må skrive inn heltall.")

    even_numbers = []
    divisible_by_three = []
    total_sum = 0

    for number in range(start_value, end_value + 1):
        if number % 2 == 0:
            even_numbers.append(number)

        if number % 3 == 0:
            divisible_by_three.append(number)

        total_sum += number

    print(f"Partall i intervallet: {even_numbers}")
    print(f"Tall som er delelige med 3: {divisible_by_three}")
    print(f"Summen av alle tallene i intervallet: {total_sum}")


# analyze_number_range()


def show_menu():
    while True:
        print("\n--- MENY ---")
        print("1. Beregn tidsbruk")
        print("2. Analyser tekst")
        print("3. Analyser tallintervall")
        print("4. Avslutt")

        choice = input("Velg et alternativ (1-4): ")

        if choice == "1":
            calculate_study_time()

        elif choice == "2":
            analyze_text()

        elif choice == "3":
            analyze_number_range()

        elif choice == "4":
            print("Programmet avsluttes.")
            break

        else:
            print("Ugyldig valg. Velg 1, 2, 3 eller 4.")


show_menu()












