print("Tere! Olen sinu uus sõber - Python!")
nimi = input("Sisesta oma nimi: ")
print(nimi + ", oi kui ilus nimi!")
vastus = int(input(nimi + "! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))

try:
    if vastus == 1:
        pikkus = int(input("Sisesta oma pikkus sentimeetrites: "))
        mass = float(input("Sisesta oma kaal kilogrammides: "))
        indeks = mass / (0.01 * pikkus) ** 2

        print(f"{nimi}, Sinu keha indeks on: {indeks:.1f}")

        if indeks < 16:
            print("Vastus: Tervisele ohtlik alakaal")
        elif 16 <= indeks < 19:
            print("Vastus: Alakaal")
        elif 19 <= indeks < 25:
            print("Vastus: Normaalkaal")
        elif 25 <= indeks < 30:
            print("Vastus: Ylekaal")
        elif 30 <= indeks < 35:
            print("Vastus: Rasvumine")
        elif 35 <= indeks < 40:
            print("Vastus: Tugev rasvumine")
        elif indeks >= 40:
            print("Vastus: Tervisele ohtlik rasvumine")
    elif vastus == 0:
        
        print("Kahju! See on väga kasulik info!")
        
    else:
        print("Vale sisend! Palun sisesta 0 või 1.")

except ValueError:
    print("Viga sisestamisel! Palun sisesta õige väärtus.")

finally:
    print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")




