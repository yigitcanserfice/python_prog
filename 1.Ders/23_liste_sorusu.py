"""
1- Klavyeden girilen 5 tane sayiyi bir listeye atarak bunlarin
 karelerinden 20 ciktiginda ortaya cikan sonuca
 gore siralayin ve listeyi buna gore yazdiran programi yaziniz
"""

liste = []

for i in range(0, 5):
    liste.append(eval(input()))


def siralama_fonksiyonu(a):
    return a * a - 20


liste.sort(key=siralama_fonksiyonu)
print(liste)
