#string formatlama
#format() methodu bir stringin seçili kısımlarını formatlamayı sağlar

#bir kullnıcı inputundan veya database den gelen ve
# bizim kontrolümüzde olmayan metinler oluyor.
# curly brackets dediğimiz {} ile format() metodunu çalıştırarak bu metinlerin kontrolünü sağlarız.

#dolar kuru görüntülemek istiyorum :
kur = 7.4266

metin= "Bugun doların satış kuru {}TL.."
print(metin.format(kur))

