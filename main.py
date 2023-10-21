from turkishLanguagePack import *

# Veri Tipleri // Data Types

benimTamSayi = tamSayi(31)
benimOndalikli = ondalikliSayi(16.5)
benimDizgi = dizgi("Economy")
benimBool = dogrulukDegeri(True)

# Print Function
yazdir(benimOndalikli * benimTamSayi)
yazdir("İstanbul not Constantinople")
yazdir()

# for Function
her(aralik(1, 6), yazdir)


# if function
def dogruIse():
    print("Dogru")


def yanlisIse():
    print("Yanlis")


eger(2 > 3, dogruIse, yanlisIse)


# while function


def artır():
    global sayac
    sayac += 1


def kosul():
    global sayac
    return sayac < 5


def ekleYazdir(item):
    yazdir(item)


def karesiniAl(item):
    yazdir(item ** 2)


oldukca(aralik(0, 5), ekleYazdir)

yazdir("\n#######\n")

oldukca(aralik(1, 6), karesiniAl)

# max and min function

benimListe = [5, 12, 9, 3, 21, 7]

en_buyuk = enBuyuk(benimListe)
en_kucuk = enKucuk(benimListe)

yazdir("En büyük değer: " + dizgi(en_buyuk))
yazdir("En küçük değer: " + dizgi(en_kucuk))
