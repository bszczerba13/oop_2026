#Klasa = szablon, przepis
class Czlowiek:
    #Istota
    gatunek = "Homo Sapiens"
    def __init__(self):
        #Konstruktor
        #Akt istnienia
        print("Niech powstanie Czlowiek")

#Powstanie obiektu
#Gotowanie z przepisu
adam = Czlowiek()
print(adam.gatunek)