# Napisz klasę FiguraGeometryczna, która będzie zawierała
# metody:
# policz_pole()
# policz_obwód()

# Napisz klasy Prostokąt, Kwadrat, Koło i Trojkat
# oraz zaimplementuj metody z interfejsu FiguraGeometryczna

# Stwórz instancje tych klas i sprawdź ich działanie

class FiguraGeometryczna:
    def policz_pole(self):
        pass
    def policz_obwod(self):
        pass

class Prostokat(FiguraGeometryczna):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def policz_pole(self):
        pole = self.a * self.b
        print(f"Pole prostokąta wynosi {pole}")

    def policz_obwod(self):
        obwod = 2 * self.a + 2 * self.b
        print(f"Obwód prostokąata wynosi {obwod}")

class Kwadrat(Prostokat):
    def __init__(self, a, b):
        super().__init__(a, b)
    def policz_pole(self):
        pole = self.a ** 2
        print(f"Pole kwadratu wynosi {pole}")

    def policz_obwod(self):
        obwod = 4 * self.a
        print(f"Obwód kwadratu wynosi {obwod}")

class Trojkat(FiguraGeometryczna):
    def __init__(self, a, b, c, h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h
    def policz_pole(self):
        pole = (0.5 * self.a) * self.h
        print(f"Pole trójkąta wynosi {pole}")

    def policz_obwod(self):
        obwod = self.a + self.b + self.c
        print(f"Obwód trójkąta wynosi {obwod}")

class Kolo(FiguraGeometryczna):
    def __init__(self, r):
        self.r = r
    def policz_pole(self):
        pole = 3.14 * self.r ** 2
        print(f"Pole koła wynosi {pole}")

    def policz_obwod(self):
        obwod = 2 * 3.14 * self.r
        print(f"Obwód koła wynosi {obwod}")


prostakat = Prostokat(2,5)
prostakat.policz_pole()
prostakat.policz_obwod()

kwadrat = Kwadrat(5,5)
kwadrat.policz_pole()
kwadrat.policz_obwod()

trojkat = Trojkat(3,5,6,7)
trojkat.policz_pole()
trojkat.policz_obwod()

kolo = Kolo(5)
kolo.policz_pole()
kolo.policz_obwod()

