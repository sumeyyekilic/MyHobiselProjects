
"""Bir listeden veya dizeden uniq öğeler almak istiyorum"""

#1. listeden uniq ögeleri seçip sıralamak:
karmasikList = [8, 8, 2, 3, 4, 1, 1, 1, 5, 5]

#2 string dize öğelerinden uniq olanları bulmak:
stringDize=("HİİİSMYYAAABBBCCC")


if __name__ == '__main__':
    print (set(karmasikList))
    print(set(stringDize))
