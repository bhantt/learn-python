#yapısı:

#while <şart doğruyken>
#   <burayı yap>

x = 0
while x<10:
   print("{} degeri 10'dan kucuktur.".format(x))
   x+=1

#--------------------------------------------------------#

#yapısı2:
#while <şart doğruyken>
#     <burayı yap>
#else:
#  <burayı yap>

x = 0

while x<10:
   print("{} degeri 10'dan kucuktur.".format(x))
   x+=1
else:
   print("{} degeri 10'dan kucuk degil.".format(x))
   
#--------------------------------------------------------#   

#---SONSUZ DÖNGÜ---#

#while True:
   #print("xyz")
   

#--------------------------------------------------------#

sayi = 6
sonuc = 1
while sayi>0:
   sonuc = sonuc*sayi
   sayi-=1
print(sonuc)
   
   



