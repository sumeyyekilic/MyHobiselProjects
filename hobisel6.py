#birden fazla boş satırlar python kodunun sonucunu etkilemez

baslangic=0
bitis=80

for s in range(1,10):
   tahmin_et=int((baslangic+bitis)/2)
   cevap=input(str(tahmin_et) + "yaşında mısın?")

   if cevap=='evet':
      print("doğru cevap!")
      break
   elif cevap=='daha az':
      bitis=tahmin_et
   elif cevap=='daha çok':
      baslangic=tahmin_et
   else:
      print("yanlış cevap!..")




