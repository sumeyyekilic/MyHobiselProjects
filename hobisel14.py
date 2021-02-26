# *********************************************************
#  **     @sumklc                                         **
#  **     Sümeyye kılıç                                   **
#  **     26.02.2021                                      **
# *********************************************************

#Çok büyük n boyutlu listeler için (image dizisi),
#bazen numpy gibi matematiksel hesaplamaları
#hızlı şekilde yapmayı sağlayan python kütüphanesi kullanmak daha iyidir.

import numpy as geek

#Arrange metodu ile dizi oluşturma
a = geek.arange(9)

a = a.reshape(3, 3)  # Array shape : a dizisini 3 satırlı shape dixziye çevirme.

#diziyi yinele
for x in geek.nditer(a):
    print(x)