class Kutya:
    def __init__(self, nev, fajta, eletkor, gazdi):
        self.nev = str(nev)
        self.fajta = str(fajta)
        self.eletkor = int(eletkor)
        self.gazdi = str(gazdi)

    def __str__(self):
        return f"{self.nev} ({self.fajta}, {self.eletkor}) - gazdi: {self.gazdi} \n"

kutyakiallitas = []
#1. feladat
def beolvasas():
    with open("kutyak.txt", encoding = "utf-8") as f:
        for line in f:
            line = line.strip()
            adatok = line.split(";")
            kutya = Kutya(adatok[0], adatok[1], adatok[2], adatok[3])
            kutyakiallitas.append(kutya)
    f.close()

#1. feladat
def db():
    print(f"{len(kutyakiallitas)} kutya szerepel a listában")

def main():
    beolvasas()
    db()

main()