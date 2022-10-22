"""Kendisine gonderilen sayilardan sadece palindrom olanlari toplayan,
 digerlerini de bu toplamdan cikaran ve geri donduren python programini yaziniz"""



def polinDram(*dram):
    toplam = 0
    for sayi in dram:
        ters = str(sayi)[::-1]
        if ters == str(sayi):
            toplam += sayi
        else:
            toplam -= sayi

    return toplam


print(polinDram(10, 101, 55, 40, 9009))


