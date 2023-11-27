#FILTER NEDİR?
# Python da filter, bir fonksiyondan True dönen elementler için liste oluşturur ve for döngüsüne benzetilebilir. 
# Filter fonksiyonu yerleşik bir fonksiyondur ve çok daha hızlıdır.

def tek_sayileri_filtrele(x):
   if x%2==1:
      return x
   else:
      None
      
print(tek_sayileri_filtrele(3))
"""Print Output:
3
"""
#------#
print(tek_sayileri_filtrele(2))
"""
Print Output:
None
"""

#OR

def cift_sayilari_filtrele(y):
   return y if y%2==0 else None

print(cift_sayilari_filtrele(2))
"""
Print Output:
2
"""

#-------------FILTER-------------#

sayilar = [*range(1,6)]
print([*filter(tek_sayileri_filtrele,sayilar)])
"""
Print Output:
[1, 3, 5]
"""
