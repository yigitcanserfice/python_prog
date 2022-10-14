"""
Bunun hakknda sınav sorusu cıkabılır

"""

def fonksiyonum(n):
    return lambda a: a * n

katini_al = fonksiyonum(2)
print(katini_al(5))

katini_al = fonksiyonum(5)
print(katini_al(5))