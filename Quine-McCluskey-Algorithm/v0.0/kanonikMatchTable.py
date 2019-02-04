from kanonikMatchClass import fourthMatchClass

harf= fourthMatchClass.harfDonusumu()
minterm= fourthMatchClass.mintermler()

class kanonikMatchTable(object):

    def __init__(self,harf,minterm):

        package=[]
        for i in range(len(harf)):

            newList=[]
            if i % 2 == 0:
                newList.append(harf[i])
                newList.append(harf[i+1])
                package.append(newList)
        self.harf= package
        self.minterm= minterm

    def printing(self):

        package=[]
        for i in range(len(self.harf)):
            newList=[]
            for j in range(len(self.minterm)):

                if self.harf[i][1] == self.minterm[j][0]:
                    newList.append(self.harf[i][0])
                    newList.append(self.minterm[j][1])

            package.append(newList)

        newPackage=[]
        for i in range(len(package)):
            newListe=[package[i][0]]
            for j in range(len(package[i])):
                if j % 2 == 1:
                    newListe.append(package[i][j])
            newPackage.append(newListe)

        # print(newPackage)



        print("harfler          mintermler               | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |")
        for i in range(len(newPackage)):
            liste=[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
            for j in range(len(newPackage[i][1:])):
                liste.pop(int(newPackage[i][1:][j]))
                liste.insert(int(newPackage[i][1:][j]),"X")
            print(" {}    {}     | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {}  | {}  | {}  | {}  | {}  | {}  |".format(newPackage[i][0],newPackage[i][1:],liste[0],liste[1],liste[2],liste[3],liste[4],liste[5],liste[6],liste[7],liste[8],liste[9],liste[10],liste[11],liste[12],liste[13],liste[14],liste[15]))
        # print("harfler          mintermler")
        # for f in range(len(newPackage)):
        #     print("{}    {}      ".format(newPackage[f][0],newPackage[f][1:])
        # print(liste[0],liste[1],liste[2],liste[3],liste[4],liste[5],liste[6],liste[7],liste[8],liste[9],liste[10],liste[11],liste[12],liste[13],liste[14],liste[15])

kanonikMatchTable(harf,minterm).printing()
