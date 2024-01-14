from math import pi, sqrt

class Figura:
    def wypisz_informacje(self):
        pass

    def oblicz_obwod(self):
        pass

    def oblicz_pole(self):
        pass

class Kolo(Figura):
    def __init__(self, promien):
        self.promien = promien

    def wypisz_informacje(self):
        print(f"Koło o promieniu: {self.promien}")

    def oblicz_obwod(self):
        return 2 * pi * self.promien

    def oblicz_pole(self):
        return pi * self.promien ** 2

class Prostokat(Figura):
    def __init__(self, bok_a, bok_b):
        self.bok_a = bok_a
        self.bok_b = bok_b

    def wypisz_informacje(self):
        print(f"Prostokąt o bokach: {self.bok_a} i {self.bok_b}")

    def oblicz_obwod(self):
        return 2 * (self.bok_a + self.bok_b)

    def oblicz_pole(self):
        return self.bok_a * self.bok_b

class Kwadrat(Prostokat):
    def __init__(self, bok):
        super().__init__(bok, bok)

    def wypisz_informacje(self):
        print(f"Kwadrat o boku: {self.bok_a}")

class Trojkat(Figura):
    def __init__(self, bok_a, bok_b, bok_c):
        if not self.czy_trojkat_poprawny(bok_a, bok_b, bok_c):
            raise ValueError("Taki trójkąt nie istnieje")
        self.bok_a = bok_a
        self.bok_b = bok_b
        self.bok_c = bok_c

    @staticmethod
    def czy_trojkat_poprawny(a, b, c):
        return a + b > c and a + c > b and b + c > a

    def wypisz_informacje(self):
        print(f"Trójkąt o bokach: {self.bok_a}, {self.bok_b} i {self.bok_c}")

    def oblicz_obwod(self):
        return self.bok_a + self.bok_b + self.bok_c

    def oblicz_pole(self):
        p = self.oblicz_obwod() / 2
        return sqrt(p * (p - self.bok_a) * (p - self.bok_b) * (p - self.bok_c))

def utworz_kolo():
    promien = float(input("Podaj promień koła: "))
    kolo = Kolo(promien)
    kolo.wypisz_informacje()
    print("Obwód:", kolo.oblicz_obwod())
    print("Pole:", kolo.oblicz_pole())
    return kolo

def utworz_prostokat():
    bok_a = float(input("Podaj długość boku a prostokąta: "))
    bok_b = float(input("Podaj długość boku b prostokąta: "))
    prostokat = Prostokat(bok_a, bok_b)
    prostokat.wypisz_informacje()
    print("Obwód:", prostokat.oblicz_obwod())
    print("Pole:", prostokat.oblicz_pole())
    return prostokat

def utworz_kwadrat():
    bok = float(input("Podaj długość boku kwadratu: "))
    kwadrat = Kwadrat(bok)
    kwadrat.wypisz_informacje()
    print("Obwód:", kwadrat.oblicz_obwod())
    print("Pole:", kwadrat.oblicz_pole())
    return kwadrat

def utworz_trojkat():
    while True:
        try:
            bok_a = float(input("Podaj długość boku a trójkąta: "))
            bok_b = float(input("Podaj długość boku b trójkąta: "))
            bok_c = float(input("Podaj długość boku c trójkąta: "))
            trojkat = Trojkat(bok_a, bok_b, bok_c)
            trojkat.wypisz_informacje()
            print("Obwód:", trojkat.oblicz_obwod())
            print("Pole:", trojkat.oblicz_pole())
            return trojkat
        except ValueError as e:
            print(f"Błąd: {e}")
            continue

def main():
    figury = []
    while True:
        print("Wybierz figurę do utworzenia:")
        print("1. Koło")
        print("2. Prostokąt")
        print("3. Kwadrat")
        print("4. Trójkąt")
        print("5. Zakończ")

        wybor = input("Twój wybór: ")

        if wybor == "1":
            figura = utworz_kolo()
        elif wybor == "2":
            figura = utworz_prostokat()
        elif wybor == "3":
            figura = utworz_kwadrat()
        elif wybor == "4":
            figura = utworz_trojkat()
        elif wybor == "5":
            break
        else:
            print("Wybierz liczbe od 1 do 5")
            continue

        figury.append(figura)

    print("\nWszystkie figury:")
    for figura in figury:
        figura.wypisz_informacje()
        print("Obwód:", figura.oblicz_obwod())
        print("Pole:", figura.oblicz_pole())
        print()

if __name__ == "__main__":
    main()
