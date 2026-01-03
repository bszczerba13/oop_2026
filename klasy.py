#Klasa = szablon, przepis
class Czlowiek:
    #Istota
    #atrybuty klasy
    #(cechy wspolne kazdego czlowieka)
    gatunek = "Homo Sapiens"
    def __init__(self, imie, plec): #atrybuty obiektu (skladniki potrawy)
        #(Cechy konkretnej osoby)
        #Konstruktor
        #Akt istnienia
        print(f"Niech powstanie Czlowiek o imieniu {imie}")
        self.imie = imie
        self.plec = plec

    #Metoda
    #Moznosc (mozliwosc, zdlonosc, umiejetnosc)
    def przedstaw_sie(self):
        print(f"Dzien dobry, mam na imie {self.imie} i jestem ", end="")
        if self.plec == "M":
            print("mezczyzna")
        else:
            print("kobieta")

    def przedstaw(self, osoba):
        print(f"Oto {osoba.imie}")

#Powstanie obiektu
#Gotowanie z przepisu
adam = Czlowiek("Adam", "M")
ewa = Czlowiek("Ewa", "K")

adam.przedstaw_sie()
ewa.przedstaw_sie()

ewa.przedstaw(adam)