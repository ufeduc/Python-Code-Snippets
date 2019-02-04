from accuracyClass import accuracy
from thirdMatchClass2 import thirdMatchClass2

mintermList= accuracy.mintermCreator()
thirdMatch= thirdMatchClass2.createGrup()

class fourthMatchClass(object):

    def __init__(self,mintermList,thirdMatch):

        self.mintermList= mintermList
        self.thirdMatch= thirdMatch

    # def printing(self):
    #
    #     # print(self.minterm)
    #     # print(self.mintermList)
    #     # print(self.thirdMatch)

    def harfDonusumu(self):

        # print(self.thirdMatch)
        returnPackage=[]
        newList=[]
        i=0
        while i< len(self.thirdMatch):

            insidePackage=[]
            j=0
            while j<len(self.thirdMatch[i]):
                if self.thirdMatch[i][j] == "1":
                    if j == 0:
                        insidePackage.append("a")
                    elif j == 1:
                        insidePackage.append("b")
                    elif j == 2:
                        insidePackage.append("c")
                    elif j == 3:
                        insidePackage.append("d")

                elif self.thirdMatch[i][j] == "0":
                    if j == 0:
                        insidePackage.append("a~")
                    elif j == 1:
                        insidePackage.append("b~")
                    elif j == 2:
                        insidePackage.append("c~")
                    elif j == 3:
                        insidePackage.append("d~")
                # print(a[i])
                j+=1
            newList.append(insidePackage)
            newList.append(self.thirdMatch[i])
            i+=1

        return newList


    def mintermler(self):
        packageList=[]
        for i in range(len(self.thirdMatch)):
            for j in range(len(self.mintermList)):
                newList=[]
                counter=0
                for l in range(len(self.mintermList[j])):
                    if self.thirdMatch[i][l] == self.mintermList[j][l]:
                        counter+=1
                        if len(self.mintermList[j]) == 4:
                            if self.mintermList[j] == ['0', '0', '0', '0']:
                                minterm="0"
                            if self.mintermList[j] == ['0', '0', '0', '1']:
                                minterm="1"
                            if self.mintermList[j] == ['0', '0', '1', '0']:
                                minterm="2"
                            if self.mintermList[j] == ['0', '0', '1', '1']:
                                minterm="3"
                            if self.mintermList[j] == ['0', '1', '0', '0']:
                                minterm="4"
                            if self.mintermList[j] == ['0', '1', '0', '1']:
                                minterm="5"
                            if self.mintermList[j] == ['0', '1', '1', '0']:
                                minterm="6"
                            if self.mintermList[j] == ['0', '1', '1', '1']:
                                minterm="7"
                            if self.mintermList[j] == ['1', '0', '0', '0']:
                                minterm="8"
                            if self.mintermList[j] == ['1', '0', '0', '1']:
                                minterm="9"
                            if self.mintermList[j] == ['1', '0', '1', '0']:
                                minterm="10"
                            if self.mintermList[j] == ['1', '0', '1', '1']:
                                minterm="11"
                            if self.mintermList[j] == ['1', '1', '0', '0']:
                                minterm="12"
                            if self.mintermList[j] == ['1', '1', '0', '1']:
                                minterm="13"
                            if self.mintermList[j] == ['1', '1', '1', '0']:
                                minterm="14"
                            if self.mintermList[j] == ['1', '1', '1', '1']:
                                minterm="15"

                        elif len(self.mintermList[j]) == 3:
                            if self.mintermList[j] == ['0', '0', '0']:
                                minterm="0"
                            if self.mintermList[j] == ['0', '0', '1']:
                                minterm="1"
                            if self.mintermList[j] == ['0', '1', '0']:
                                minterm="2"
                            if self.mintermList[j] == ['0', '1', '1']:
                                minterm="3"
                            if self.mintermList[j] == ['1', '0', '0']:
                                minterm="4"
                            if self.mintermList[j] == ['1', '0', '1']:
                                minterm="5"
                            if self.mintermList[j] == ['1', '1', '0']:
                                minterm="6"
                            if self.mintermList[j] == ['1', '1', '1']:
                                minterm="7"

                        elif len(self.mintermList[j]) == 2:
                            if self.mintermList[j] == ['0', '0']:
                                minterm="0"
                            if self.mintermList[j] == ['0', '1']:
                                minterm="1"
                            if self.mintermList[j] == ['1', '0']:
                                minterm="2"
                            if self.mintermList[j] == ['1', '1']:
                                minterm="3"

                if counter == 2:
                    newList.append(self.thirdMatch[i])
                    newList.append(minterm)

                packageList.append(newList)
        package=[]
        for i in packageList:
            if i != []:
                package.append(i)

        return package


fourthMatchClass= fourthMatchClass(mintermList,thirdMatch)
fourthMatchClass.harfDonusumu()
fourthMatchClass.mintermler()
