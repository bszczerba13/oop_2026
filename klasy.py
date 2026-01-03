#Klasa = szablon, przepis
class Czlowiek:
    #Istota
    gatunek = "Homo Sapiens"
    def __init__(self, imie):
        #Konstruktor
        #Akt istnienia
        print(f"Niech powstanie Czlowiek o imieniu {imie}")
        self.imie = imie

#Powstanie obiektu
#Gotowanie z przepisu
adam = Czlowiek("Adam")
ewa = Czlowiek("Ewa")
print(adam.gatunek)
print(ewa.gatunek)
print(adam.imie)
print(ewa.imie)