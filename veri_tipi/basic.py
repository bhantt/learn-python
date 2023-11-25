# tipi otomatik algılar yani

####### int sayi = 5 gibi başına int yazmaya gerek yok #######

###--------SAYI VERİ TİPLERİ--------###
##--INT--##
sayi = 5
print(sayi)

##--FLOAT--##
sayi2 = 5.0
sayi3 = 3.2 # noktalı olmalı
print(sayi2)
print(sayi3)


##--BOOLEAN--##
gercek = True # 0'dan farklı her değer
yalan = False # 0
print(gercek)
print(yalan)

##--LIST--##
list  = [1,True,"hello", 4.0] # değiştirilebilir liste
print(list)

##--SET--##
set  = {1,1,1,1,2,2,False,False} # bir değerden birden çok varsa o değeri tekli yapar yani çıktısı = {False,1,2} olur.
print(set)

##--DICTIONARY--##
dict = {'isim':'Batuhan', 'Yas ':'20'} # anahtar ve değer olarak düşünebiliriz anahtar = isim, değer = batuhan'dır.
print(dict)

##--TUPLE--##
tup  = (1,2,True) # değiştirilemez liste
print(tup)

print()
###--------STRING VERİ TİPLERİ--------###

##-STRING--##
metin = "Hello World!"
print(metin)


print()
##-INDEX-##
print(metin[3]) 
# eğer bir yerden itibaren başlatmak istiyorsanız da
print(metin[3:]) # 3. indexten sona kadar gider
print(metin[3:7]) # 3. indexten 7. indexe kadar gider 3 dahil ama 7. index dahil değildir.
print(metin[0:3:2]) # 0. indexten başla, 3. indexe git 2 atla

print()
##-LENGTH-##
print(len(metin)) # saymaya 1'den başlar!

print()
##-CONCAT--## 

print(metin+" Merhaba Dünya!")

#metin +=" Batuhan!"
print(metin)

##-ÇARPMA-##

print(metin*5)

print()
##-UPPERCASE-LOWER-SPLİT##

print(metin.upper())
print(metin.lower())
print(metin.split()) # ayırma
