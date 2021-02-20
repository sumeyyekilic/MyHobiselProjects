# *********************************************************
#  **     @sumklc                                         **
#  **     Sümeyye kılıç                                   **
#  **     20.02.2021                                      **
# *********************************************************


"""range(len()) yerine Enumarete() ile tekrarlamak """

newData1=[11,12,-13,-14]
for data in range(len(newData1)):
	if newData1[data] < 0 :
		newData1[data]=0    """neg degeri 0'a ayarladım"""


##****tricks : enumerate kullanımı daha hoş****

newData2=[11,12,-13,-14]
for index, data2 in enumerate(newData2):
	if data2< 0:
		newData2[index]=0

if __name__ == '__main__':
    print("range(len()) yönteminde :", newData1)
    print("Enumerate() yönteminde :" , newData2)
