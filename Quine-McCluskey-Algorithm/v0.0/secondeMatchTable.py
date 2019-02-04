from secondeMatchClass import secondeMatch
from accuracyClass import accuracy

matchTable= secondeMatch.createSecondeMatch()
terim= accuracy.termCreator()

class secondeMatchTable(object):

    def __init__(self,matchTable,terim):

        self.matchTable= matchTable
        self.terim= terim

    def createSecondeMatchTable(self):

        grup0= self.matchTable[0]
        grup1= self.matchTable[1]
        grup2= self.matchTable[2]
        grup3= self.matchTable[3]

        print("GRUPLAR   {}".format(self.terim))
        print()
        for i in range(len(grup0)):
            print("GRUP0     {}".format(grup0[i]))
        print()
        for i in range(len(grup1)):
            print("GRUP1     {}".format(grup1[i]))
        print()
        for i in range(len(grup2)):
            print("GRUP2     {}".format(grup2[i]))
        print()
        for i in range(len(grup3)):
            print("GRUP3     {}".format(grup3[i]))

secondeMatchTable(matchTable,terim).createSecondeMatchTable()
