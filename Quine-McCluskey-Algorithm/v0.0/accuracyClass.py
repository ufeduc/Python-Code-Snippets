from inputClass import inputClass

terimSayisi= inputClass.returnTerimSayisi()
minterm= inputClass.returnMinterm()

class accuracy(object):

        def __init__(self,terimSayisi,minterm):

            self.terSay= terimSayisi
            self.mint= minterm

        def termCreator(self):
            while True:
                if self.terSay == "2":
                    return ["a","b"]
                    break
                elif self.terSay == "3":
                    return ["a","b","c"]
                    break
                elif self.terSay == "4":
                    return ["a","b","c","d"]
                    break
                else:
                    print("Unexpectable Term Number!!!")
                    break


        def mintermCreator(self):
            sortedList= []
            for miniterm in self.mint.split(","):
                sortedList.append(int(miniterm))
            sortList= sorted(sortedList)

            uniqList=[]
            for i in range(len(sortList)):
                if sortList[i] not in uniqList:
                    uniqList.append(sortList[i])


            if self.terSay == "2":
                tableList=[]
                for singleMin in uniqList:
                    if singleMin == 0:
                        tableList.append(["0","0"])
                    elif singleMin == 1:
                        tableList.append(["0","1"])
                    elif singleMin == 2:
                        tableList.append(["1","0"])
                    elif singleMin == 3:
                        tableList.append(["1","1"])
                return tableList

            elif self.terSay == "3":
                tableList=[]
                for singleMin in uniqList:
                    if singleMin == 0:
                        tableList.append(["0","0","0"])
                    elif singleMin == 1:
                        tableList.append(["0","0","1"])
                    elif singleMin == 2:
                        tableList.append(["0","1","0"])
                    elif singleMin == 3:
                        tableList.append(["0","1","1"])
                    elif singleMin == 4:
                        tableList.append(["1","0","0"])
                    elif singleMin == 5:
                        tableList.append(["1","0","1"])
                    elif singleMin == 6:
                        tableList.append(["1","1","0"])
                    elif singleMin == 7:
                        tableList.append(["1","1","1"])
                return tableList


            elif self.terSay == "4":
                tableList=[]
                for singleMin in uniqList:
                    if singleMin ==  0:
                        tableList.append(["0","0","0","0"])
                    elif singleMin ==  1:
                        tableList.append(["0","0","0","1"])
                    elif singleMin ==  2:
                        tableList.append(["0","0","1","0"])
                    elif singleMin ==  3:
                        tableList.append(["0","0","1","1"])
                    elif singleMin ==  4:
                        tableList.append(["0","1","0","0"])
                    elif singleMin ==  5:
                        tableList.append(["0","1","0","1"])
                    elif singleMin ==  6:
                        tableList.append(["0","1","1","0"])
                    elif singleMin ==  7:
                        tableList.append(["0","1","1","1"])
                    elif singleMin ==  8:
                        tableList.append(["1","0","0","0"])
                    elif singleMin ==  9:
                        tableList.append(["1","0","0","1"])
                    elif singleMin == 10:
                        tableList.append(["1","0","1","0"])
                    elif singleMin == 11:
                        tableList.append(["1","0","1","1"])
                    elif singleMin == 12:
                        tableList.append(["1","1","0","0"])
                    elif singleMin == 13:
                        tableList.append(["1","1","0","1"])
                    elif singleMin == 14:
                        tableList.append(["1","1","1","0"])
                    elif singleMin == 15:
                        tableList.append(["1","1","1","1"])
                return tableList

            else:
                print("U did not entered well, am i right?")

accuracy= accuracy(terimSayisi,minterm)
accuracy.termCreator()
accuracy.mintermCreator()
