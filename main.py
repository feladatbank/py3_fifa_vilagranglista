'''
* A képernyőre írást igénylő részfeladatok eredményék megjelenítése előtt írja a képernyőre a feladat sorszámát (például: 3. feladat:)!
* Az egyes feladtokban a kiírásokat a minta szerint készítse el!
* Az azonosítókat p kis- és nagybetűkkel is kezdheti
* Az ékezetmentes kiírás is elfogadott.
* A program megírásakor a fájlban lévő adatok helyes szerkezetét nem kell ellenőriznie, feltételezheti, hogy a rendelkezésre álló adatok a leírtaknak megfelelnek
* Megoldását úgy készítse el, hogy az azonos szerkezetű, de tetszőleges bemeneti adatok mellet is helyes eredményt adjon

Hozz létre egy osztályt (class) létrehozása NEM KÖTELEZŐ DE több pontot lehet kapni osztály használata esetén, 
ami reprezentálja egy alkalmazott példányait (object) istance. Az osztály konstruktora (constructor) paraméterként kapja meg a beolvasott sort, 
és ebből határozza meg az adott attribútomokat (property). 

1. feladat:
Készítsen konzolalkalmazást (projektet) a következő feladatok megoldásához, amelynek forráskódját "FIFAvilagranglista" néven mentse el!

2. feladat:
Olvassa be a "fifa.txt" állomány sorait és tárolja az adatokat egy olyan összetett adatszerkezetben (pl. vektor, lista, stb.), amely használatával a további feladatok megoldhatók/ Ügyeljen arra, hogy az állomány első sora a mezőneveket tartalmazza!

3. feladat:
Határozza meg és írja ki a képernyőre a minta szerint, hogy hány csapat szerepel a forrásállományban!

4. feladat:
Határozza meg a ranglistán szereplő csapatok által elért pontszámok átlagát!
Az eredményt két tizedesjegyre kerekítve jelenítse meg a minta szerint

5. feladat:
Határozza meg és írja ki a képernyőre a minta szerint a legtöbbet javító (Valtozas) csapat adatait! Feltételezheti, hogy nem alakult ki holtverseny

'''
class Fifa:
  def __init__(self, sor):
    csapat, helyezes, valtozas, pontszam = sor.strip().split(";")
    self.csapat = csapat
    self.helyezes = int(helyezes)
    self.valtozas = int(valtozas)
    self.pontszam = int(pontszam)

lista = []
with open("fifa.txt", "r", encoding="latin2") as f:
  f.readline()
  for sor in f:
    lista.append(Fifa(sor))

#3. feladat:
print(f"3. feladat: A világranglistán {len(lista)} csapat szerepel")

#4. feladat:
ossz = 0
for sor in lista:
  ossz += sor.pontszam
print(f"4. feladat: A csapatok átlagos pontszáma: {round(ossz / len(lista), 2)} pont")

#5. feladat:
'''
valtozas = max(lista, key=lambda x:x.valtozas)
print(f"5. feladat: A legtöbbet javító csapat: \n        Helyezés: {valtozas.helyezes} \n        Csapat: {valtozas.csapat} \n        Pontszám: {valtozas.pontszam}")
'''

# Vagy

valtozas = lista[0].valtozas
for sor in lista:
  if sor.valtozas > valtozas:
    valtozas = sor.valtozas
    helyezes = sor.helyezes
    csapat = sor.csapat
    pontszam = sor.pontszam
print(f"5. feladat: A legtöbbet javító csapat: \n        Helyezés: {helyezes} \n        Csapat: {csapat} \n        Pontszám: {pontszam}")
