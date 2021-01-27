"""n'e kadar olan tamsayıları toplamak isiyorum"""

#deneme1  **iyi çözüm değill
def SumDef(s):
    arttir = 1
    toplam = 0
    while arttir < s + 1:
        toplam= toplam +arttir
        arttir= arttir + 1
    return toplam

print("Yontem1 toplam sonuç:", SumDef(77))


#deneme2 : daha iyi olana kadar **iyi
def SumDef2(s):
    return sum(range(s + 1))

print("Yontem2 toplam sonuç:", SumDef2(77))

#yukardaki kod harika 'mış gibi görünse de hata yönetimim yok ??
#deneme3 :
def SumDef3(s):
    try:
        toplam= sum(range(s + 1))
    except TypeError:
        toplam = 0
    return toplam

print("Yontem3 toplam sonuç:", SumDef3(77))