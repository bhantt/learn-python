
#--------LİSTELERDE FOR---------#

yorum_yapanlar = ["Ahmet Yılmaz", "Hasan Bırakmaz", "Muhsin Korkmaz"]
kullanici_no = 0
ad,soyad = yorum_yapanlar[0].split()[0], yorum_yapanlar[0].split()[1]

for kullanici in yorum_yapanlar:
   kullanici_no+=1
   
   print("{}. kullanicinin adı: {}, Soyadı: {}".format(kullanici_no,ad,soyad))


#----BOYUTLU LİSTELERDE FOR----#

liste = [[1,2],[3,4]]

for x,y in liste: # x'ler buradaki 1 ve 3 olur. y'ler ise 2 ve 4
   print(x,y) # çıktı = 1 2
              #       = 3 4
   

#----DICTIONARYDE FOR----#

users = {
   'Ad': 'Ahmet',
   'Soyad': 'Han' 
}

for key,value in users.items():
   print("Key: {} |\t| Value: {}".format(key,value)) 
   # çıktı: 
      #Key: Ad         Value: Ahmet
      #Key: Soyad      Value: Han 


#-----SAYILAR İLE FOR-----#

for i in range(5):
   print(i) # 0-5 arasını yazdırır. 5 dahil değil!

for j in range(5,10):
   print(j) #5-10 arasını yazdırır 10 dahil değil!

for k in range(0,11,2):
   print(k) # 0-11 arasını 2'şer 2'şer yazdırır.