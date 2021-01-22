""" bikeStore liste elemanlarını diziniyle birlkte her yenilenme durumunda
ekrana yazdırmak istiyorum """

#bisiklet markaları
newBikeStore=["Sedona","Mosso","Kross"]
#bisiklet tüleri
typeOfBike=["26 Rim Mountain Bike","1.0 Road Bike","20 Rim City Bike" ]
index = 0

#1wayBest, dizini depolamak ve her yinelemede güncellemek için bir değişken oluşturmaktır: """
print('***birinci(riskli) yöntem***')
for value in newBikeStore:
	print(index, value)
	index += 1  #indexte sakladığımız sayıyı bir artırılma unutulduğunda hata oluşur:

#secondWayBest,otomatik bir for ile dizin döndürmek için len () ile birlikte range () kullanmak.
print('***ikinci(saglam) yöntem***')
for index in range(len(newBikeStore)):
	    bike = newBikeStore[index]
	    print(index, bike)
	    #bu yolla dizinleri güncellemeyi unutmanın getireceği hata ortadan kalakacaktır.

#Zip() metoduyla birinci, ikinci dizilerimi aynı zamanda yineleyebilriz.
#bisiklet markalarını hangi tür olduklarıyla berber eşleştirmek için For ile, öğeyi birinciden bire, ikinciden ikiye atamak istiyorum:
for isCount, (oneType, twoType) in enumerate(zip(newBikeStore, typeOfBike)):
    print(isCount, oneType, twoType)