from accuracyClass import accuracy
from firstMatchClass import firstMatch

terim= accuracy.termCreator()
matchList= firstMatch.createTable()


class firstMatchTable(object):

    def __init__(self,terim,matchList):
        self.terim= terim
        self.matchList= matchList

    def createMatchTable(self):

        grup0=self.matchList[0]
        grup1=self.matchList[1]
        grup2=self.matchList[2]
        grup3=self.matchList[3]
        grup4=self.matchList[4]

        print("GRUPLAR  {}".format(self.terim))
        print("*****************************")
        for i in range(len(grup0)):
            print("GRUP0    {} ".format(grup0[i]))
        print()
        for i in range(len(grup1)):
            print("GRUP1    {} ".format(grup1[i]))
        print()
        for i in range(len(grup2)):
            print("GRUP2    {} ".format(grup2[i]))
        print()
        for i in range(len(grup3)):
            print("GRUP3    {} ".format(grup3[i]))
        print()
        for i in range(len(grup4)):
            print("GRUP4    {} ".format(grup4[i]))



firstMatchTable(terim,matchList).createMatchTable()
