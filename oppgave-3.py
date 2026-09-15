from datetime import datetime, timedelta


DATE_FORMAT = "%d.%m.%Y"
TIME_FORMAT = "%H:%M"


def parse_date(date_text):
    date_value = datetime.strptime(date_text, DATE_FORMAT).date()

    if date_value.strftime(DATE_FORMAT) != date_text:
        raise ValueError

    return date_value


def calculate_end_time(start_time, duration_minutes):
    return start_time + timedelta(minutes=duration_minutes)


def days_between(first_date, second_date):
    return abs((second_date - first_date).days)


def sort_dates(dates):
    return sorted(dates)


def get_valid_date(prompt):
    while True:
        date_text = input(prompt).strip()

        try:
            return parse_date(date_text)

        except ValueError:
            print(
                "Ugyldig dato. Bruk formatet dd.mm.åååå, "
                "for eksempel 14.09.2026."
            )


def get_valid_start_time():
    while True:
        time_text = input("Starttid (HH:MM): ").strip()

        try:
            start_time = datetime.strptime(time_text, TIME_FORMAT)

            if start_time.strftime(TIME_FORMAT) != time_text:
                raise ValueError

            return start_time

        except ValueError:
            print(
                "Ugyldig starttid. Bruk formatet HH:MM, "
                "for eksempel 09:30."
            )


def get_positive_duration():
    while True:
        try:
            duration_minutes = int(
                input("Varighet i minutter: ").strip()
            )

            if duration_minutes <= 0:
                print("Varigheten må være et positivt heltall.")
                continue

            return duration_minutes

        except ValueError:
            print("Varigheten må være et positivt heltall.")


def main():
    print("=== Studieplanlegger ===")

    study_dates = []

    print("\nRegistrer tre studiedatoer:")

    for number in range(1, 4):
        study_date = get_valid_date(
            f"Dato {number} (dd.mm.åååå): "
        )

        study_dates.append(study_date)

    print("\nRegistrer en studieøkt:")

    start_time = get_valid_start_time()
    duration_minutes = get_positive_duration()

    end_time = calculate_end_time(
        start_time,
        duration_minutes
    )

    difference = days_between(
        study_dates[0],
        study_dates[1]
    )

    sorted_dates = sort_dates(study_dates)

    print("\n=== Resultat ===")

    print(
        f"Starttid: {start_time.strftime(TIME_FORMAT)}"
    )

    print(
        f"Varighet: {duration_minutes} minutter"
    )

    print(
        f"Sluttid: {end_time.strftime(TIME_FORMAT)}"
    )

    print(
        f"Antall dager mellom de to første datoene: "
        f"{difference}"
    )

    print("\nDatoer sortert kronologisk:")

    for study_date in sorted_dates:
        print(study_date.strftime(DATE_FORMAT))


main()