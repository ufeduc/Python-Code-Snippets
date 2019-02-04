from accuracyClass import accuracy
from inputClass import inputClass

terim= accuracy.termCreator()
minterm= inputClass.returnMinterm()
mintermTable= accuracy.mintermCreator()


class firstMatch(object):

    def __init__(self,terim,minterm,mintermTable):
        self.terim= terim
        self.minterm= minterm
        self.mintermTable= mintermTable

    def createTable(self):

        sortedList= []
        for miniterm in self.minterm.split(","):
            sortedList.append(int(miniterm))
        sortList= sorted(sortedList)

        uniqList=[]
        for i in range(len(sortList)):
            if sortList[i] not in uniqList:
                uniqList.append(sortList[i])

        grup0=[]
        grup1=[]
        grup2=[]
        grup3=[]
        grup4=[]

        i=0
        while i < len(uniqList):
            if uniqList[i]== 0:
                grup0.append(self.mintermTable[i])
                i+=1
            elif uniqList[i]== 1:
                grup1.append(self.mintermTable[i])
                i+=1
            elif uniqList[i]== 2:
                grup1.append(self.mintermTable[i])
                i+=1
            elif uniqList[i]== 3:
                grup2.append(self.mintermTable[i])
                i+=1
            elif uniqList[i]== 4:
                grup1.append(self.mintermTable[i])
                i+=1
            elif uniqList[i] == 5:
                grup2.append(self.mintermTable[i])
                i+=1
            elif uniqList[i]== 6:
                grup2.append(self.mintermTable[i])
                i+=1
            elif uniqList[i]== 7:
                grup3.append(self.mintermTable[i])
                i+=1
            elif uniqList[i]== 8:
                grup1.append(self.mintermTable[i])
                i+=1
            elif uniqList[i]== 9:
                grup2.append(self.mintermTable[i])
                i+=1
            elif uniqList[i]== 10:
                grup2.append(self.mintermTable[i])
                i+=1
            elif uniqList[i]== 11:
                grup3.append(self.mintermTable[i])
                i+=1
            elif uniqList[i]== 12:
                grup2.append(self.mintermTable[i])
                i+=1
            elif uniqList[i]== 13:
                grup3.append(self.mintermTable[i])
                i+=1
            elif uniqList[i]== 14:
                grup3.append(self.mintermTable[i])
                i+=1
            elif uniqList[i]== 15:
                grup4.append(self.mintermTable[i])
                i+=1


        matchList=[grup0,grup1,grup2,grup3,grup4]
        return matchList

firstMatch=firstMatch(terim,minterm,mintermTable)
firstMatch.createTable()
