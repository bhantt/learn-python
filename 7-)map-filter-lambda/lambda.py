#LAMBDA NEDİR?

#Lambda tek satırlık fonksiyonlardır. Birden fazla parametre kabul ederler, fakat tek bir işlem yapabilirler.


sayilar = [*range(1,6)]
print([*map(lambda x: x**2,sayilar)])
"""
Print Output:
[1, 4, 9, 16, 25]
"""

"""
map.py'deki def karesi() fonksiyonu gibi kullanılır.

"""

#filter ile

sayilar2 = [*range(1,6)]

print([*filter(lambda x: x**2 if x%2==0 else None , sayilar2)])
"""
Print Output:
[2, 4]
"""

x = lambda a : a + 20
print(x(5))

"""
Print Output:
25
"""
