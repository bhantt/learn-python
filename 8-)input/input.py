# kullanıcıdan veri alma
metin = input("Bir metin gir: ")

#string türünde bir veri alır

#------------------------------------#

sayi = int(input("Bir sayı gir: "))

#int türünde veri alır



#ör 

def app():
   sayi = int(input("Bir sayı gir: "))
   
   if sayi%2==0:
      return "sayı çift"
   else:
      return "sayı tek"
   
print(app())