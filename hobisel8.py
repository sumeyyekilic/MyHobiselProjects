# *********************************************************
#  **     @sumklc                                         **
#  **     Sümeyye kılıç                                   **
#  **     01.02.2021                                      **
# *********************************************************


"""status param olarak varsayılan bir boolen değer atadım:"""
status=False  #true da atayabilirsiniz..

#bunu kullanarak if şartı yazarsam:

#BİRİNCİ YÖNT
if status:
    s1=1
else:
    s1=0

#İKİNCİ YÖNT.. (best)
s2=1 if status else 0


if __name__ == '__main__':
    print("birinci yöntemde :", s1)
    print("ikinci yöntemde :" , s2)
