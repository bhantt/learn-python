"""
def <fonk_adi>():
   <kod>
"""

def bes_yaz():
   print(5)

bes_yaz() #  <== burada foknsiyonu çağırdık./ output: 5

#--------------------------------------------#

"""
def <fonk_adi>(<args>):
   <kod>
"""

def sayi_yaz(a):
   print(a)
   
sayi_yaz(6) # <== Girdiğimiz değeri yazdırır. / output: 6

#---------------------------------------------#

"""
def <fonk_adi>()
   return <any>

"""

def iki_dondur():
   return 2

#Fonksiyon içinde print olmadığından yazdırmak için print kullanmalıyız.

print(iki_dondur()) # <== 

#----------------------------------------------#

"""
Default argüman
"""
def sayi_dondur(sayi = 100): # <== Buradaki '100' dafult değerdir yani eğer sayi_dondur() içine bir şey girmezsek '100' çıktısını alırız.
   return sayi

print(sayi_dondur()) # <== çıktı '100'
print(sayi_dondur(70)) # <== çıktı '70'

#-----------------------------------------------#
"""
Çoklu Argüman
"""

def buyuk_olan(a,b):
   if(a>b):
      return a
   else:
      return b
   
print(buyuk_olan(45,80)) # output: 80
print(buyuk_olan(30,20)) # output: 30

#-----------------------------------------------#

"""
Fonksiyonların ilişkisi
"""

def yazdir(a,b):
   buyuk = buyuk_olan(a,b)
   metin = "{} daha buyuktur".format(buyuk)
   print(metin)
   
yazdir(4,5) # output: 5 daha buyuktur

#-----------------------------------------------#

"""
Fonksiyonlar birden fazla sonuc döndürebilir
"""

def isim_soyimi_ayirma(isim_soyisim):
   isim = isim_soyisim.split()[0]
   soyisim = isim_soyisim.split()[1]
   return isim,soyisim

print(isim_soyimi_ayirma("Ahmet Han")) # output: ('Ahmet', 'Han')

#-----------------------------------------------#

"""
args ifadesi
"""
# def isim_soyisim_birlestir(isim,soyisim): # toplam 3 isimli birisi bu fonksiyonu kullanamaz
#     return " ".join(isim,soyisim)


def isim_soyisim_birlestir(*args): # içeriye kaç değer girdiğinin önemi yok.
   return " ".join(args)

print(isim_soyisim_birlestir("Ahmet", "Han", "Gundogdu")) # output: Ahmet Han Gundogdu

#-----------------------------------------------#
"""
**kwargs ifadesi
"""

def gobek_adi_yazdir(**kwargs): # Aynı dictionary mantığı. 'gobekadi' anahtarının karşılığını yazdırır. 
   if 'gobekadi' in kwargs:
      print(kwargs['gobekadi'])
   else:
      print('gobek adi yok')
      
gobek_adi_yazdir(adi="Ahmet", gobekadi="Han", soyad="Gundogdu") # output: Han
gobek_adi_yazdir(adi="Hasan", soyad = "Decrilmez") # output: gobek adi yok