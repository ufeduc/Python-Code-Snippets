from thirdMatchClass2 import thirdMatchClass2
from accuracyClass import accuracy

liste= thirdMatchClass2.createGrup()
terim= accuracy.termCreator()

class thirdMatchTable(object):

    def __init__(self,liste,terim):

        self.liste= liste
        self.terim= terim

    def createTable(self):

        print("GRUPLAR   {}".format(self.terim))
        for i in range(len(self.liste)):
            print()
            print("GRUP{}     {}".format(i,self.liste[i]))


thirdMatchTable= thirdMatchTable(liste,terim)
thirdMatchTable.createTable()
