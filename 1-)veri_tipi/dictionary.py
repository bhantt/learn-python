user = {
   'Name': 'Batuhan',
   'Age': '20',
   'Location':{
      'BornState': 'Kayseri',
      'CurrentState': 'Amasya'
   
   }
}

print(user.keys()) # anahtarları gösterir
print(user.values()) # anahtarlara karşılık gelen değerleri gösterir
print(user.get('Location')) # Location içindeki değerleri gösterir/çeker
print(user['Location']['BornState']) # Location içinde bulunan BornState'deki veriyi çeker




