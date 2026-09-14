# Arbeidskrav 1 – Python

Weronika Martinsen


## Hvordan kjøre programmene

Oppgavene kjøres som vanlige Python-filer fra terminalen.

Eksempel:

python oppgave-1.py

python oppgave-2.py


## Oppgave 1 – Grunnleggende programflyt

I oppgave 1 har jeg laget et program med flere mindre oppgaver samlet i en meny.

Programmet kan beregne samlet studietid, analysere tekst og analysere et tallintervall.

Jeg har brukt variabler, input, if-setninger, while-løkker og try/except.

Jeg har også lagt inn validering av input. Hvis brukeren skriver inn en ugyldig verdi, får brukeren en feilmelding og kan prøve på nytt uten at programmet stopper.

Jeg synes while-løkker passet godt i denne oppgaven fordi brukeren skal kunne prøve igjen hvis input er ugyldig.


## Oppgave 2 – Datastrukturer og behandling av data

I oppgave 2 har jeg laget et program for å registrere og behandle studieøkter.

Jeg bruker en liste som heter `study_sessions`. Hver studieøkt i listen er en dictionary med `topic`, `duration_minutes` og `status`.

Jeg valgte en liste fordi programmet skal lagre flere studieøkter, og det er enkelt å gå gjennom dem med en for-løkke.

Jeg bruker en dictionary for hver studieøkt fordi hver økt har flere verdier som hører sammen. Det gjør det enkelt å hente ut for eksempel topic, varighet og status.

Programmet kan registrere nye studieøkter, vise alle økter, vise fullførte økter, søke etter tema, sortere etter varighet og beregne samlet og gjennomsnittlig tid for fullførte økter.

Jeg har også lagt inn validering slik at tema ikke kan være tomt, varighet må være et positivt heltall, og status må være enten `planned` eller `completed`.


## Oppgave 3

...


## Oppgave 4

...


## Oppgave 5

...


## Kjente feil

Ingen kjente feil så langt.


## Refleksjon

I oppgave 1 lærte jeg mer om hvordan while-løkker, if-setninger og try/except fungerer sammen.

I oppgave 2 lærte jeg hvordan en liste kan inneholde dictionaries, og hvordan jeg kan bruke en for-løkke til å gå gjennom studieøktene og hente ut verdier fra hver dictionary.


## KI-bruk

Se egen fil: `KI-dokumentasjon.md`