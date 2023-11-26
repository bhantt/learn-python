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