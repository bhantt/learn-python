#--------- Kullanım Şekli-1-----------

#if <koşul doğruysa>:
   #<bunu yap>

hava_durumu = 'yagisli'
if hava_durumu=='yagisli':
   print('Şemsiyeni Al!')

#-------- Kullanım Şekli-2----------

#if <koşul doğruysa>:
   #<bunu yap>
#else:
   #bunu yap

hava_durumu2 = 'temiz'
if hava_durumu =='temiz':
   print('semsiyeye gerek yok')
else:
   print('semsiyeni al')
   

#--------Kullanım Şekli-3-------------

#if <koşul doğruysa>:
   #<bunu yap>
#elif <bu koşul doğruysa>:
   #<bunu yap>
#else:
   #<bunu yap>
   
hava_durumu3 = 'gunesli'
if hava_durumu3=='yagisli':
   print('semsiteni al')
elif hava_durumu3=='karli':
   print('atkini al')
else:
   print('bir sey almana gerek yok')
   
   
#------ORNEKLER-----#
   yas = 20
   
   if yas>18:
      print('gecebilirsin')
   else:
      print('gecemezsin')
   
   #------------------------------#
   
   if yas>18:
      print('indirim var')
   elif yas<25:
      print('indirim var')
   else:
      print('indirim yok')

#---------LİSTELERDE SORGU-----------#

liste = ['a','b','c']

aranan = 'd'

if aranan in liste:
   print('mevcut')
else:
   print('mevcut degil')
#------------------------------#
aranan2 = 'a'

if aranan2 in liste:
   print('mevcut')
else:
   print('mevcut degil')

#------------------------------#
aranan3 = 'f'
   
if aranan3 in liste:
   print('mevcut')
else:
   liste.append(aranan3)
   print('mevcut degildi listeye ekledim')
   print('Yeni Liste {}'.format(liste)) # çıktı = ['a','b','c','f']
   
#------------------------------#

aranan4 = 'a'

if aranan4 in liste:
   liste.remove(aranan4)
   print('buldum ve kaldırdım')
   print('Yeni Liste {}'.format(liste)) # çıktı = ['b','c','f']
else:
   print('bulamadım')
   
   
#------------------------------#

aranan3 = 'f'

if (aranan3 in liste) and (aranan3==liste[2]):
   print('Evet aranan {}'.format(aranan3),' var ve 2. indexte') #['b','c','f']
else:
   print('bulamadım')