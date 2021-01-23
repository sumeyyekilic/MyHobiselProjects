"""Generator ifadeleri fonksiyonları çağırıları yaparken
 genelde bağımsız değişken olarak kullanılır."""

seqOfNum = [1, 2, 3, 4, 5, 6, 7]
takeSquare = []

for num in seqOfNum:
    takeSquare.append(num ** 2)

firstWay=takeSquare


"""bir fonk ile bir çok yere entegre edebilir"""
def takeSquareDef(seqOfNum):
    return (seqOfNum ** 2)

""" list () ifadesimi şu şekilde çağırarak yukarıdaki örnekle aynı sonucu elde edebiliyorum:"""
secondWay=list(takeSquareDef(x) for x in seqOfNum)

if __name__ == '__main__':

    print(firstWay)
    print(secondWay)
