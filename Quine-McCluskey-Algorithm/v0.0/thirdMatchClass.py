from secondeMatchClass import secondeMatch

matchList= secondeMatch.createSecondeMatch()


class thirdMatch(object):

    def __init__(self,matchList):

        self.matchList= matchList

    def createThirdMatch(self):

        #grup0 --------------------
        if self.matchList[0] != []:
            if len(self.matchList[0]) == 4:
                grup00= self.matchList[0][0]
                grup01= self.matchList[0][1]
                grup02= self.matchList[0][2]
                grup03= self.matchList[0][3]
            elif len(self.matchList[0]) == 3:
                grup00= self.matchList[0][0]
                grup01= self.matchList[0][1]
                grup02= self.matchList[0][2]
                grup03= []
            elif len(self.matchList[0]) == 2:
                grup00= self.matchList[0][0]
                grup01= self.matchList[0][1]
                grup02= []
                grup03= []
            elif len(self.matchList[0]) == 1:
                grup00= self.matchList[0][0]
                grup01= []
                grup02= []
                grup03= []
        else:
            grup00= []
            grup01= []
            grup02= []
            grup03= []

        #grup1------------------------------------------
        if self.matchList[1] != []:
            if len(self.matchList[1]) == 13:
                grup10= self.matchList[1][0]
                grup11= self.matchList[1][1]
                grup12= self.matchList[1][2]
                grup13= self.matchList[1][3]
                grup14= self.matchList[1][4]
                grup15= self.matchList[1][5]
                grup16= self.matchList[1][6]
                grup17= self.matchList[1][7]
                grup18= self.matchList[1][8]
                grup19= self.matchList[1][9]
                grup110= self.matchList[1][10]
                grup111= self.matchList[1][11]
                grup112= self.matchList[1][12]
            elif len(self.matchList[1]) == 12:
                grup10= self.matchList[1][0]
                grup11= self.matchList[1][1]
                grup12= self.matchList[1][2]
                grup13= self.matchList[1][3]
                grup14= self.matchList[1][4]
                grup15= self.matchList[1][5]
                grup16= self.matchList[1][6]
                grup17= self.matchList[1][7]
                grup18= self.matchList[1][8]
                grup19= self.matchList[1][9]
                grup110= self.matchList[1][10]
                grup111= self.matchList[1][11]
                grup112= []
            elif len(self.matchList[1]) == 11:
                grup10= self.matchList[1][0]
                grup11= self.matchList[1][1]
                grup12= self.matchList[1][2]
                grup13= self.matchList[1][3]
                grup14= self.matchList[1][4]
                grup15= self.matchList[1][5]
                grup16= self.matchList[1][6]
                grup17= self.matchList[1][7]
                grup18= self.matchList[1][8]
                grup19= self.matchList[1][9]
                grup110= self.matchList[1][10]
                grup111= []
                grup112= []
            elif len(self.matchList[1]) == 10:
                grup10= self.matchList[1][0]
                grup11= self.matchList[1][1]
                grup12= self.matchList[1][2]
                grup13= self.matchList[1][3]
                grup14= self.matchList[1][4]
                grup15= self.matchList[1][5]
                grup16= self.matchList[1][6]
                grup17= self.matchList[1][7]
                grup18= self.matchList[1][8]
                grup19= self.matchList[1][9]
                grup110= []
                grup111= []
                grup112= []
            elif len(self.matchList[1]) == 9:
                grup10= self.matchList[1][0]
                grup11= self.matchList[1][1]
                grup12= self.matchList[1][2]
                grup13= self.matchList[1][3]
                grup14= self.matchList[1][4]
                grup15= self.matchList[1][5]
                grup16= self.matchList[1][6]
                grup17= self.matchList[1][7]
                grup18= self.matchList[1][8]
                grup19= []
                grup110= []
                grup111= []
                grup112= []
            elif len(self.matchList[1]) == 8:
                grup10= self.matchList[1][0]
                grup11= self.matchList[1][1]
                grup12= self.matchList[1][2]
                grup13= self.matchList[1][3]
                grup14= self.matchList[1][4]
                grup15= self.matchList[1][5]
                grup16= self.matchList[1][6]
                grup17= self.matchList[1][7]
                grup18= []
                grup19= []
                grup110= []
                grup111= []
                grup112= []
            elif len(self.matchList[1]) == 7:
                grup10= self.matchList[1][0]
                grup11= self.matchList[1][1]
                grup12= self.matchList[1][2]
                grup13= self.matchList[1][3]
                grup14= self.matchList[1][4]
                grup15= self.matchList[1][5]
                grup16= self.matchList[1][6]
                grup17= []
                grup18= []
                grup19= []
                grup110= []
                grup111= []
                grup112= []
            elif len(self.matchList[1]) == 6:
                grup10= self.matchList[1][0]
                grup11= self.matchList[1][1]
                grup12= self.matchList[1][2]
                grup13= self.matchList[1][3]
                grup14= self.matchList[1][4]
                grup15= self.matchList[1][5]
                grup16= []
                grup17= []
                grup18= []
                grup19= []
                grup110= []
                grup111= []
                grup112= []
            elif len(self.matchList[1]) == 5:
                grup10= self.matchList[1][0]
                grup11= self.matchList[1][1]
                grup12= self.matchList[1][2]
                grup13= self.matchList[1][3]
                grup14= self.matchList[1][4]
                grup15= []
                grup16= []
                grup17= []
                grup18= []
                grup19= []
                grup110= []
                grup111= []
                grup112= []
            elif len(self.matchList[1]) == 4:
                grup10= self.matchList[1][0]
                grup11= self.matchList[1][1]
                grup12= self.matchList[1][2]
                grup13= self.matchList[1][3]
                grup14= []
                grup15= []
                grup16= []
                grup17= []
                grup18= []
                grup19= []
                grup110= []
                grup111= []
                grup112= []
            elif len(self.matchList[1]) == 3:
                grup10= self.matchList[1][0]
                grup11= self.matchList[1][1]
                grup12= self.matchList[1][2]
                grup13= []
                grup14= []
                grup15= []
                grup16= []
                grup17= []
                grup18= []
                grup19= []
                grup110= []
                grup111= []
                grup112= []
            elif len(self.matchList[1]) == 2:
                grup10= self.matchList[1][0]
                grup11= self.matchList[1][1]
                grup12= []
                grup13= []
                grup14= []
                grup15= []
                grup16= []
                grup17= []
                grup18= []
                grup19= []
                grup110= []
                grup111= []
                grup112= []
            elif len(self.matchList[1]) == 1:
                grup10= self.matchList[1][0]
                grup11= []
                grup12= []
                grup13= []
                grup14= []
                grup15= []
                grup16= []
                grup17= []
                grup18= []
                grup19= []
                grup110= []
                grup111= []
                grup112= []
        else:
            grup10= []
            grup11= []
            grup12= []
            grup13= []
            grup14= []
            grup15= []
            grup16= []
            grup17= []
            grup18= []
            grup19= []
            grup110= []
            grup111= []
            grup112= []

        #grup2------------------------------------------
        if self.matchList[2] != []:
            if len(self.matchList[2]) == 12:
                grup20= self.matchList[2][0]
                grup21= self.matchList[2][1]
                grup22= self.matchList[2][2]
                grup23= self.matchList[2][3]
                grup24= self.matchList[2][4]
                grup25= self.matchList[2][5]
                grup26= self.matchList[2][6]
                grup27= self.matchList[2][7]
                grup28= self.matchList[2][8]
                grup29= self.matchList[2][9]
                grup210= self.matchList[2][10]
                grup211= self.matchList[2][11]
                grup212= []
            elif len(self.matchList[2]) == 11:
                grup20= self.matchList[2][0]
                grup21= self.matchList[2][1]
                grup22= self.matchList[2][2]
                grup23= self.matchList[2][3]
                grup24= self.matchList[2][4]
                grup25= self.matchList[2][5]
                grup26= self.matchList[2][6]
                grup27= self.matchList[2][7]
                grup28= self.matchList[2][8]
                grup29= self.matchList[2][9]
                grup210= self.matchList[2][10]
                grup211= []
                grup212= []
            elif len(self.matchList[2]) == 10:
                grup20= self.matchList[2][0]
                grup21= self.matchList[2][1]
                grup22= self.matchList[2][2]
                grup23= self.matchList[2][3]
                grup24= self.matchList[2][4]
                grup25= self.matchList[2][5]
                grup26= self.matchList[2][6]
                grup27= self.matchList[2][7]
                grup28= self.matchList[2][8]
                grup29= self.matchList[2][9]
                grup210= []
                grup211= []
                grup212= []
            elif len(self.matchList[2]) == 9:
                grup20= self.matchList[2][0]
                grup21= self.matchList[2][1]
                grup22= self.matchList[2][2]
                grup23= self.matchList[2][3]
                grup24= self.matchList[2][4]
                grup25= self.matchList[2][5]
                grup26= self.matchList[2][6]
                grup27= self.matchList[2][7]
                grup28= self.matchList[2][8]
                grup29= []
                grup210= []
                grup211= []
                grup212= []
            elif len(self.matchList[2]) == 8:
                grup20= self.matchList[2][0]
                grup21= self.matchList[2][1]
                grup22= self.matchList[2][2]
                grup23= self.matchList[2][3]
                grup24= self.matchList[2][4]
                grup25= self.matchList[2][5]
                grup26= self.matchList[2][6]
                grup27= self.matchList[2][7]
                grup28= []
                grup29= []
                grup210= []
                grup211= []
                grup212= []
            elif len(self.matchList[2]) == 7:
                grup20= self.matchList[2][0]
                grup21= self.matchList[2][1]
                grup22= self.matchList[2][2]
                grup23= self.matchList[2][3]
                grup24= self.matchList[2][4]
                grup25= self.matchList[2][5]
                grup26= self.matchList[2][6]
                grup27= []
                grup28= []
                grup29= []
                grup210= []
                grup211= []
                grup212= []
            elif len(self.matchList[2]) == 6:
                grup20= self.matchList[2][0]
                grup21= self.matchList[2][1]
                grup22= self.matchList[2][2]
                grup23= self.matchList[2][3]
                grup24= self.matchList[2][4]
                grup25= self.matchList[2][5]
                grup26= []
                grup27= []
                grup28= []
                grup29= []
                grup210= []
                grup211= []
                grup212= []
            elif len(self.matchList[2]) == 5:
                grup20= self.matchList[2][0]
                grup21= self.matchList[2][1]
                grup22= self.matchList[2][2]
                grup23= self.matchList[2][3]
                grup24= self.matchList[2][4]
                grup25= []
                grup26= []
                grup27= []
                grup28= []
                grup29= []
                grup210= []
                grup211= []
                grup212= []
            elif len(self.matchList[2]) == 4:
                grup20= self.matchList[2][0]
                grup21= self.matchList[2][1]
                grup22= self.matchList[2][2]
                grup23= self.matchList[2][3]
                grup24= []
                grup25= []
                grup26= []
                grup27= []
                grup28= []
                grup29= []
                grup210= []
                grup211= []
                grup212= []
            elif len(self.matchList[2]) == 3:
                grup20= self.matchList[2][0]
                grup21= self.matchList[2][1]
                grup22= self.matchList[2][2]
                grup23= []
                grup24= []
                grup25= []
                grup26= []
                grup27= []
                grup28= []
                grup29= []
                grup210= []
                grup211= []
                grup212= []
            elif len(self.matchList[2]) == 2:
                grup20= self.matchList[2][0]
                grup21= self.matchList[2][1]
                grup22= []
                grup23= []
                grup24= []
                grup25= []
                grup26= []
                grup27= []
                grup28= []
                grup29= []
                grup210= []
                grup211= []
                grup212= []
            elif len(self.matchList[2]) == 1:
                grup20= self.matchList[2][0]
                grup21= []
                grup22= []
                grup23= []
                grup24= []
                grup25= []
                grup26= []
                grup27= []
                grup28= []
                grup29= []
                grup210= []
                grup211= []
                grup212= []
        else:
            grup20= []
            grup21= []
            grup22= []
            grup23= []
            grup24= []
            grup25= []
            grup26= []
            grup27= []
            grup28= []
            grup29= []
            grup210= []
            grup211= []
            grup212= []

        #grup3 --------------------
        if self.matchList[3] != []:
            if len(self.matchList[3]) == 4:
                grup30= self.matchList[3][0]
                grup31= self.matchList[3][1]
                grup32= self.matchList[3][2]
                grup33= self.matchList[3][3]
            elif len(self.matchList[3]) == 3:
                grup30= self.matchList[3][0]
                grup31= self.matchList[3][1]
                grup32= self.matchList[3][2]
                grup33= []
            elif len(self.matchList[3]) == 2:
                grup30= self.matchList[3][0]
                grup31= self.matchList[3][1]
                grup32= []
                grup33= []
            elif len(self.matchList[3]) == 1:
                grup30= self.matchList[3][0]
                grup31= []
                grup32= []
                grup33= []
        else:
            grup30= []
            grup31= []
            grup32= []
            grup33= []

        # HellJumper!

        #sifirin sifiri ---------------------------------
        if grup00 != []:
            if grup10 != []:
                i=0
                grup0010=[]
                while i < len(grup10):
                    if grup00[i] == grup10[i]:
                        grup0010.append(grup00[i])
                    else:
                        grup0010.append("-")
                    i+=1
            else:
                grup0010=[]

            if grup11 != []:
                i=0
                grup0011=[]
                while i < len(grup11):
                    if grup00[i] == grup11[i]:
                        grup0011.append(grup00[i])
                    else:
                        grup0011.append("-")
                    i+=1
            else:
                grup0011=[]

            if grup12 != []:
                i=0
                grup0012=[]
                while i < len(grup12):
                    if grup00[i] == grup12[i]:
                        grup0012.append(grup00[i])
                    else:
                        grup0012.append("-")
                    i+=1
            else:
                grup0012=[]

            if grup13 != []:
                i=0
                grup0013=[]
                while i < len(grup13):
                    if grup00[i] == grup13[i]:
                        grup0013.append(grup00[i])
                    else:
                        grup0013.append("-")
                    i+=1
            else:
                grup0013=[]

            if grup14 != []:
                i=0
                grup0014=[]
                while i < len(grup14):
                    if grup00[i] == grup14[i]:
                        grup0014.append(grup00[i])
                    else:
                        grup0014.append("-")
                    i+=1
            else:
                grup0014=[]

            if grup15 != []:
                i=0
                grup0015=[]
                while i < len(grup15):
                    if grup00[i] == grup15[i]:
                        grup0015.append(grup00[i])
                    else:
                        grup0015.append("-")
                    i+=1
            else:
                grup0015=[]

            if grup16 != []:
                i=0
                grup0016=[]
                while i < len(grup16):
                    if grup00[i] == grup16[i]:
                        grup0016.append(grup00[i])
                    else:
                        grup0016.append("-")
                    i+=1
            else:
                grup0016=[]

            if grup17 != []:
                i=0
                grup0017=[]
                while i < len(grup17):
                    if grup00[i] == grup17[i]:
                        grup0017.append(grup00[i])
                    else:
                        grup0017.append("-")
                    i+=1
            else:
                grup0017=[]

            if grup18 != []:
                i=0
                grup0018=[]
                while i < len(grup18):
                    if grup00[i] == grup18[i]:
                        grup0018.append(grup00[i])
                    else:
                        grup0018.append("-")
                    i+=1
            else:
                grup0018=[]

            if grup19 != []:
                i=0
                grup0019=[]
                while i < len(grup19):
                    if grup00[i] == grup19[i]:
                        grup0019.append(grup00[i])
                    else:
                        grup0019.append("-")
                    i+=1
            else:
                grup0019=[]

            if grup110 != []:
                i=0
                grup00110=[]
                while i < len(grup110):
                    if grup00[i] == grup110[i]:
                        grup00110.append(grup00[i])
                    else:
                        grup00110.append("-")
                    i+=1
            else:
                grup00110=[]

            if grup111 != []:
                i=0
                grup00111=[]
                while i < len(grup111):
                    if grup00[i] == grup111[i]:
                        grup00111.append(grup00[i])
                    else:
                        grup00111.append("-")
                    i+=1
            else:
                grup00111=[]

            if grup112 != []:
                i=0
                grup00112=[]
                while i < len(grup112):
                    if grup00[i] == grup112[i]:
                        grup00112.append(grup00[i])
                    else:
                        grup00112.append("-")
                    i+=1
            else:
                grup00112=[]

        else:
            grup0010=[]
            grup0011=[]
            grup0012=[]
            grup0013=[]
            grup0014=[]
            grup0015=[]
            grup0016=[]
            grup0017=[]
            grup0018=[]
            grup0019=[]
            grup00110=[]
            grup00111=[]
            grup00112=[]

        #sifirin biri ---------------------------------
        if grup01 != []:
            if grup10 != []:
                i=0
                grup0110=[]
                while i < len(grup10):
                    if grup01[i] == grup10[i]:
                        grup0110.append(grup01[i])
                    else:
                        grup0110.append("-")
                    i+=1
            else:
                grup0110=[]

            if grup11 != []:
                i=0
                grup0111=[]
                while i < len(grup11):
                    if grup01[i] == grup11[i]:
                        grup0111.append(grup01[i])
                    else:
                        grup0111.append("-")
                    i+=1
            else:
                grup0111=[]

            if grup12 != []:
                i=0
                grup0112=[]
                while i < len(grup12):
                    if grup01[i] == grup12[i]:
                        grup0112.append(grup01[i])
                    else:
                        grup0112.append("-")
                    i+=1
            else:
                grup0112=[]

            if grup13 != []:
                i=0
                grup0113=[]
                while i < len(grup13):
                    if grup01[i] == grup13[i]:
                        grup0113.append(grup01[i])
                    else:
                        grup0113.append("-")
                    i+=1
            else:
                grup0113=[]

            if grup14 != []:
                i=0
                grup0114=[]
                while i < len(grup14):
                    if grup01[i] == grup14[i]:
                        grup0114.append(grup01[i])
                    else:
                        grup0114.append("-")
                    i+=1
            else:
                grup0114=[]

            if grup15 != []:
                i=0
                grup0115=[]
                while i < len(grup15):
                    if grup01[i] == grup15[i]:
                        grup0115.append(grup01[i])
                    else:
                        grup0115.append("-")
                    i+=1
            else:
                grup0115=[]

            if grup16 != []:
                i=0
                grup0116=[]
                while i < len(grup16):
                    if grup01[i] == grup16[i]:
                        grup0116.append(grup01[i])
                    else:
                        grup0116.append("-")
                    i+=1
            else:
                grup0116=[]

            if grup17 != []:
                i=0
                grup0117=[]
                while i < len(grup17):
                    if grup01[i] == grup17[i]:
                        grup0117.append(grup01[i])
                    else:
                        grup0117.append("-")
                    i+=1
            else:
                grup0117=[]

            if grup18 != []:
                i=0
                grup0118=[]
                while i < len(grup18):
                    if grup01[i] == grup18[i]:
                        grup0118.append(grup01[i])
                    else:
                        grup0118.append("-")
                    i+=1
            else:
                grup0118=[]

            if grup19 != []:
                i=0
                grup0119=[]
                while i < len(grup19):
                    if grup01[i] == grup19[i]:
                        grup0119.append(grup01[i])
                    else:
                        grup0119.append("-")
                    i+=1
            else:
                grup0119=[]

            if grup110 != []:
                i=0
                grup01110=[]
                while i < len(grup110):
                    if grup01[i] == grup110[i]:
                        grup01110.append(grup01[i])
                    else:
                        grup01110.append("-")
                    i+=1
            else:
                grup01110=[]

            if grup111 != []:
                i=0
                grup01111=[]
                while i < len(grup111):
                    if grup01[i] == grup111[i]:
                        grup01111.append(grup01[i])
                    else:
                        grup01111.append("-")
                    i+=1
            else:
                grup01111=[]

            if grup112 != []:
                i=0
                grup01112=[]
                while i < len(grup112):
                    if grup01[i] == grup112[i]:
                        grup01112.append(grup01[i])
                    else:
                        grup01112.append("-")
                    i+=1
            else:
                grup01112=[]

        else:
            grup0110=[]
            grup0111=[]
            grup0112=[]
            grup0113=[]
            grup0114=[]
            grup0115=[]
            grup0116=[]
            grup0117=[]
            grup0118=[]
            grup0119=[]
            grup01110=[]
            grup01111=[]
            grup01112=[]

        #sifirin ikisi ---------------------------------
        if grup02 != []:
            if grup10 != []:
                i=0
                grup0210=[]
                while i < len(grup10):
                    if grup02[i] == grup10[i]:
                        grup0210.append(grup02[i])
                    else:
                        grup0210.append("-")
                    i+=1
            else:
                grup0210=[]

            if grup11 != []:
                i=0
                grup0211=[]
                while i < len(grup11):
                    if grup02[i] == grup11[i]:
                        grup0211.append(grup02[i])
                    else:
                        grup0211.append("-")
                    i+=1
            else:
                grup0211=[]

            if grup12 != []:
                i=0
                grup0212=[]
                while i < len(grup12):
                    if grup02[i] == grup12[i]:
                        grup0212.append(grup02[i])
                    else:
                        grup0212.append("-")
                    i+=1
            else:
                grup0212=[]

            if grup13 != []:
                i=0
                grup0213=[]
                while i < len(grup13):
                    if grup02[i] == grup13[i]:
                        grup0213.append(grup02[i])
                    else:
                        grup0213.append("-")
                    i+=1
            else:
                grup0213=[]

            if grup14 != []:
                i=0
                grup0214=[]
                while i < len(grup14):
                    if grup02[i] == grup14[i]:
                        grup0214.append(grup02[i])
                    else:
                        grup0214.append("-")
                    i+=1
            else:
                grup0214=[]

            if grup15 != []:
                i=0
                grup0215=[]
                while i < len(grup15):
                    if grup02[i] == grup15[i]:
                        grup0215.append(grup02[i])
                    else:
                        grup0215.append("-")
                    i+=1
            else:
                grup0215=[]

            if grup16 != []:
                i=0
                grup0216=[]
                while i < len(grup16):
                    if grup02[i] == grup16[i]:
                        grup0216.append(grup02[i])
                    else:
                        grup0216.append("-")
                    i+=1
            else:
                grup0216=[]

            if grup17 != []:
                i=0
                grup0217=[]
                while i < len(grup17):
                    if grup02[i] == grup17[i]:
                        grup0217.append(grup02[i])
                    else:
                        grup0217.append("-")
                    i+=1
            else:
                grup0217=[]

            if grup18 != []:
                i=0
                grup0218=[]
                while i < len(grup18):
                    if grup02[i] == grup18[i]:
                        grup0218.append(grup02[i])
                    else:
                        grup0218.append("-")
                    i+=1
            else:
                grup0218=[]

            if grup19 != []:
                i=0
                grup0219=[]
                while i < len(grup19):
                    if grup02[i] == grup19[i]:
                        grup0219.append(grup02[i])
                    else:
                        grup0219.append("-")
                    i+=1
            else:
                grup0219=[]

            if grup110 != []:
                i=0
                grup02110=[]
                while i < len(grup110):
                    if grup02[i] == grup110[i]:
                        grup02110.append(grup02[i])
                    else:
                        grup02110.append("-")
                    i+=1
            else:
                grup02110=[]

            if grup111 != []:
                i=0
                grup02111=[]
                while i < len(grup111):
                    if grup02[i] == grup111[i]:
                        grup02111.append(grup02[i])
                    else:
                        grup02111.append("-")
                    i+=1
            else:
                grup02111=[]

            if grup112 != []:
                i=0
                grup02112=[]
                while i < len(grup112):
                    if grup02[i] == grup112[i]:
                        grup02112.append(grup02[i])
                    else:
                        grup02112.append("-")
                    i+=1
            else:
                grup02112=[]

        else:
            grup0210=[]
            grup0211=[]
            grup0212=[]
            grup0213=[]
            grup0214=[]
            grup0215=[]
            grup0216=[]
            grup0217=[]
            grup0218=[]
            grup0219=[]
            grup02110=[]
            grup02111=[]
            grup02112=[]

        #sifirin ucu ---------------------------------
        if grup03 != []:
            if grup10 != []:
                i=0
                grup0310=[]
                while i < len(grup10):
                    if grup03[i] == grup10[i]:
                        grup0310.append(grup03[i])
                    else:
                        grup0310.append("-")
                    i+=1
            else:
                grup0310=[]

            if grup11 != []:
                i=0
                grup0311=[]
                while i < len(grup11):
                    if grup03[i] == grup11[i]:
                        grup0311.append(grup03[i])
                    else:
                        grup0311.append("-")
                    i+=1
            else:
                grup0311=[]

            if grup12 != []:
                i=0
                grup0312=[]
                while i < len(grup12):
                    if grup03[i] == grup12[i]:
                        grup0312.append(grup03[i])
                    else:
                        grup0312.append("-")
                    i+=1
            else:
                grup0312=[]

            if grup13 != []:
                i=0
                grup0313=[]
                while i < len(grup13):
                    if grup03[i] == grup13[i]:
                        grup0313.append(grup03[i])
                    else:
                        grup0313.append("-")
                    i+=1
            else:
                grup0313=[]

            if grup14 != []:
                i=0
                grup0314=[]
                while i < len(grup14):
                    if grup03[i] == grup14[i]:
                        grup0314.append(grup03[i])
                    else:
                        grup0314.append("-")
                    i+=1
            else:
                grup0314=[]

            if grup15 != []:
                i=0
                grup0315=[]
                while i < len(grup15):
                    if grup03[i] == grup15[i]:
                        grup0315.append(grup03[i])
                    else:
                        grup0315.append("-")
                    i+=1
            else:
                grup0315=[]

            if grup16 != []:
                i=0
                grup0316=[]
                while i < len(grup16):
                    if grup03[i] == grup16[i]:
                        grup0316.append(grup03[i])
                    else:
                        grup0316.append("-")
                    i+=1
            else:
                grup0316=[]

            if grup17 != []:
                i=0
                grup0317=[]
                while i < len(grup17):
                    if grup03[i] == grup17[i]:
                        grup0317.append(grup03[i])
                    else:
                        grup0317.append("-")
                    i+=1
            else:
                grup0317=[]

            if grup18 != []:
                i=0
                grup0318=[]
                while i < len(grup18):
                    if grup03[i] == grup18[i]:
                        grup0318.append(grup03[i])
                    else:
                        grup0318.append("-")
                    i+=1
            else:
                grup0318=[]

            if grup19 != []:
                i=0
                grup0319=[]
                while i < len(grup19):
                    if grup03[i] == grup19[i]:
                        grup0319.append(grup03[i])
                    else:
                        grup0319.append("-")
                    i+=1
            else:
                grup0319=[]

            if grup110 != []:
                i=0
                grup03110=[]
                while i < len(grup110):
                    if grup03[i] == grup110[i]:
                        grup03110.append(grup03[i])
                    else:
                        grup03110.append("-")
                    i+=1
            else:
                grup03110=[]

            if grup111 != []:
                i=0
                grup03111=[]
                while i < len(grup111):
                    if grup03[i] == grup111[i]:
                        grup03111.append(grup03[i])
                    else:
                        grup03111.append("-")
                    i+=1
            else:
                grup03111=[]

            if grup112 != []:
                i=0
                grup03112=[]
                while i < len(grup112):
                    if grup03[i] == grup112[i]:
                        grup03112.append(grup03[i])
                    else:
                        grup03112.append("-")
                    i+=1
            else:
                grup03112=[]

        else:
            grup0310=[]
            grup0311=[]
            grup0312=[]
            grup0313=[]
            grup0314=[]
            grup0315=[]
            grup0316=[]
            grup0317=[]
            grup0318=[]
            grup0319=[]
            grup03110=[]
            grup03111=[]
            grup03112=[]

        #birin sifiri ---------------------------------------------
        if grup10 != []:
            if grup20 != []:
                i=0
                grup1020=[]
                while i < len(grup10):
                    if grup10[i] == grup20[i]:
                        grup1020.append(grup10[i])
                    else:
                        grup1020.append("-")
                    i+=1
            else:
                grup1020=[]

            if grup21 != []:
                i=0
                grup1021=[]
                while i < len(grup10):
                    if grup10[i] == grup21[i]:
                        grup1021.append(grup10[i])
                    else:
                        grup1021.append("-")
                    i+=1
            else:
                grup1021=[]

            if grup22 != []:
                i=0
                grup1022=[]
                while i < len(grup10):
                    if grup10[i] == grup22[i]:
                        grup1022.append(grup10[i])
                    else:
                        grup1022.append("-")
                    i+=1
            else:
                grup1022=[]

            if grup23 != []:
                i=0
                grup1023=[]
                while i < len(grup10):
                    if grup10[i] == grup23[i]:
                        grup1023.append(grup10[i])
                    else:
                        grup1023.append("-")
                    i+=1
            else:
                grup1023=[]

            if grup24 != []:
                i=0
                grup1024=[]
                while i < len(grup10):
                    if grup10[i] == grup24[i]:
                        grup1024.append(grup10[i])
                    else:
                        grup1024.append("-")
                    i+=1
            else:
                grup1024=[]

            if grup25 != []:
                i=0
                grup1025=[]
                while i < len(grup10):
                    if grup10[i] == grup25[i]:
                        grup1025.append(grup10[i])
                    else:
                        grup1025.append("-")
                    i+=1
            else:
                grup1025=[]

            if grup26 != []:
                i=0
                grup1026=[]
                while i < len(grup10):
                    if grup10[i] == grup26[i]:
                        grup1026.append(grup10[i])
                    else:
                        grup1026.append("-")
                    i+=1
            else:
                grup1026=[]

            if grup27 != []:
                i=0
                grup1027=[]
                while i < len(grup10):
                    if grup10[i] == grup27[i]:
                        grup1027.append(grup10[i])
                    else:
                        grup1027.append("-")
                    i+=1
            else:
                grup1027=[]

            if grup28 != []:
                i=0
                grup1028=[]
                while i < len(grup10):
                    if grup10[i] == grup28[i]:
                        grup1028.append(grup10[i])
                    else:
                        grup1028.append("-")
                    i+=1
            else:
                grup1028=[]

            if grup29 != []:
                i=0
                grup1029=[]
                while i < len(grup10):
                    if grup10[i] == grup29[i]:
                        grup1029.append(grup10[i])
                    else:
                        grup1029.append("-")
                    i+=1
            else:
                grup1029=[]

            if grup210 != []:
                i=0
                grup10210=[]
                while i < len(grup10):
                    if grup10[i] == grup210[i]:
                        grup10210.append(grup10[i])
                    else:
                        grup10210.append("-")
                    i+=1
            else:
                grup10210=[]

            if grup211 != []:
                i=0
                grup10211=[]
                while i < len(grup10):
                    if grup10[i] == grup211[i]:
                        grup10211.append(grup10[i])
                    else:
                        grup10211.append("-")
                    i+=1
            else:
                grup10211=[]

        else:
            grup1020=[]
            grup1021=[]
            grup1022=[]
            grup1023=[]
            grup1024=[]
            grup1025=[]
            grup1026=[]
            grup1027=[]
            grup1028=[]
            grup1029=[]
            grup10210=[]
            grup10211=[]

        #birin biri ---------------------------------------------
        if grup11 != []:
            if grup20 != []:
                i=0
                grup1120=[]
                while i < len(grup11):
                    if grup11[i] == grup20[i]:
                        grup1120.append(grup11[i])
                    else:
                        grup1120.append("-")
                    i+=1
            else:
                grup1120=[]

            if grup21 != []:
                i=0
                grup1121=[]
                while i < len(grup11):
                    if grup11[i] == grup21[i]:
                        grup1121.append(grup11[i])
                    else:
                        grup1121.append("-")
                    i+=1
            else:
                grup1121=[]

            if grup22 != []:
                i=0
                grup1122=[]
                while i < len(grup11):
                    if grup11[i] == grup22[i]:
                        grup1122.append(grup11[i])
                    else:
                        grup1122.append("-")
                    i+=1
            else:
                grup1122=[]

            if grup23 != []:
                i=0
                grup1123=[]
                while i < len(grup11):
                    if grup11[i] == grup23[i]:
                        grup1123.append(grup11[i])
                    else:
                        grup1123.append("-")
                    i+=1
            else:
                grup1123=[]

            if grup24 != []:
                i=0
                grup1124=[]
                while i < len(grup11):
                    if grup11[i] == grup24[i]:
                        grup1124.append(grup11[i])
                    else:
                        grup1124.append("-")
                    i+=1
            else:
                grup1124=[]

            if grup25 != []:
                i=0
                grup1125=[]
                while i < len(grup11):
                    if grup11[i] == grup25[i]:
                        grup1125.append(grup11[i])
                    else:
                        grup1125.append("-")
                    i+=1
            else:
                grup1125=[]

            if grup26 != []:
                i=0
                grup1126=[]
                while i < len(grup11):
                    if grup11[i] == grup26[i]:
                        grup1126.append(grup11[i])
                    else:
                        grup1126.append("-")
                    i+=1
            else:
                grup1126=[]

            if grup27 != []:
                i=0
                grup1127=[]
                while i < len(grup11):
                    if grup11[i] == grup27[i]:
                        grup1127.append(grup11[i])
                    else:
                        grup1127.append("-")
                    i+=1
            else:
                grup1127=[]

            if grup28 != []:
                i=0
                grup1128=[]
                while i < len(grup11):
                    if grup11[i] == grup28[i]:
                        grup1128.append(grup11[i])
                    else:
                        grup1128.append("-")
                    i+=1
            else:
                grup1128=[]

            if grup29 != []:
                i=0
                grup1129=[]
                while i < len(grup11):
                    if grup11[i] == grup29[i]:
                        grup1129.append(grup11[i])
                    else:
                        grup1129.append("-")
                    i+=1
            else:
                grup1129=[]

            if grup210 != []:
                i=0
                grup11210=[]
                while i < len(grup11):
                    if grup11[i] == grup210[i]:
                        grup11210.append(grup11[i])
                    else:
                        grup11210.append("-")
                    i+=1
            else:
                grup11210=[]

            if grup211 != []:
                i=0
                grup11211=[]
                while i < len(grup11):
                    if grup11[i] == grup211[i]:
                        grup11211.append(grup11[i])
                    else:
                        grup11211.append("-")
                    i+=1
            else:
                grup11211=[]

        else:
            grup1120=[]
            grup1121=[]
            grup1122=[]
            grup1123=[]
            grup1124=[]
            grup1125=[]
            grup1126=[]
            grup1127=[]
            grup1128=[]
            grup1129=[]
            grup11210=[]
            grup11211=[]

        #birin ikisi ---------------------------------------------
        if grup12 != []:
            if grup20 != []:
                i=0
                grup1220=[]
                while i < len(grup12):
                    if grup12[i] == grup20[i]:
                        grup1220.append(grup12[i])
                    else:
                        grup1220.append("-")
                    i+=1
            else:
                grup1220=[]

            if grup21 != []:
                i=0
                grup1221=[]
                while i < len(grup12):
                    if grup12[i] == grup21[i]:
                        grup1221.append(grup12[i])
                    else:
                        grup1221.append("-")
                    i+=1
            else:
                grup1221=[]

            if grup22 != []:
                i=0
                grup1222=[]
                while i < len(grup12):
                    if grup12[i] == grup22[i]:
                        grup1222.append(grup12[i])
                    else:
                        grup1222.append("-")
                    i+=1
            else:
                grup1222=[]

            if grup23 != []:
                i=0
                grup1223=[]
                while i < len(grup12):
                    if grup12[i] == grup23[i]:
                        grup1223.append(grup12[i])
                    else:
                        grup1223.append("-")
                    i+=1
            else:
                grup1223=[]

            if grup24 != []:
                i=0
                grup1224=[]
                while i < len(grup12):
                    if grup12[i] == grup24[i]:
                        grup1224.append(grup12[i])
                    else:
                        grup1224.append("-")
                    i+=1
            else:
                grup1224=[]

            if grup25 != []:
                i=0
                grup1225=[]
                while i < len(grup12):
                    if grup12[i] == grup25[i]:
                        grup1225.append(grup12[i])
                    else:
                        grup1225.append("-")
                    i+=1
            else:
                grup1225=[]

            if grup26 != []:
                i=0
                grup1226=[]
                while i < len(grup12):
                    if grup12[i] == grup26[i]:
                        grup1226.append(grup12[i])
                    else:
                        grup1226.append("-")
                    i+=1
            else:
                grup1226=[]

            if grup27 != []:
                i=0
                grup1227=[]
                while i < len(grup12):
                    if grup12[i] == grup27[i]:
                        grup1227.append(grup12[i])
                    else:
                        grup1227.append("-")
                    i+=1
            else:
                grup1227=[]

            if grup28 != []:
                i=0
                grup1228=[]
                while i < len(grup12):
                    if grup12[i] == grup28[i]:
                        grup1228.append(grup12[i])
                    else:
                        grup1228.append("-")
                    i+=1
            else:
                grup1228=[]

            if grup29 != []:
                i=0
                grup1229=[]
                while i < len(grup12):
                    if grup12[i] == grup29[i]:
                        grup1229.append(grup12[i])
                    else:
                        grup1229.append("-")
                    i+=1
            else:
                grup1229=[]

            if grup210 != []:
                i=0
                grup12210=[]
                while i < len(grup12):
                    if grup12[i] == grup210[i]:
                        grup12210.append(grup12[i])
                    else:
                        grup12210.append("-")
                    i+=1
            else:
                grup12210=[]

            if grup211 != []:
                i=0
                grup12211=[]
                while i < len(grup12):
                    if grup12[i] == grup211[i]:
                        grup12211.append(grup12[i])
                    else:
                        grup12211.append("-")
                    i+=1
            else:
                grup12211=[]

        else:
            grup1220=[]
            grup1221=[]
            grup1222=[]
            grup1223=[]
            grup1224=[]
            grup1225=[]
            grup1226=[]
            grup1227=[]
            grup1228=[]
            grup1229=[]
            grup12210=[]
            grup12211=[]

        #birin ucu ---------------------------------------------
        if grup13 != []:
            if grup20 != []:
                i=0
                grup1320=[]
                while i < len(grup13):
                    if grup13[i] == grup20[i]:
                        grup1320.append(grup13[i])
                    else:
                        grup1320.append("-")
                    i+=1
            else:
                grup1320=[]

            if grup21 != []:
                i=0
                grup1321=[]
                while i < len(grup13):
                    if grup13[i] == grup21[i]:
                        grup1321.append(grup13[i])
                    else:
                        grup1321.append("-")
                    i+=1
            else:
                grup1321=[]

            if grup22 != []:
                i=0
                grup1322=[]
                while i < len(grup13):
                    if grup13[i] == grup22[i]:
                        grup1322.append(grup13[i])
                    else:
                        grup1322.append("-")
                    i+=1
            else:
                grup1322=[]

            if grup23 != []:
                i=0
                grup1323=[]
                while i < len(grup13):
                    if grup13[i] == grup23[i]:
                        grup1323.append(grup13[i])
                    else:
                        grup1323.append("-")
                    i+=1
            else:
                grup1323=[]

            if grup24 != []:
                i=0
                grup1324=[]
                while i < len(grup13):
                    if grup13[i] == grup24[i]:
                        grup1324.append(grup13[i])
                    else:
                        grup1324.append("-")
                    i+=1
            else:
                grup1324=[]

            if grup25 != []:
                i=0
                grup1325=[]
                while i < len(grup13):
                    if grup13[i] == grup25[i]:
                        grup1325.append(grup13[i])
                    else:
                        grup1325.append("-")
                    i+=1
            else:
                grup1325=[]

            if grup26 != []:
                i=0
                grup1326=[]
                while i < len(grup13):
                    if grup13[i] == grup26[i]:
                        grup1326.append(grup13[i])
                    else:
                        grup1326.append("-")
                    i+=1
            else:
                grup1326=[]

            if grup27 != []:
                i=0
                grup1327=[]
                while i < len(grup13):
                    if grup13[i] == grup27[i]:
                        grup1327.append(grup13[i])
                    else:
                        grup1327.append("-")
                    i+=1
            else:
                grup1327=[]

            if grup28 != []:
                i=0
                grup1328=[]
                while i < len(grup13):
                    if grup13[i] == grup28[i]:
                        grup1328.append(grup13[i])
                    else:
                        grup1328.append("-")
                    i+=1
            else:
                grup1328=[]

            if grup29 != []:
                i=0
                grup1329=[]
                while i < len(grup13):
                    if grup13[i] == grup29[i]:
                        grup1329.append(grup13[i])
                    else:
                        grup1329.append("-")
                    i+=1
            else:
                grup1329=[]

            if grup210 != []:
                i=0
                grup13210=[]
                while i < len(grup13):
                    if grup13[i] == grup210[i]:
                        grup13210.append(grup13[i])
                    else:
                        grup13210.append("-")
                    i+=1
            else:
                grup13210=[]

            if grup211 != []:
                i=0
                grup13211=[]
                while i < len(grup13):
                    if grup13[i] == grup211[i]:
                        grup13211.append(grup13[i])
                    else:
                        grup13211.append("-")
                    i+=1
            else:
                grup13211=[]

        else:
            grup1320=[]
            grup1321=[]
            grup1322=[]
            grup1323=[]
            grup1324=[]
            grup1325=[]
            grup1326=[]
            grup1327=[]
            grup1328=[]
            grup1329=[]
            grup13210=[]
            grup13211=[]

        #birin dordu ---------------------------------------------
        if grup14 != []:
            if grup20 != []:
                i=0
                grup1420=[]
                while i < len(grup14):
                    if grup14[i] == grup20[i]:
                        grup1420.append(grup14[i])
                    else:
                        grup1420.append("-")
                    i+=1
            else:
                grup1420=[]

            if grup21 != []:
                i=0
                grup1421=[]
                while i < len(grup14):
                    if grup14[i] == grup21[i]:
                        grup1421.append(grup14[i])
                    else:
                        grup1421.append("-")
                    i+=1
            else:
                grup1421=[]

            if grup22 != []:
                i=0
                grup1422=[]
                while i < len(grup14):
                    if grup14[i] == grup22[i]:
                        grup1422.append(grup14[i])
                    else:
                        grup1422.append("-")
                    i+=1
            else:
                grup1422=[]

            if grup23 != []:
                i=0
                grup1423=[]
                while i < len(grup14):
                    if grup14[i] == grup23[i]:
                        grup1423.append(grup14[i])
                    else:
                        grup1423.append("-")
                    i+=1
            else:
                grup1423=[]

            if grup24 != []:
                i=0
                grup1424=[]
                while i < len(grup14):
                    if grup14[i] == grup24[i]:
                        grup1424.append(grup14[i])
                    else:
                        grup1424.append("-")
                    i+=1
            else:
                grup1424=[]

            if grup25 != []:
                i=0
                grup1425=[]
                while i < len(grup14):
                    if grup14[i] == grup25[i]:
                        grup1425.append(grup14[i])
                    else:
                        grup1425.append("-")
                    i+=1
            else:
                grup1425=[]

            if grup26 != []:
                i=0
                grup1426=[]
                while i < len(grup14):
                    if grup14[i] == grup26[i]:
                        grup1426.append(grup14[i])
                    else:
                        grup1426.append("-")
                    i+=1
            else:
                grup1426=[]

            if grup27 != []:
                i=0
                grup1427=[]
                while i < len(grup14):
                    if grup14[i] == grup27[i]:
                        grup1427.append(grup14[i])
                    else:
                        grup1427.append("-")
                    i+=1
            else:
                grup1427=[]

            if grup28 != []:
                i=0
                grup1428=[]
                while i < len(grup14):
                    if grup14[i] == grup28[i]:
                        grup1428.append(grup14[i])
                    else:
                        grup1428.append("-")
                    i+=1
            else:
                grup1428=[]

            if grup29 != []:
                i=0
                grup1429=[]
                while i < len(grup14):
                    if grup14[i] == grup29[i]:
                        grup1429.append(grup14[i])
                    else:
                        grup1429.append("-")
                    i+=1
            else:
                grup1429=[]

            if grup210 != []:
                i=0
                grup14210=[]
                while i < len(grup14):
                    if grup14[i] == grup210[i]:
                        grup14210.append(grup14[i])
                    else:
                        grup14210.append("-")
                    i+=1
            else:
                grup14210=[]

            if grup211 != []:
                i=0
                grup14211=[]
                while i < len(grup14):
                    if grup14[i] == grup211[i]:
                        grup14211.append(grup14[i])
                    else:
                        grup14211.append("-")
                    i+=1
            else:
                grup14211=[]

        else:
            grup1420=[]
            grup1421=[]
            grup1422=[]
            grup1423=[]
            grup1424=[]
            grup1425=[]
            grup1426=[]
            grup1427=[]
            grup1428=[]
            grup1429=[]
            grup14210=[]
            grup14211=[]

        #birin besi ---------------------------------------------
        if grup15 != []:
            if grup20 != []:
                i=0
                grup1520=[]
                while i < len(grup15):
                    if grup15[i] == grup20[i]:
                        grup1520.append(grup15[i])
                    else:
                        grup1520.append("-")
                    i+=1
            else:
                grup1520=[]

            if grup21 != []:
                i=0
                grup1521=[]
                while i < len(grup15):
                    if grup15[i] == grup21[i]:
                        grup1521.append(grup15[i])
                    else:
                        grup1521.append("-")
                    i+=1
            else:
                grup1521=[]

            if grup22 != []:
                i=0
                grup1522=[]
                while i < len(grup15):
                    if grup15[i] == grup22[i]:
                        grup1522.append(grup15[i])
                    else:
                        grup1522.append("-")
                    i+=1
            else:
                grup1522=[]

            if grup23 != []:
                i=0
                grup1523=[]
                while i < len(grup15):
                    if grup15[i] == grup23[i]:
                        grup1523.append(grup15[i])
                    else:
                        grup1523.append("-")
                    i+=1
            else:
                grup1523=[]

            if grup24 != []:
                i=0
                grup1524=[]
                while i < len(grup15):
                    if grup15[i] == grup24[i]:
                        grup1524.append(grup15[i])
                    else:
                        grup1524.append("-")
                    i+=1
            else:
                grup1524=[]

            if grup25 != []:
                i=0
                grup1525=[]
                while i < len(grup15):
                    if grup15[i] == grup25[i]:
                        grup1525.append(grup15[i])
                    else:
                        grup1525.append("-")
                    i+=1
            else:
                grup1525=[]

            if grup26 != []:
                i=0
                grup1526=[]
                while i < len(grup15):
                    if grup15[i] == grup26[i]:
                        grup1526.append(grup15[i])
                    else:
                        grup1526.append("-")
                    i+=1
            else:
                grup1526=[]

            if grup27 != []:
                i=0
                grup1527=[]
                while i < len(grup15):
                    if grup15[i] == grup27[i]:
                        grup1527.append(grup15[i])
                    else:
                        grup1527.append("-")
                    i+=1
            else:
                grup1527=[]

            if grup28 != []:
                i=0
                grup1528=[]
                while i < len(grup15):
                    if grup15[i] == grup28[i]:
                        grup1528.append(grup15[i])
                    else:
                        grup1528.append("-")
                    i+=1
            else:
                grup1528=[]

            if grup29 != []:
                i=0
                grup1529=[]
                while i < len(grup15):
                    if grup15[i] == grup29[i]:
                        grup1529.append(grup15[i])
                    else:
                        grup1529.append("-")
                    i+=1
            else:
                grup1529=[]

            if grup210 != []:
                i=0
                grup15210=[]
                while i < len(grup15):
                    if grup15[i] == grup210[i]:
                        grup15210.append(grup15[i])
                    else:
                        grup15210.append("-")
                    i+=1
            else:
                grup15210=[]

            if grup211 != []:
                i=0
                grup15211=[]
                while i < len(grup15):
                    if grup15[i] == grup211[i]:
                        grup15211.append(grup15[i])
                    else:
                        grup15211.append("-")
                    i+=1
            else:
                grup15211=[]

        else:
            grup1520=[]
            grup1521=[]
            grup1522=[]
            grup1523=[]
            grup1524=[]
            grup1525=[]
            grup1526=[]
            grup1527=[]
            grup1528=[]
            grup1529=[]
            grup15210=[]
            grup15211=[]

        #birin altisi ---------------------------------------------
        if grup16 != []:
            if grup20 != []:
                i=0
                grup1620=[]
                while i < len(grup16):
                    if grup16[i] == grup20[i]:
                        grup1620.append(grup16[i])
                    else:
                        grup1620.append("-")
                    i+=1
            else:
                grup1620=[]

            if grup21 != []:
                i=0
                grup1621=[]
                while i < len(grup16):
                    if grup16[i] == grup21[i]:
                        grup1621.append(grup16[i])
                    else:
                        grup1621.append("-")
                    i+=1
            else:
                grup1621=[]

            if grup22 != []:
                i=0
                grup1622=[]
                while i < len(grup16):
                    if grup16[i] == grup22[i]:
                        grup1622.append(grup16[i])
                    else:
                        grup1622.append("-")
                    i+=1
            else:
                grup1622=[]

            if grup23 != []:
                i=0
                grup1623=[]
                while i < len(grup16):
                    if grup16[i] == grup23[i]:
                        grup1623.append(grup16[i])
                    else:
                        grup1623.append("-")
                    i+=1
            else:
                grup1623=[]

            if grup24 != []:
                i=0
                grup1624=[]
                while i < len(grup16):
                    if grup16[i] == grup24[i]:
                        grup1624.append(grup16[i])
                    else:
                        grup1624.append("-")
                    i+=1
            else:
                grup1624=[]

            if grup25 != []:
                i=0
                grup1625=[]
                while i < len(grup16):
                    if grup16[i] == grup25[i]:
                        grup1625.append(grup16[i])
                    else:
                        grup1625.append("-")
                    i+=1
            else:
                grup1625=[]

            if grup26 != []:
                i=0
                grup1626=[]
                while i < len(grup16):
                    if grup16[i] == grup26[i]:
                        grup1626.append(grup16[i])
                    else:
                        grup1626.append("-")
                    i+=1
            else:
                grup1626=[]

            if grup27 != []:
                i=0
                grup1627=[]
                while i < len(grup16):
                    if grup16[i] == grup27[i]:
                        grup1627.append(grup16[i])
                    else:
                        grup1627.append("-")
                    i+=1
            else:
                grup1627=[]

            if grup28 != []:
                i=0
                grup1628=[]
                while i < len(grup16):
                    if grup16[i] == grup28[i]:
                        grup1628.append(grup16[i])
                    else:
                        grup1628.append("-")
                    i+=1
            else:
                grup1628=[]

            if grup29 != []:
                i=0
                grup1629=[]
                while i < len(grup16):
                    if grup16[i] == grup29[i]:
                        grup1629.append(grup16[i])
                    else:
                        grup1629.append("-")
                    i+=1
            else:
                grup1629=[]

            if grup210 != []:
                i=0
                grup16210=[]
                while i < len(grup16):
                    if grup16[i] == grup210[i]:
                        grup16210.append(grup16[i])
                    else:
                        grup16210.append("-")
                    i+=1
            else:
                grup16210=[]

            if grup211 != []:
                i=0
                grup16211=[]
                while i < len(grup16):
                    if grup16[i] == grup211[i]:
                        grup16211.append(grup16[i])
                    else:
                        grup16211.append("-")
                    i+=1
            else:
                grup16211=[]

        else:
            grup1620=[]
            grup1621=[]
            grup1622=[]
            grup1623=[]
            grup1624=[]
            grup1625=[]
            grup1626=[]
            grup1627=[]
            grup1628=[]
            grup1629=[]
            grup16210=[]
            grup16211=[]

        #birin yedisi ---------------------------------------------
        if grup17 != []:
            if grup20 != []:
                i=0
                grup1720=[]
                while i < len(grup17):
                    if grup17[i] == grup20[i]:
                        grup1720.append(grup17[i])
                    else:
                        grup1720.append("-")
                    i+=1
            else:
                grup1720=[]

            if grup21 != []:
                i=0
                grup1721=[]
                while i < len(grup17):
                    if grup17[i] == grup21[i]:
                        grup1721.append(grup17[i])
                    else:
                        grup1721.append("-")
                    i+=1
            else:
                grup1721=[]

            if grup22 != []:
                i=0
                grup1722=[]
                while i < len(grup17):
                    if grup17[i] == grup22[i]:
                        grup1722.append(grup17[i])
                    else:
                        grup1722.append("-")
                    i+=1
            else:
                grup1722=[]

            if grup23 != []:
                i=0
                grup1723=[]
                while i < len(grup17):
                    if grup17[i] == grup23[i]:
                        grup1723.append(grup17[i])
                    else:
                        grup1723.append("-")
                    i+=1
            else:
                grup1723=[]

            if grup24 != []:
                i=0
                grup1724=[]
                while i < len(grup17):
                    if grup17[i] == grup24[i]:
                        grup1724.append(grup17[i])
                    else:
                        grup1724.append("-")
                    i+=1
            else:
                grup1724=[]

            if grup25 != []:
                i=0
                grup1725=[]
                while i < len(grup17):
                    if grup17[i] == grup25[i]:
                        grup1725.append(grup17[i])
                    else:
                        grup1725.append("-")
                    i+=1
            else:
                grup1725=[]

            if grup26 != []:
                i=0
                grup1726=[]
                while i < len(grup17):
                    if grup17[i] == grup26[i]:
                        grup1726.append(grup17[i])
                    else:
                        grup1726.append("-")
                    i+=1
            else:
                grup1726=[]

            if grup27 != []:
                i=0
                grup1727=[]
                while i < len(grup17):
                    if grup17[i] == grup27[i]:
                        grup1727.append(grup17[i])
                    else:
                        grup1727.append("-")
                    i+=1
            else:
                grup1727=[]

            if grup28 != []:
                i=0
                grup1728=[]
                while i < len(grup17):
                    if grup17[i] == grup28[i]:
                        grup1728.append(grup17[i])
                    else:
                        grup1728.append("-")
                    i+=1
            else:
                grup1728=[]

            if grup29 != []:
                i=0
                grup1729=[]
                while i < len(grup17):
                    if grup17[i] == grup29[i]:
                        grup1729.append(grup17[i])
                    else:
                        grup1729.append("-")
                    i+=1
            else:
                grup1729=[]

            if grup210 != []:
                i=0
                grup17210=[]
                while i < len(grup17):
                    if grup17[i] == grup210[i]:
                        grup17210.append(grup17[i])
                    else:
                        grup17210.append("-")
                    i+=1
            else:
                grup17210=[]

            if grup211 != []:
                i=0
                grup17211=[]
                while i < len(grup17):
                    if grup17[i] == grup211[i]:
                        grup17211.append(grup17[i])
                    else:
                        grup17211.append("-")
                    i+=1
            else:
                grup17211=[]

        else:
            grup1720=[]
            grup1721=[]
            grup1722=[]
            grup1723=[]
            grup1724=[]
            grup1725=[]
            grup1726=[]
            grup1727=[]
            grup1728=[]
            grup1729=[]
            grup17210=[]
            grup17211=[]

        #birin sekizi ---------------------------------------------
        if grup18 != []:
            if grup20 != []:
                i=0
                grup1820=[]
                while i < len(grup18):
                    if grup18[i] == grup20[i]:
                        grup1820.append(grup18[i])
                    else:
                        grup1820.append("-")
                    i+=1
            else:
                grup1820=[]

            if grup21 != []:
                i=0
                grup1821=[]
                while i < len(grup18):
                    if grup18[i] == grup21[i]:
                        grup1821.append(grup18[i])
                    else:
                        grup1821.append("-")
                    i+=1
            else:
                grup1821=[]

            if grup22 != []:
                i=0
                grup1822=[]
                while i < len(grup18):
                    if grup18[i] == grup22[i]:
                        grup1822.append(grup18[i])
                    else:
                        grup1822.append("-")
                    i+=1
            else:
                grup1822=[]

            if grup23 != []:
                i=0
                grup1823=[]
                while i < len(grup18):
                    if grup18[i] == grup23[i]:
                        grup1823.append(grup18[i])
                    else:
                        grup1823.append("-")
                    i+=1
            else:
                grup1823=[]

            if grup24 != []:
                i=0
                grup1824=[]
                while i < len(grup18):
                    if grup18[i] == grup24[i]:
                        grup1824.append(grup18[i])
                    else:
                        grup1824.append("-")
                    i+=1
            else:
                grup1824=[]

            if grup25 != []:
                i=0
                grup1825=[]
                while i < len(grup18):
                    if grup18[i] == grup25[i]:
                        grup1825.append(grup18[i])
                    else:
                        grup1825.append("-")
                    i+=1
            else:
                grup1825=[]

            if grup26 != []:
                i=0
                grup1826=[]
                while i < len(grup18):
                    if grup18[i] == grup26[i]:
                        grup1826.append(grup18[i])
                    else:
                        grup1826.append("-")
                    i+=1
            else:
                grup1826=[]

            if grup27 != []:
                i=0
                grup1827=[]
                while i < len(grup18):
                    if grup18[i] == grup27[i]:
                        grup1827.append(grup18[i])
                    else:
                        grup1827.append("-")
                    i+=1
            else:
                grup1827=[]

            if grup28 != []:
                i=0
                grup1828=[]
                while i < len(grup18):
                    if grup18[i] == grup28[i]:
                        grup1828.append(grup18[i])
                    else:
                        grup1828.append("-")
                    i+=1
            else:
                grup1828=[]

            if grup29 != []:
                i=0
                grup1829=[]
                while i < len(grup18):
                    if grup18[i] == grup29[i]:
                        grup1829.append(grup18[i])
                    else:
                        grup1829.append("-")
                    i+=1
            else:
                grup1829=[]

            if grup210 != []:
                i=0
                grup18210=[]
                while i < len(grup18):
                    if grup18[i] == grup210[i]:
                        grup18210.append(grup18[i])
                    else:
                        grup18210.append("-")
                    i+=1
            else:
                grup18210=[]

            if grup211 != []:
                i=0
                grup18211=[]
                while i < len(grup18):
                    if grup18[i] == grup211[i]:
                        grup18211.append(grup18[i])
                    else:
                        grup18211.append("-")
                    i+=1
            else:
                grup18211=[]

        else:
            grup1820=[]
            grup1821=[]
            grup1822=[]
            grup1823=[]
            grup1824=[]
            grup1825=[]
            grup1826=[]
            grup1827=[]
            grup1828=[]
            grup1829=[]
            grup18210=[]
            grup18211=[]

        #birin dokuzu ---------------------------------------------
        if grup19 != []:
            if grup20 != []:
                i=0
                grup1920=[]
                while i < len(grup19):
                    if grup19[i] == grup20[i]:
                        grup1920.append(grup19[i])
                    else:
                        grup1920.append("-")
                    i+=1
            else:
                grup1920=[]

            if grup21 != []:
                i=0
                grup1921=[]
                while i < len(grup19):
                    if grup19[i] == grup21[i]:
                        grup1921.append(grup19[i])
                    else:
                        grup1921.append("-")
                    i+=1
            else:
                grup1921=[]

            if grup22 != []:
                i=0
                grup1922=[]
                while i < len(grup19):
                    if grup19[i] == grup22[i]:
                        grup1922.append(grup19[i])
                    else:
                        grup1922.append("-")
                    i+=1
            else:
                grup1922=[]

            if grup23 != []:
                i=0
                grup1923=[]
                while i < len(grup19):
                    if grup19[i] == grup23[i]:
                        grup1923.append(grup19[i])
                    else:
                        grup1923.append("-")
                    i+=1
            else:
                grup1923=[]

            if grup24 != []:
                i=0
                grup1924=[]
                while i < len(grup19):
                    if grup19[i] == grup24[i]:
                        grup1924.append(grup19[i])
                    else:
                        grup1924.append("-")
                    i+=1
            else:
                grup1924=[]

            if grup25 != []:
                i=0
                grup1925=[]
                while i < len(grup19):
                    if grup19[i] == grup25[i]:
                        grup1925.append(grup19[i])
                    else:
                        grup1925.append("-")
                    i+=1
            else:
                grup1925=[]

            if grup26 != []:
                i=0
                grup1926=[]
                while i < len(grup19):
                    if grup19[i] == grup26[i]:
                        grup1926.append(grup19[i])
                    else:
                        grup1926.append("-")
                    i+=1
            else:
                grup1926=[]

            if grup27 != []:
                i=0
                grup1927=[]
                while i < len(grup19):
                    if grup19[i] == grup27[i]:
                        grup1927.append(grup19[i])
                    else:
                        grup1927.append("-")
                    i+=1
            else:
                grup1927=[]

            if grup28 != []:
                i=0
                grup1928=[]
                while i < len(grup19):
                    if grup19[i] == grup28[i]:
                        grup1928.append(grup19[i])
                    else:
                        grup1928.append("-")
                    i+=1
            else:
                grup1928=[]

            if grup29 != []:
                i=0
                grup1929=[]
                while i < len(grup19):
                    if grup19[i] == grup29[i]:
                        grup1929.append(grup19[i])
                    else:
                        grup1929.append("-")
                    i+=1
            else:
                grup1929=[]

            if grup210 != []:
                i=0
                grup19210=[]
                while i < len(grup19):
                    if grup19[i] == grup210[i]:
                        grup19210.append(grup19[i])
                    else:
                        grup19210.append("-")
                    i+=1
            else:
                grup19210=[]

            if grup211 != []:
                i=0
                grup19211=[]
                while i < len(grup19):
                    if grup19[i] == grup211[i]:
                        grup19211.append(grup19[i])
                    else:
                        grup19211.append("-")
                    i+=1
            else:
                grup19211=[]

        else:
            grup1920=[]
            grup1921=[]
            grup1922=[]
            grup1923=[]
            grup1924=[]
            grup1925=[]
            grup1926=[]
            grup1927=[]
            grup1928=[]
            grup1929=[]
            grup19210=[]
            grup19211=[]

        #birin onu---------------------------------------------
        if grup110 != []:
            if grup20 != []:
                i=0
                grup11020=[]
                while i < len(grup110):
                    if grup110[i] == grup20[i]:
                        grup11020.append(grup110[i])
                    else:
                        grup11020.append("-")
                    i+=1
            else:
                grup11020=[]

            if grup21 != []:
                i=0
                grup11021=[]
                while i < len(grup110):
                    if grup110[i] == grup21[i]:
                        grup11021.append(grup110[i])
                    else:
                        grup11021.append("-")
                    i+=1
            else:
                grup11021=[]

            if grup22 != []:
                i=0
                grup11022=[]
                while i < len(grup110):
                    if grup110[i] == grup22[i]:
                        grup11022.append(grup110[i])
                    else:
                        grup11022.append("-")
                    i+=1
            else:
                grup11022=[]

            if grup23 != []:
                i=0
                grup11023=[]
                while i < len(grup110):
                    if grup110[i] == grup23[i]:
                        grup11023.append(grup110[i])
                    else:
                        grup11023.append("-")
                    i+=1
            else:
                grup11023=[]

            if grup24 != []:
                i=0
                grup11024=[]
                while i < len(grup110):
                    if grup110[i] == grup24[i]:
                        grup11024.append(grup110[i])
                    else:
                        grup11024.append("-")
                    i+=1
            else:
                grup11024=[]

            if grup25 != []:
                i=0
                grup11025=[]
                while i < len(grup110):
                    if grup110[i] == grup25[i]:
                        grup11025.append(grup110[i])
                    else:
                        grup11025.append("-")
                    i+=1
            else:
                grup11025=[]

            if grup26 != []:
                i=0
                grup11026=[]
                while i < len(grup110):
                    if grup110[i] == grup26[i]:
                        grup11026.append(grup110[i])
                    else:
                        grup11026.append("-")
                    i+=1
            else:
                grup11026=[]

            if grup27 != []:
                i=0
                grup11027=[]
                while i < len(grup110):
                    if grup110[i] == grup27[i]:
                        grup11027.append(grup110[i])
                    else:
                        grup11027.append("-")
                    i+=1
            else:
                grup11027=[]

            if grup28 != []:
                i=0
                grup11028=[]
                while i < len(grup110):
                    if grup110[i] == grup28[i]:
                        grup11028.append(grup110[i])
                    else:
                        grup11028.append("-")
                    i+=1
            else:
                grup11028=[]

            if grup29 != []:
                i=0
                grup11029=[]
                while i < len(grup110):
                    if grup110[i] == grup29[i]:
                        grup11029.append(grup110[i])
                    else:
                        grup11029.append("-")
                    i+=1
            else:
                grup11029=[]

            if grup210 != []:
                i=0
                grup110210=[]
                while i < len(grup110):
                    if grup110[i] == grup210[i]:
                        grup110210.append(grup110[i])
                    else:
                        grup110210.append("-")
                    i+=1
            else:
                grup110210=[]

            if grup211 != []:
                i=0
                grup110211=[]
                while i < len(grup110):
                    if grup110[i] == grup211[i]:
                        grup110211.append(grup110[i])
                    else:
                        grup110211.append("-")
                    i+=1
            else:
                grup110211=[]

        else:
            grup11020=[]
            grup11021=[]
            grup11022=[]
            grup11023=[]
            grup11024=[]
            grup11025=[]
            grup11026=[]
            grup11027=[]
            grup11028=[]
            grup11029=[]
            grup110210=[]
            grup110211=[]

        #birin onbiri---------------------------------------------
        if grup111 != []:
            if grup20 != []:
                i=0
                grup11120=[]
                while i < len(grup111):
                    if grup111[i] == grup20[i]:
                        grup11120.append(grup111[i])
                    else:
                        grup11120.append("-")
                    i+=1
            else:
                grup11120=[]

            if grup21 != []:
                i=0
                grup11121=[]
                while i < len(grup111):
                    if grup111[i] == grup21[i]:
                        grup11121.append(grup111[i])
                    else:
                        grup11121.append("-")
                    i+=1
            else:
                grup11121=[]

            if grup22 != []:
                i=0
                grup11122=[]
                while i < len(grup111):
                    if grup111[i] == grup22[i]:
                        grup11122.append(grup111[i])
                    else:
                        grup11122.append("-")
                    i+=1
            else:
                grup11122=[]

            if grup23 != []:
                i=0
                grup11123=[]
                while i < len(grup111):
                    if grup111[i] == grup23[i]:
                        grup11123.append(grup111[i])
                    else:
                        grup11123.append("-")
                    i+=1
            else:
                grup11123=[]

            if grup24 != []:
                i=0
                grup11124=[]
                while i < len(grup111):
                    if grup111[i] == grup24[i]:
                        grup11124.append(grup111[i])
                    else:
                        grup11124.append("-")
                    i+=1
            else:
                grup11124=[]

            if grup25 != []:
                i=0
                grup11125=[]
                while i < len(grup111):
                    if grup111[i] == grup25[i]:
                        grup11125.append(grup111[i])
                    else:
                        grup11125.append("-")
                    i+=1
            else:
                grup11125=[]

            if grup26 != []:
                i=0
                grup11126=[]
                while i < len(grup111):
                    if grup111[i] == grup26[i]:
                        grup11126.append(grup111[i])
                    else:
                        grup11126.append("-")
                    i+=1
            else:
                grup11126=[]

            if grup27 != []:
                i=0
                grup11127=[]
                while i < len(grup111):
                    if grup111[i] == grup27[i]:
                        grup11127.append(grup111[i])
                    else:
                        grup11127.append("-")
                    i+=1
            else:
                grup11127=[]

            if grup28 != []:
                i=0
                grup11128=[]
                while i < len(grup111):
                    if grup111[i] == grup28[i]:
                        grup11128.append(grup111[i])
                    else:
                        grup11128.append("-")
                    i+=1
            else:
                grup11128=[]

            if grup29 != []:
                i=0
                grup11129=[]
                while i < len(grup111):
                    if grup111[i] == grup29[i]:
                        grup11129.append(grup111[i])
                    else:
                        grup11129.append("-")
                    i+=1
            else:
                grup11129=[]

            if grup210 != []:
                i=0
                grup111210=[]
                while i < len(grup111):
                    if grup111[i] == grup210[i]:
                        grup111210.append(grup111[i])
                    else:
                        grup111210.append("-")
                    i+=1
            else:
                grup111210=[]

            if grup211 != []:
                i=0
                grup111211=[]
                while i < len(grup111):
                    if grup111[i] == grup211[i]:
                        grup111211.append(grup111[i])
                    else:
                        grup111211.append("-")
                    i+=1
            else:
                grup111211=[]

        else:
            grup11120=[]
            grup11121=[]
            grup11122=[]
            grup11123=[]
            grup11124=[]
            grup11125=[]
            grup11126=[]
            grup11127=[]
            grup11128=[]
            grup11129=[]
            grup111210=[]
            grup111211=[]

        #birin onikisi---------------------------------------------
        if grup112 != []:
            if grup20 != []:
                i=0
                grup11220=[]
                while i < len(grup112):
                    if grup112[i] == grup20[i]:
                        grup11220.append(grup112[i])
                    else:
                        grup11220.append("-")
                    i+=1
            else:
                grup11220=[]

            if grup21 != []:
                i=0
                grup11221=[]
                while i < len(grup112):
                    if grup112[i] == grup21[i]:
                        grup11221.append(grup112[i])
                    else:
                        grup11221.append("-")
                    i+=1
            else:
                grup11221=[]

            if grup22 != []:
                i=0
                grup11222=[]
                while i < len(grup112):
                    if grup112[i] == grup22[i]:
                        grup11222.append(grup112[i])
                    else:
                        grup11222.append("-")
                    i+=1
            else:
                grup11222=[]

            if grup23 != []:
                i=0
                grup11223=[]
                while i < len(grup112):
                    if grup112[i] == grup23[i]:
                        grup11223.append(grup112[i])
                    else:
                        grup11223.append("-")
                    i+=1
            else:
                grup11223=[]

            if grup24 != []:
                i=0
                grup11224=[]
                while i < len(grup112):
                    if grup112[i] == grup24[i]:
                        grup11224.append(grup112[i])
                    else:
                        grup11224.append("-")
                    i+=1
            else:
                grup11224=[]

            if grup25 != []:
                i=0
                grup11225=[]
                while i < len(grup112):
                    if grup112[i] == grup25[i]:
                        grup11225.append(grup112[i])
                    else:
                        grup11225.append("-")
                    i+=1
            else:
                grup11225=[]

            if grup26 != []:
                i=0
                grup11226=[]
                while i < len(grup112):
                    if grup112[i] == grup26[i]:
                        grup11226.append(grup112[i])
                    else:
                        grup11226.append("-")
                    i+=1
            else:
                grup11226=[]

            if grup27 != []:
                i=0
                grup11227=[]
                while i < len(grup112):
                    if grup112[i] == grup27[i]:
                        grup11227.append(grup112[i])
                    else:
                        grup11227.append("-")
                    i+=1
            else:
                grup11227=[]

            if grup28 != []:
                i=0
                grup11228=[]
                while i < len(grup112):
                    if grup112[i] == grup28[i]:
                        grup11228.append(grup112[i])
                    else:
                        grup11228.append("-")
                    i+=1
            else:
                grup11228=[]

            if grup29 != []:
                i=0
                grup11229=[]
                while i < len(grup112):
                    if grup112[i] == grup29[i]:
                        grup11229.append(grup112[i])
                    else:
                        grup11229.append("-")
                    i+=1
            else:
                grup11229=[]

            if grup210 != []:
                i=0
                grup112210=[]
                while i < len(grup112):
                    if grup112[i] == grup210[i]:
                        grup112210.append(grup112[i])
                    else:
                        grup112210.append("-")
                    i+=1
            else:
                grup112210=[]

            if grup211 != []:
                i=0
                grup112211=[]
                while i < len(grup112):
                    if grup112[i] == grup211[i]:
                        grup112211.append(grup112[i])
                    else:
                        grup112211.append("-")
                    i+=1
            else:
                grup112211=[]

        else:
            grup11220=[]
            grup11221=[]
            grup11222=[]
            grup11223=[]
            grup11224=[]
            grup11225=[]
            grup11226=[]
            grup11227=[]
            grup11228=[]
            grup11229=[]
            grup112210=[]
            grup112211=[]

        #ikinin sifiri ---------------------------------
        if grup20 != []:
            if grup30 != []:
                i=0
                grup2030=[]
                while i < len(grup30):
                    if grup20[i] == grup30[i]:
                        grup2030.append(grup20[i])
                    else:
                        grup2030.append("-")
                    i+=1
            else:
                grup2030=[]

            if grup31 != []:
                i=0
                grup2031=[]
                while i < len(grup31):
                    if grup20[i] == grup31[i]:
                        grup2031.append(grup20[i])
                    else:
                        grup2031.append("-")
                    i+=1
            else:
                grup2031=[]

            if grup32 != []:
                i=0
                grup2032=[]
                while i < len(grup32):
                    if grup20[i] == grup32[i]:
                        grup2032.append(grup20[i])
                    else:
                        grup2032.append("-")
                    i+=1
            else:
                grup2032=[]

            if grup33 != []:
                i=0
                grup2033=[]
                while i < len(grup33):
                    if grup20[i] == grup33[i]:
                        grup2033.append(grup20[i])
                    else:
                        grup2033.append("-")
                    i+=1
            else:
                grup2033=[]
        else:
            grup2030=[]
            grup2031=[]
            grup2032=[]
            grup2033=[]

        #ikinin biri ---------------------------------
        if grup21 != []:
            if grup30 != []:
                i=0
                grup2130=[]
                while i < len(grup30):
                    if grup21[i] == grup30[i]:
                        grup2130.append(grup21[i])
                    else:
                        grup2130.append("-")
                    i+=1
            else:
                grup2130=[]

            if grup31 != []:
                i=0
                grup2131=[]
                while i < len(grup31):
                    if grup21[i] == grup31[i]:
                        grup2131.append(grup21[i])
                    else:
                        grup2131.append("-")
                    i+=1
            else:
                grup2131=[]

            if grup32 != []:
                i=0
                grup2132=[]
                while i < len(grup32):
                    if grup21[i] == grup32[i]:
                        grup2132.append(grup21[i])
                    else:
                        grup2132.append("-")
                    i+=1
            else:
                grup2132=[]

            if grup33 != []:
                i=0
                grup2133=[]
                while i < len(grup33):
                    if grup21[i] == grup33[i]:
                        grup2133.append(grup21[i])
                    else:
                        grup2133.append("-")
                    i+=1
            else:
                grup2133=[]
        else:
            grup2130=[]
            grup2131=[]
            grup2132=[]
            grup2133=[]

        #ikinin ikisi---------------------------------
        if grup22 != []:
            if grup30 != []:
                i=0
                grup2230=[]
                while i < len(grup30):
                    if grup22[i] == grup30[i]:
                        grup2230.append(grup22[i])
                    else:
                        grup2230.append("-")
                    i+=1
            else:
                grup2230=[]

            if grup31 != []:
                i=0
                grup2231=[]
                while i < len(grup31):
                    if grup22[i] == grup31[i]:
                        grup2231.append(grup22[i])
                    else:
                        grup2231.append("-")
                    i+=1
            else:
                grup2231=[]

            if grup32 != []:
                i=0
                grup2232=[]
                while i < len(grup32):
                    if grup22[i] == grup32[i]:
                        grup2232.append(grup22[i])
                    else:
                        grup2232.append("-")
                    i+=1
            else:
                grup2232=[]

            if grup33 != []:
                i=0
                grup2233=[]
                while i < len(grup33):
                    if grup22[i] == grup33[i]:
                        grup2233.append(grup22[i])
                    else:
                        grup2233.append("-")
                    i+=1
            else:
                grup2233=[]
        else:
            grup2230=[]
            grup2231=[]
            grup2232=[]
            grup2233=[]

        #ikinin ucu---------------------------------
        if grup23 != []:
            if grup30 != []:
                i=0
                grup2330=[]
                while i < len(grup30):
                    if grup23[i] == grup30[i]:
                        grup2330.append(grup23[i])
                    else:
                        grup2330.append("-")
                    i+=1
            else:
                grup2330=[]

            if grup31 != []:
                i=0
                grup2331=[]
                while i < len(grup31):
                    if grup23[i] == grup31[i]:
                        grup2331.append(grup23[i])
                    else:
                        grup2331.append("-")
                    i+=1
            else:
                grup2331=[]

            if grup32 != []:
                i=0
                grup2332=[]
                while i < len(grup32):
                    if grup23[i] == grup32[i]:
                        grup2332.append(grup23[i])
                    else:
                        grup2332.append("-")
                    i+=1
            else:
                grup2332=[]

            if grup33 != []:
                i=0
                grup2333=[]
                while i < len(grup33):
                    if grup23[i] == grup33[i]:
                        grup2333.append(grup23[i])
                    else:
                        grup2333.append("-")
                    i+=1
            else:
                grup2333=[]
        else:
            grup2330=[]
            grup2331=[]
            grup2332=[]
            grup2333=[]


        #return grubu -------------------------------------------------
        package0=[]
        # print 0-1 grubu-------------------
        # print("grup 00")
        # print(grup0010)
        if grup0010 != []:
            i=0
            j=0
            while i< len(grup0010):
                if grup0010[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0010)

        # print(grup0011)
        if grup0011 != []:
            i=0
            j=0
            while i< len(grup0011):
                if grup0011[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0011)

        # print(grup0012)
        if grup0012 != []:
            i=0
            j=0
            while i< len(grup0012):
                if grup0012[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0012)

        # print(grup0013)
        if grup0013 != []:
            i=0
            j=0
            while i< len(grup0013):
                if grup0013[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0013)

        # print(grup0014)
        if grup0014 != []:
            i=0
            j=0
            while i< len(grup0014):
                if grup0014[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0014)

        # print(grup0015)
        if grup0015 != []:
            i=0
            j=0
            while i< len(grup0015):
                if grup0015[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0015)

        # print(grup0016)
        if grup0016 != []:
            i=0
            j=0
            while i< len(grup0016):
                if grup0016[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0016)

        # print(grup0017)
        if grup0017 != []:
            i=0
            j=0
            while i< len(grup0017):
                if grup0017[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0017)

        # print(grup0018)
        if grup0018 != []:
            i=0
            j=0
            while i< len(grup0018):
                if grup0018[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0018)

        # print(grup0019)
        if grup0019 != []:
            i=0
            j=0
            while i< len(grup0019):
                if grup0019[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0019)

        # print(grup00110)
        if grup00110 != []:
            i=0
            j=0
            while i< len(grup00110):
                if grup00110[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup00110)

        # print(grup00111)
        if grup00111 != []:
            i=0
            j=0
            while i< len(grup00111):
                if grup00111[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup00111)

        # print(grup00112)
        if grup00112 != []:
            i=0
            j=0
            while i< len(grup00112):
                if grup00112[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup00112)

        # print("grup 01")
        # print(grup0110)
        if grup0110 != []:
            i=0
            j=0
            while i< len(grup0110):
                if grup0110[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0110)

        # print(grup0111)
        if grup0111 != []:
            i=0
            j=0
            while i< len(grup0111):
                if grup0111[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0111)

        # print(grup0112)
        if grup0112 != []:
            i=0
            j=0
            while i< len(grup0112):
                if grup0112[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0112)

        # print(grup0113)
        if grup0113 != []:
            i=0
            j=0
            while i< len(grup0113):
                if grup0113[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0113)

        # print(grup0114)
        if grup0114 != []:
            i=0
            j=0
            while i< len(grup0114):
                if grup0114[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0114)

        # print(grup0115)
        if grup0115 != []:
            i=0
            j=0
            while i< len(grup0115):
                if grup0115[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0115)

        # print(grup0116)
        if grup0116 != []:
            i=0
            j=0
            while i< len(grup0116):
                if grup0116[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0116)

        # print(grup0117)
        if grup0117 != []:
            i=0
            j=0
            while i< len(grup0117):
                if grup0117[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0117)

        # print(grup0118)
        if grup0118 != []:
            i=0
            j=0
            while i< len(grup0118):
                if grup0118[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0118)

        # print(grup0119)
        if grup0119 != []:
            i=0
            j=0
            while i< len(grup0119):
                if grup0119[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0119)

        # print(grup01110)
        if grup01110 != []:
            i=0
            j=0
            while i< len(grup01110):
                if grup01110[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup01110)

        # print(grup01111)
        if grup01111 != []:
            i=0
            j=0
            while i< len(grup01111):
                if grup01111[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup01111)

        # print(grup01112)
        if grup01112 != []:
            i=0
            j=0
            while i< len(grup01112):
                if grup01112[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup01112)

        # print("grup 02")--------------------------
        # print(grup0210)
        if grup0210 != []:
            i=0
            j=0
            while i< len(grup0210):
                if grup0210[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0210)

        # print(grup0211)
        if grup0211 != []:
            i=0
            j=0
            while i< len(grup0211):
                if grup0211[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0211)

        # print(grup0212)
        if grup0212 != []:
            i=0
            j=0
            while i< len(grup0212):
                if grup0212[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0212)

        # print(grup0213)
        if grup0213 != []:
            i=0
            j=0
            while i< len(grup0213):
                if grup0213[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0213)

        # print(grup0214)
        if grup0214 != []:
            i=0
            j=0
            while i< len(grup0214):
                if grup0214[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0214)

        # print(grup0215)
        if grup0215 != []:
            i=0
            j=0
            while i< len(grup0215):
                if grup0215[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0215)

        # print(grup0216)
        if grup0216 != []:
            i=0
            j=0
            while i< len(grup0216):
                if grup0216[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0216)

        # print(grup0217)
        if grup0217 != []:
            i=0
            j=0
            while i< len(grup0217):
                if grup0217[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0217)

        # print(grup0218)
        if grup0218 != []:
            i=0
            j=0
            while i< len(grup0218):
                if grup0218[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0218)

        # print(grup0219)
        if grup0219 != []:
            i=0
            j=0
            while i< len(grup0219):
                if grup0219[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0219)

        # print(grup02110)
        if grup02110 != []:
            i=0
            j=0
            while i< len(grup02110):
                if grup02110[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup02110)

        # print(grup02111)
        if grup02111 != []:
            i=0
            j=0
            while i< len(grup02111):
                if grup02111[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup02111)

        # print(grup02112)
        if grup02112 != []:
            i=0
            j=0
            while i< len(grup02112):
                if grup02112[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup02112)

        # print("grup 03")---------------------------------------
        # print(grup0310)
        if grup0310 != []:
            i=0
            j=0
            while i< len(grup0310):
                if grup0310[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0310)

        # print(grup0311)
        if grup0311 != []:
            i=0
            j=0
            while i< len(grup0311):
                if grup0311[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0311)

        # print(grup0312)
        if grup0312 != []:
            i=0
            j=0
            while i< len(grup0312):
                if grup0312[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0312)

        # print(grup0313)
        if grup0313 != []:
            i=0
            j=0
            while i< len(grup0313):
                if grup0313[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0313)

        # print(grup0314)
        if grup0314 != []:
            i=0
            j=0
            while i< len(grup0314):
                if grup0314[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0314)

        # print(grup0315)
        if grup0315 != []:
            i=0
            j=0
            while i< len(grup0315):
                if grup0315[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0315)

        # print(grup0316)
        if grup0316 != []:
            i=0
            j=0
            while i< len(grup0316):
                if grup0316[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0316)

        # print(grup0317)
        if grup0317 != []:
            i=0
            j=0
            while i< len(grup0317):
                if grup0317[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0317)

        # print(grup0318)
        if grup0318 != []:
            i=0
            j=0
            while i< len(grup0318):
                if grup0318[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0318)

        # print(grup0319)
        if grup0319 != []:
            i=0
            j=0
            while i< len(grup0319):
                if grup0319[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup0319)

        # print(grup03110)
        if grup03110 != []:
            i=0
            j=0
            while i< len(grup03110):
                if grup03110[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup03110)

        # print(grup03111)
        if grup03111 != []:
            i=0
            j=0
            while i< len(grup03111):
                if grup03111[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup03111)

        # print(grup03112)
        if grup03112 != []:
            i=0
            j=0
            while i< len(grup03112):
                if grup03112[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package0.append(grup03112)

        # print 1-2 grubu------------------------------------
        package1=[]
        # print("grup 10")
        # print(grup1020)
        if grup1020 != []:
            i=0
            j=0
            while i< len(grup1020):
                if grup1020[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1020)

        # print(grup1021)
        if grup1021 != []:
            i=0
            j=0
            while i< len(grup1021):
                if grup1021[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1021)

        # print(grup1022)
        if grup1022 != []:
            i=0
            j=0
            while i< len(grup1022):
                if grup1022[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1022)

        # print(grup1023)
        if grup1023 != []:
            i=0
            j=0
            while i< len(grup1023):
                if grup1023[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1023)

        # print(grup1024)
        if grup1024 != []:
            i=0
            j=0
            while i< len(grup1024):
                if grup1024[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1024)

        # print(grup1025)
        if grup1025 != []:
            i=0
            j=0
            while i< len(grup1025):
                if grup1025[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1025)

        # print(grup1026)
        if grup1026 != []:
            i=0
            j=0
            while i< len(grup1026):
                if grup1026[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1026)

        # print(grup1027)
        if grup1027 != []:
            i=0
            j=0
            while i< len(grup1027):
                if grup1027[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1027)

        # print(grup1028)
        if grup1028 != []:
            i=0
            j=0
            while i< len(grup1028):
                if grup1028[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1028)

        # print(grup1029)
        if grup1029 != []:
            i=0
            j=0
            while i< len(grup1029):
                if grup1029[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1029)

        # print(grup10210)
        if grup10210 != []:
            i=0
            j=0
            while i< len(grup10210):
                if grup10210[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup10210)

        # print(grup10211)
        if grup10211 != []:
            i=0
            j=0
            while i< len(grup10211):
                if grup10211[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup10211)

        # print("grup 11")
        # print(grup1120)
        if grup1120 != []:
            i=0
            j=0
            while i< len(grup1120):
                if grup1120[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1120)

        # print(grup1121)
        if grup1121 != []:
            i=0
            j=0
            while i< len(grup1121):
                if grup1121[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1121)

        # print(grup1122)
        if grup1122 != []:
            i=0
            j=0
            while i< len(grup1122):
                if grup1122[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1122)

        # print(grup1123)
        if grup1123 != []:
            i=0
            j=0
            while i< len(grup1123):
                if grup1123[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1123)

        # print(grup1124)
        if grup1124 != []:
            i=0
            j=0
            while i< len(grup1124):
                if grup1124[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1124)

        # print(grup1125)
        if grup1125 != []:
            i=0
            j=0
            while i< len(grup1125):
                if grup1125[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1125)

        # print(grup1126)
        if grup1126 != []:
            i=0
            j=0
            while i< len(grup1126):
                if grup1126[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1126)

        # print(grup1127)
        if grup1127 != []:
            i=0
            j=0
            while i< len(grup1127):
                if grup1127[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1127)

        # print(grup1128)
        if grup1128 != []:
            i=0
            j=0
            while i< len(grup1128):
                if grup1128[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1128)

        # print(grup1129)
        if grup1129 != []:
            i=0
            j=0
            while i< len(grup1129):
                if grup1129[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1129)

        # print(grup11210)
        if grup11210 != []:
            i=0
            j=0
            while i< len(grup11210):
                if grup11210[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup11210)

        # print(grup11211)
        if grup11211 != []:
            i=0
            j=0
            while i< len(grup11211):
                if grup11211[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup11211)

        # print("grup 12")
        # print(grup1220)
        if grup1220 != []:
            i=0
            j=0
            while i< len(grup1220):
                if grup1220[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1220)

        # print(grup1221)
        if grup1221 != []:
            i=0
            j=0
            while i< len(grup1221):
                if grup1221[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1221)

        # print(grup1222)
        if grup1222 != []:
            i=0
            j=0
            while i< len(grup1222):
                if grup1222[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1222)

        # print(grup1223)
        if grup1223 != []:
            i=0
            j=0
            while i< len(grup1223):
                if grup1223[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1223)

        # print(grup1224)
        if grup1224 != []:
            i=0
            j=0
            while i< len(grup1224):
                if grup1224[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1224)

        # print(grup1225)
        if grup1225 != []:
            i=0
            j=0
            while i< len(grup1225):
                if grup1225[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1225)

        # print(grup1226)
        if grup1226 != []:
            i=0
            j=0
            while i< len(grup1226):
                if grup1226[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1226)

        # print(grup1227)
        if grup1227 != []:
            i=0
            j=0
            while i< len(grup1227):
                if grup1227[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1227)

        # print(grup1228)
        if grup1228 != []:
            i=0
            j=0
            while i< len(grup1228):
                if grup1228[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1228)

        # print(grup1229)
        if grup1229 != []:
            i=0
            j=0
            while i< len(grup1229):
                if grup1229[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1229)

        # print(grup12210)
        if grup12210 != []:
            i=0
            j=0
            while i< len(grup12210):
                if grup12210[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup12210)

        # print(grup12211)
        if grup12211 != []:
            i=0
            j=0
            while i< len(grup12211):
                if grup12211[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup12211)

        # print("grup 13")
        # print(grup1320)
        if grup1320 != []:
            i=0
            j=0
            while i< len(grup1320):
                if grup1320[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1320)

        # print(grup1321)
        if grup1321 != []:
            i=0
            j=0
            while i< len(grup1321):
                if grup1321[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1321)

        # print(grup1322)
        if grup1322 != []:
            i=0
            j=0
            while i< len(grup1322):
                if grup1322[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1322)

        # print(grup1323)
        if grup1323 != []:
            i=0
            j=0
            while i< len(grup1323):
                if grup1323[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1323)

        # print(grup1324)
        if grup1324 != []:
            i=0
            j=0
            while i< len(grup1324):
                if grup1324[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1324)

        # print(grup1325)
        if grup1325 != []:
            i=0
            j=0
            while i< len(grup1325):
                if grup1325[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1325)

        # print(grup1326)
        if grup1326 != []:
            i=0
            j=0
            while i< len(grup1326):
                if grup1326[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1326)

        # print(grup1327)
        if grup1327 != []:
            i=0
            j=0
            while i< len(grup1327):
                if grup1327[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1327)

        # print(grup1328)
        if grup1328 != []:
            i=0
            j=0
            while i< len(grup1328):
                if grup1328[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1328)

        # print(grup1329)
        if grup1329 != []:
            i=0
            j=0
            while i< len(grup1329):
                if grup1329[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1329)

        # print(grup13210)
        if grup13210 != []:
            i=0
            j=0
            while i< len(grup13210):
                if grup13210[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup13210)

        # print(grup13211)
        if grup13211 != []:
            i=0
            j=0
            while i< len(grup13211):
                if grup13211[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup13211)

        # print("grup 14")
        # print(grup1420)
        if grup1420 != []:
            i=0
            j=0
            while i< len(grup1420):
                if grup1420[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1420)

        # print(grup1421)
        if grup1421 != []:
            i=0
            j=0
            while i< len(grup1421):
                if grup1421[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1421)

        # print(grup1422)
        if grup1422 != []:
            i=0
            j=0
            while i< len(grup1422):
                if grup1422[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1422)

        # print(grup1423)
        if grup1423 != []:
            i=0
            j=0
            while i< len(grup1423):
                if grup1423[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1423)

        # print(grup1424)
        if grup1424 != []:
            i=0
            j=0
            while i< len(grup1424):
                if grup1424[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1424)

        # print(grup1425)
        if grup1425 != []:
            i=0
            j=0
            while i< len(grup1425):
                if grup1425[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1425)

        # print(grup1426)
        if grup1426 != []:
            i=0
            j=0
            while i< len(grup1426):
                if grup1426[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1426)

        # print(grup1427)
        if grup1427 != []:
            i=0
            j=0
            while i< len(grup1427):
                if grup1427[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1427)

        # print(grup1428)
        if grup1428 != []:
            i=0
            j=0
            while i< len(grup1428):
                if grup1428[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1428)

        # print(grup1429)
        if grup1429 != []:
            i=0
            j=0
            while i< len(grup1429):
                if grup1429[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1429)

        # print(grup14210)
        if grup14210 != []:
            i=0
            j=0
            while i< len(grup14210):
                if grup14210[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup14210)

        # print(grup14211)
        if grup14211 != []:
            i=0
            j=0
            while i< len(grup14211):
                if grup14211[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup14211)

        # print("grup 15")
        # print(grup1520)
        if grup1520 != []:
            i=0
            j=0
            while i< len(grup1520):
                if grup1520[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1520)

        # print(grup1521)
        if grup1521 != []:
            i=0
            j=0
            while i< len(grup1521):
                if grup1521[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1521)

        # print(grup1522)
        if grup1522 != []:
            i=0
            j=0
            while i< len(grup1522):
                if grup1522[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1522)

        # print(grup1523)
        if grup1523 != []:
            i=0
            j=0
            while i< len(grup1523):
                if grup1523[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1523)

        # print(grup1524)
        if grup1524 != []:
            i=0
            j=0
            while i< len(grup1524):
                if grup1524[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1524)

        # print(grup1525)
        if grup1525 != []:
            i=0
            j=0
            while i< len(grup1525):
                if grup1525[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1525)

        # print(grup1526)
        if grup1526 != []:
            i=0
            j=0
            while i< len(grup1526):
                if grup1526[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1526)

        # print(grup1527)
        if grup1527 != []:
            i=0
            j=0
            while i< len(grup1527):
                if grup1527[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1527)

        # print(grup1528)
        if grup1528 != []:
            i=0
            j=0
            while i< len(grup1528):
                if grup1528[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1528)

        # print(grup1529)
        if grup1529 != []:
            i=0
            j=0
            while i< len(grup1529):
                if grup1529[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1529)

        # print(grup15210)
        if grup15210 != []:
            i=0
            j=0
            while i< len(grup15210):
                if grup15210[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup15210)

        # print(grup15211)
        if grup15211 != []:
            i=0
            j=0
            while i< len(grup15211):
                if grup15211[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup15211)

        # print("grup 16")
        # print(grup1620)
        if grup1620 != []:
            i=0
            j=0
            while i< len(grup1620):
                if grup1620[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1620)

        # print(grup1621)
        if grup1621 != []:
            i=0
            j=0
            while i< len(grup1621):
                if grup1621[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1621)

        # print(grup1622)
        if grup1622 != []:
            i=0
            j=0
            while i< len(grup1622):
                if grup1622[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1622)

        # print(grup1623)
        if grup1623 != []:
            i=0
            j=0
            while i< len(grup1623):
                if grup1623[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1623)

        # print(grup1624)
        if grup1624 != []:
            i=0
            j=0
            while i< len(grup1624):
                if grup1624[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1624)

        # print(grup1625)
        if grup1625 != []:
            i=0
            j=0
            while i< len(grup1625):
                if grup1625[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1625)

        # print(grup1626)
        if grup1626 != []:
            i=0
            j=0
            while i< len(grup1626):
                if grup1626[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1626)

        # print(grup1627)
        if grup1627 != []:
            i=0
            j=0
            while i< len(grup1627):
                if grup1627[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1627)

        # print(grup1628)
        if grup1628 != []:
            i=0
            j=0
            while i< len(grup1628):
                if grup1628[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1628)

        # print(grup1629)
        if grup1629 != []:
            i=0
            j=0
            while i< len(grup1629):
                if grup1629[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1629)

        # print(grup16210)
        if grup16210 != []:
            i=0
            j=0
            while i< len(grup16210):
                if grup16210[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup16210)

        # print(grup16211)
        if grup16211 != []:
            i=0
            j=0
            while i< len(grup16211):
                if grup16211[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup16211)

        # print("grup 17")
        # print(grup1720)
        if grup1720 != []:
            i=0
            j=0
            while i< len(grup1720):
                if grup1720[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1720)

        # print(grup1721)
        if grup1721 != []:
            i=0
            j=0
            while i< len(grup1721):
                if grup1721[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1721)

        # print(grup1722)
        if grup1722 != []:
            i=0
            j=0
            while i< len(grup1722):
                if grup1722[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1722)

        # print(grup1723)
        if grup1723 != []:
            i=0
            j=0
            while i< len(grup1723):
                if grup1723[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1723)

        # print(grup1724)
        if grup1724 != []:
            i=0
            j=0
            while i< len(grup1724):
                if grup1724[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1724)

        # print(grup1725)
        if grup1725 != []:
            i=0
            j=0
            while i< len(grup1725):
                if grup1725[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1725)

        # print(grup1726)
        if grup1726 != []:
            i=0
            j=0
            while i< len(grup1726):
                if grup1726[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1726)

        # print(grup1727)
        if grup1727 != []:
            i=0
            j=0
            while i< len(grup1727):
                if grup1727[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1727)

        # print(grup1728)
        if grup1728 != []:
            i=0
            j=0
            while i< len(grup1728):
                if grup1728[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1728)

        # print(grup1729)
        if grup1729 != []:
            i=0
            j=0
            while i< len(grup1729):
                if grup1729[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1729)

        # print(grup17210)
        if grup17210 != []:
            i=0
            j=0
            while i< len(grup17210):
                if grup17210[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup17210)

        # print(grup17211)
        if grup17211 != []:
            i=0
            j=0
            while i< len(grup17211):
                if grup17211[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup17211)

        # print("grup 18")
        # print(grup1820)
        if grup1820 != []:
            i=0
            j=0
            while i< len(grup1820):
                if grup1820[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1820)

        # print(grup1821)
        if grup1821 != []:
            i=0
            j=0
            while i< len(grup1821):
                if grup1821[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1821)

        # print(grup1822)
        if grup1822 != []:
            i=0
            j=0
            while i< len(grup1822):
                if grup1822[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1822)

        # print(grup1823)
        if grup1823 != []:
            i=0
            j=0
            while i< len(grup1823):
                if grup1823[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1823)

        # print(grup1824)
        if grup1824 != []:
            i=0
            j=0
            while i< len(grup1824):
                if grup1824[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1824)

        # print(grup1825)
        if grup1825 != []:
            i=0
            j=0
            while i< len(grup1825):
                if grup1825[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1825)

        # print(grup1826)
        if grup1826 != []:
            i=0
            j=0
            while i< len(grup1826):
                if grup1826[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1826)

        # print(grup1827)
        if grup1827 != []:
            i=0
            j=0
            while i< len(grup1827):
                if grup1827[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1827)

        # print(grup1828)
        if grup1828 != []:
            i=0
            j=0
            while i< len(grup1828):
                if grup1828[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1828)

        # print(grup1829)
        if grup1829 != []:
            i=0
            j=0
            while i< len(grup1829):
                if grup1829[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1829)

        # print(grup18210)
        if grup18210 != []:
            i=0
            j=0
            while i< len(grup18210):
                if grup18210[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup18210)

        # print(grup18211)
        if grup18211 != []:
            i=0
            j=0
            while i< len(grup18211):
                if grup18211[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup18211)

        # print("grup 19")
        # print(grup1920)
        if grup1920 != []:
            i=0
            j=0
            while i< len(grup1920):
                if grup1920[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1920)

        # print(grup1921)
        if grup1921 != []:
            i=0
            j=0
            while i< len(grup1921):
                if grup1921[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1921)

        # print(grup1922)
        if grup1922 != []:
            i=0
            j=0
            while i< len(grup1922):
                if grup1922[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1922)

        # print(grup1923)
        if grup1923 != []:
            i=0
            j=0
            while i< len(grup1923):
                if grup1923[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1923)

        # print(grup1924)
        if grup1924 != []:
            i=0
            j=0
            while i< len(grup1924):
                if grup1924[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1924)

        # print(grup1925)
        if grup1925 != []:
            i=0
            j=0
            while i< len(grup1925):
                if grup1925[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1925)

        # print(grup1926)
        if grup1926 != []:
            i=0
            j=0
            while i< len(grup1926):
                if grup1926[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1926)

        # print(grup1927)
        if grup1927 != []:
            i=0
            j=0
            while i< len(grup1927):
                if grup1927[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1927)

        # print(grup1928)
        if grup1928 != []:
            i=0
            j=0
            while i< len(grup1928):
                if grup1928[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1928)

        # print(grup1929)
        if grup1929 != []:
            i=0
            j=0
            while i< len(grup1929):
                if grup1929[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup1929)

        # print(grup19210)
        if grup19210 != []:
            i=0
            j=0
            while i< len(grup19210):
                if grup19210[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup19210)

        # print(grup19211)
        if grup19211 != []:
            i=0
            j=0
            while i< len(grup19211):
                if grup19211[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup19211)

        # print("grup 110")
        # print(grup11020)
        if grup11020 != []:
            i=0
            j=0
            while i< len(grup11020):
                if grup11020[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup11020)

        # print(grup11021)
        if grup11021 != []:
            i=0
            j=0
            while i< len(grup11021):
                if grup11021[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup11021)

        # print(grup11022)
        if grup11022 != []:
            i=0
            j=0
            while i< len(grup11022):
                if grup11022[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup11022)

        # print(grup11023)
        if grup11023 != []:
            i=0
            j=0
            while i< len(grup11023):
                if grup11023[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup11023)

        # print(grup11024)
        if grup11024 != []:
            i=0
            j=0
            while i< len(grup11024):
                if grup11024[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup11024)

        # print(grup11025)
        if grup11025 != []:
            i=0
            j=0
            while i< len(grup11025):
                if grup11025[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup11025)

        # print(grup11026)
        if grup11026 != []:
            i=0
            j=0
            while i< len(grup11026):
                if grup11026[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup11026)

        # print(grup11027)
        if grup11027 != []:
            i=0
            j=0
            while i< len(grup11027):
                if grup11027[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup11027)

        # print(grup11028)
        if grup11028 != []:
            i=0
            j=0
            while i< len(grup11028):
                if grup11028[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup11028)

        # print(grup11029)
        if grup11029 != []:
            i=0
            j=0
            while i< len(grup11029):
                if grup11029[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup11029)

        # print(grup110210)
        if grup110210 != []:
            i=0
            j=0
            while i< len(grup110210):
                if grup110210[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup110210)

        # print(grup110211)
        if grup110211 != []:
            i=0
            j=0
            while i< len(grup110211):
                if grup110211[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup110211)

        # print("grup 111")
        # print(grup11120)
        if grup11120 != []:
            i=0
            j=0
            while i< len(grup11120):
                if grup11120[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup11120)

        # print(grup11121)
        if grup11121 != []:
            i=0
            j=0
            while i< len(grup11121):
                if grup11121[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup11121)

        # print(grup11122)
        if grup11122 != []:
            i=0
            j=0
            while i< len(grup11122):
                if grup11122[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup11122)

        # print(grup11123)
        if grup11123 != []:
            i=0
            j=0
            while i< len(grup11123):
                if grup11123[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup11123)

        # print(grup11124)
        if grup11125 != []:
            i=0
            j=0
            while i< len(grup11125):
                if grup11125[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup11125)

        # print(grup11125)
        if grup11125 != []:
            i=0
            j=0
            while i< len(grup11125):
                if grup11125[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup11125)

        # print(grup11126)
        if grup11126 != []:
            i=0
            j=0
            while i< len(grup11126):
                if grup11126[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup11126)

        # print(grup11127)
        if grup11127 != []:
            i=0
            j=0
            while i< len(grup11127):
                if grup11127[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup11127)

        # print(grup11128)
        if grup11128 != []:
            i=0
            j=0
            while i< len(grup11128):
                if grup11128[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup11128)

        # print(grup11129)
        if grup11129 != []:
            i=0
            j=0
            while i< len(grup11129):
                if grup11129[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup11129)

        # print(grup111210)
        if grup111210 != []:
            i=0
            j=0
            while i< len(grup111210):
                if grup111210[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup111210)

        # print(grup111211)
        if grup111211 != []:
            i=0
            j=0
            while i< len(grup111211):
                if grup111211[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup111211)

        # print("grup 112")
        # print(grup11220)
        if grup11220 != []:
            i=0
            j=0
            while i< len(grup11220):
                if grup11220[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup11220)

        # print(grup11221)
        if grup11221 != []:
            i=0
            j=0
            while i< len(grup11221):
                if grup11221[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup11221)

        # print(grup11222)
        if grup11222 != []:
            i=0
            j=0
            while i< len(grup11222):
                if grup11222[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup11222)

        # print(grup11223)
        if grup11223 != []:
            i=0
            j=0
            while i< len(grup11223):
                if grup11223[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup11223)

        # print(grup11224)
        if grup11224 != []:
            i=0
            j=0
            while i< len(grup11224):
                if grup11224[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup11224)

        # print(grup11225)
        if grup11225 != []:
            i=0
            j=0
            while i< len(grup11225):
                if grup11225[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup11225)

        # print(grup11226)
        if grup11226 != []:
            i=0
            j=0
            while i< len(grup11226):
                if grup11226[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup11226)

        # print(grup11227)
        if grup11227 != []:
            i=0
            j=0
            while i< len(grup11227):
                if grup11227[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup11227)

        # print(grup11228)
        if grup11228 != []:
            i=0
            j=0
            while i< len(grup11228):
                if grup11228[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup11228)

        # print(grup11229)
        if grup11229 != []:
            i=0
            j=0
            while i< len(grup11229):
                if grup11229[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup11229)

        # print(grup112210)
        if grup112210 != []:
            i=0
            j=0
            while i< len(grup112210):
                if grup112210[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup112210)

        # print(grup112211)
        if grup112211 != []:
            i=0
            j=0
            while i< len(grup112211):
                if grup112211[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package1.append(grup112211)

        # print --------------------2-3 grup--------------------------
        package2=[]
        # print("grup 20")
        # print(grup2030)
        if grup2030 != []:
            i=0
            j=0
            while i< len(grup2030):
                if grup2030[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package2.append(grup2030)

        # print(grup2031)
        if grup2031 != []:
            i=0
            j=0
            while i< len(grup2031):
                if grup2031[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package2.append(grup2031)

        # print(grup2032)
        if grup2032 != []:
            i=0
            j=0
            while i< len(grup2032):
                if grup2032[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package2.append(grup2032)

        # print(grup2033)
        if grup2033 != []:
            i=0
            j=0
            while i< len(grup2033):
                if grup2033[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package2.append(grup2033)

        # print("grup 21")
        # print(grup2130)
        if grup2130 != []:
            i=0
            j=0
            while i< len(grup2130):
                if grup2130[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package2.append(grup2130)

        # print(grup2131)
        if grup2131 != []:
            i=0
            j=0
            while i< len(grup2131):
                if grup2131[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package2.append(grup2131)

        # print(grup2132)
        if grup2132 != []:
            i=0
            j=0
            while i< len(grup2132):
                if grup2132[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package2.append(grup2132)

        # print(grup2133)
        if grup2133 != []:
            i=0
            j=0
            while i< len(grup2133):
                if grup2133[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package2.append(grup2133)

        # print("grup 22")
        # print(grup2230)
        if grup2230 != []:
            i=0
            j=0
            while i< len(grup2230):
                if grup2230[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package2.append(grup2230)

        # print(grup2231)
        if grup2231 != []:
            i=0
            j=0
            while i< len(grup2231):
                if grup2231[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package2.append(grup2231)

        # print(grup2232)
        if grup2232 != []:
            i=0
            j=0
            while i< len(grup2232):
                if grup2232[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package2.append(grup2232)

        # print(grup2233)
        if grup2233 != []:
            i=0
            j=0
            while i< len(grup2233):
                if grup2233[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package2.append(grup2233)

        # print("grup 23")
        # print(grup2330)
        if grup2330 != []:
            i=0
            j=0
            while i< len(grup2330):
                if grup2330[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package2.append(grup2330)

        # print(grup2331)
        if grup2331 != []:
            i=0
            j=0
            while i< len(grup2331):
                if grup2331[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package2.append(grup2331)

        # print(grup2332)
        if grup2332 != []:
            i=0
            j=0
            while i< len(grup2332):
                if grup2332[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package2.append(grup2332)

        # print(grup2333)
        if grup2333 != []:
            i=0
            j=0
            while i< len(grup2333):
                if grup2333[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 4:
                package2.append(grup2333)


        package=[package0,package1,package2]

        return package


thirdMatch= thirdMatch(matchList)
thirdMatch.createThirdMatch()
