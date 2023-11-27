"""Bir fonksiyonda belirtilen listenin tüm elemanlarını 
map fonksiyonu aracılığıyla sırasıyla gönderilip liste de istenilen yapılandırmalar yapılır.
"""

def karesi(sayi):
   return sayi**2

liste = [*range(1,6)]

print([*map(karesi,liste)])

"""
Print Output:
[1, 4, 9, 16, 25]
"""


