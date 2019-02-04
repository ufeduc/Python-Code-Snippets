from thirdMatchClass import  thirdMatch

thirdMatchList = thirdMatch.createThirdMatch()

class thirdMatchClass2(object):

    def __init__(self,thirdMatchList):

        self.thirdMatchList= thirdMatchList

    def createGrup(self):
        # print(self.thirdMatchList)
        # for i in self.thirdMatchList:
        #     print(i)

        j=0
        package=[]
        while j< len(self.thirdMatchList):

            uniqList=[]
            for i in range(len(self.thirdMatchList[j])):
                if self.thirdMatchList[j][i] not in uniqList:
                    uniqList.append(self.thirdMatchList[j][i])
            # print(uniqList)

            counter=0
            for liste in uniqList:
                if counter < self.thirdMatchList[j].count(liste):
                    counter= self.thirdMatchList[j].count(liste)

            # print(counter)

            for liste in uniqList:
                if counter == self.thirdMatchList[j].count(liste):
                    package.append(liste)
                    # print(liste)
            j+=1
        # print(package)
        return package


thirdMatchClass2= thirdMatchClass2(thirdMatchList)
thirdMatchClass2.createGrup()
