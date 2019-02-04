from firstMatchClass import firstMatch

matchList= firstMatch.createTable()

class secondeMatch(object):

    def __init__(self,matchList):
        self.matchList= matchList

    def createSecondeMatch(self):

        if self.matchList[0] != []:
            grup00=self.matchList[0][0]
        else:
            grup00=[]

        if self.matchList[1] != []:
            if len(self.matchList[1]) == 4:
                grup10= self.matchList[1][0]
                grup11= self.matchList[1][1]
                grup12= self.matchList[1][2]
                grup13= self.matchList[1][3]
            elif len(self.matchList[1]) == 3:
                grup10= self.matchList[1][0]
                grup11= self.matchList[1][1]
                grup12= self.matchList[1][2]
                grup13=[]
            elif len(self.matchList[1]) == 2:
                grup10= self.matchList[1][0]
                grup11= self.matchList[1][1]
                grup12=[]
                grup13=[]
            elif len(self.matchList[1]) == 1:
                grup10= self.matchList[1][0]
                grup11=[]
                grup12=[]
                grup13=[]
        else:
            grup10=[]
            grup11=[]
            grup12=[]
            grup13=[]

        if self.matchList[2] != []:
            if len(self.matchList[2]) == 6:
                grup20=self.matchList[2][0]
                grup21=self.matchList[2][1]
                grup22=self.matchList[2][2]
                grup23=self.matchList[2][3]
                grup24=self.matchList[2][4]
                grup25=self.matchList[2][5]
            elif len(self.matchList[2]) == 5:
                grup20=self.matchList[2][0]
                grup21=self.matchList[2][1]
                grup22=self.matchList[2][2]
                grup23=self.matchList[2][3]
                grup24=self.matchList[2][4]
                grup25=[]
            elif len(self.matchList[2]) == 4:
                grup20=self.matchList[2][0]
                grup21=self.matchList[2][1]
                grup22=self.matchList[2][2]
                grup23=self.matchList[2][3]
                grup24=[]
                grup25=[]
            elif len(self.matchList[2]) == 3:
                grup20=self.matchList[2][0]
                grup21=self.matchList[2][1]
                grup22=self.matchList[2][2]
                grup23=[]
                grup24=[]
                grup25=[]
            elif len(self.matchList[2]) == 2:
                grup20=self.matchList[2][0]
                grup21=self.matchList[2][1]
                grup22=[]
                grup23=[]
                grup24=[]
                grup25=[]
            elif len(self.matchList[2]) == 1:
                grup20=self.matchList[2][0]
                grup21=[]
                grup22=[]
                grup23=[]
                grup24=[]
                grup25=[]
        else:
            grup20=[]
            grup21=[]
            grup22=[]
            grup23=[]
            grup24=[]
            grup25=[]

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
                grup33=[]
            elif len(self.matchList[3]) == 2:
                grup30= self.matchList[3][0]
                grup31= self.matchList[3][1]
                grup32=[]
                grup33=[]
            elif len(self.matchList[3]) == 1:
                grup30= self.matchList[3][0]
                grup31=[]
                grup32=[]
                grup33=[]
        else:
            grup30=[]
            grup31=[]
            grup32=[]
            grup33=[]

        if self.matchList[4] != []:
            grup40=self.matchList[4][0]
        else:
            grup40=[]

        # HellJumper!

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
        else:
            grup0010=[]
            grup0011=[]
            grup0012=[]
            grup0013=[]

        #birinci grup eslestirmesi
        if grup10 != []:
            if grup20 != []:
                i=0
                grup1020=[]
                while i < len(grup20):
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
                while i < len(grup21):
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
                while i < len(grup22):
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
                while i < len(grup23):
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
                while i < len(grup24):
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
                while i < len(grup25):
                    if grup10[i] == grup23[i]:
                        grup1025.append(grup10[i])
                    else:
                        grup1025.append("-")
                    i+=1
            else:
                grup1025=[]
        else:
            grup1020=[]
            grup1021=[]
            grup1022=[]
            grup1023=[]
            grup1024=[]
            grup1025=[]


        #birin biri ***************************************
        if grup11 != []:
            if grup20 != []:
                i=0
                grup1120=[]
                while i < len(grup20):
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
                while i < len(grup21):
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
                while i < len(grup22):
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
                while i < len(grup23):
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
                while i < len(grup24):
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
                while i < len(grup25):
                    if grup11[i] == grup25[i]:
                        grup1125.append(grup11[i])
                    else:
                        grup1125.append("-")
                    i+=1
            else:
                grup1125=[]
        else:
            grup1120=[]
            grup1121=[]
            grup1122=[]
            grup1123=[]
            grup1124=[]
            grup1125=[]

        #birin ikisi***************************************
        if grup12 != []:

            if grup20 != []:
                i=0
                grup1220=[]
                while i < len(grup20):
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
                while i < len(grup21):
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
                while i < len(grup22):
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
                while i < len(grup23):
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
                while i < len(grup24):
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
                while i < len(grup25):
                    if grup12[i] == grup25[i]:
                        grup1225.append(grup12[i])
                    else:
                        grup1225.append("-")
                    i+=1
            else:
                grup1225=[]
        else:
            grup1220=[]
            grup1221=[]
            grup1222=[]
            grup1223=[]
            grup1224=[]
            grup1225=[]

        #birin ucu***************************************
        if grup13 != []:
            if grup20 != []:
                i=0
                grup1320=[]
                while i < len(grup20):
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
                while i < len(grup21):
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
                while i < len(grup22):
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
                while i < len(grup23):
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
                while i < len(grup24):
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
                while i < len(grup25):
                    if grup13[i] == grup25[i]:
                        grup1325.append(grup13[i])
                    else:
                        grup1325.append("-")
                    i+=1
            else:
                grup1325=[]
        else:
            grup1320=[]
            grup1321=[]
            grup1322=[]
            grup1323=[]
            grup1324=[]
            grup1325=[]

        #ikinci bolum eslestirmesi
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


        #ikinin biri***************************************************
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

        #ikinin ikisi***************************************************
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

        #ikinin ucu***************************************************
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

        #ikinin dordu***************************************************
        if grup24 != []:
            if grup30 != []:
                i=0
                grup2430=[]
                while i < len(grup30):
                    if grup24[i] == grup30[i]:
                        grup2430.append(grup24[i])
                    else:
                        grup2430.append("-")
                    i+=1
            else:
                grup2430=[]

            if grup31 != []:
                i=0
                grup2431=[]
                while i < len(grup31):
                    if grup24[i] == grup31[i]:
                        grup2431.append(grup24[i])
                    else:
                        grup2431.append("-")
                    i+=1
            else:
                grup2431=[]

            if grup32 != []:
                i=0
                grup2432=[]
                while i < len(grup32):
                    if grup24[i] == grup32[i]:
                        grup2432.append(grup24[i])
                    else:
                        grup2432.append("-")
                    i+=1
            else:
                grup2432=[]

            if grup33 != []:
                i=0
                grup2433=[]
                while i < len(grup33):
                    if grup24[i] == grup33[i]:
                        grup2433.append(grup24[i])
                    else:
                        grup2433.append("-")
                    i+=1
            else:
                grup2433=[]
        else:
            grup2430=[]
            grup2431=[]
            grup2432=[]
            grup2433=[]


        #ikinin besi***************************************************
        if grup25 != []:
            if grup30 != []:
                i=0
                grup2530=[]
                while i < len(grup30):
                    if grup25[i] == grup30[i]:
                        grup2530.append(grup25[i])
                    else:
                        grup2530.append("-")
                    i+=1
            else:
                grup2530=[]

            if grup31 != []:
                i=0
                grup2531=[]
                while i < len(grup31):
                    if grup25[i] == grup31[i]:
                        grup2531.append(grup25[i])
                    else:
                        grup2531.append("-")
                    i+=1
            else:
                grup2531=[]

            if grup32 != []:
                i=0
                grup2532=[]
                while i < len(grup32):
                    if grup25[i] == grup32[i]:
                        grup2532.append(grup25[i])
                    else:
                        grup2532.append("-")
                    i+=1
            else:
                grup2532=[]

            if grup33 != []:
                i=0
                grup2533=[]
                while i < len(grup33):
                    if grup25[i] == grup33[i]:
                        grup2533.append(grup25[i])
                    else:
                        grup2533.append("-")
                    i+=1
            else:
                grup2533=[]
        else:
            grup2530=[]
            grup2531=[]
            grup2532=[]
            grup2533=[]


        #ucun biri :)***************************************************
        if grup40 != []:
            if grup30 != []:
                i=0
                grup4030=[]
                while i < len(grup30):
                    if grup40[i] == grup30[i]:
                        grup4030.append(grup40[i])
                    else:
                        grup4030.append("-")
                    i+=1
            else:
                grup4030=[]

            if grup31 != []:
                i=0
                grup4031=[]
                while i < len(grup31):
                    if grup40[i] == grup31[i]:
                        grup4031.append(grup40[i])
                    else:
                        grup4031.append("-")
                    i+=1
            else:
                grup4031=[]

            if grup32 != []:
                i=0
                grup4032=[]
                while i < len(grup32):
                    if grup40[i] == grup32[i]:
                        grup4032.append(grup40[i])
                    else:
                        grup4032.append("-")
                    i+=1
            else:
                grup4032=[]

            if grup33 != []:
                i=0
                grup4033=[]
                while i < len(grup33):
                    if grup40[i] == grup33[i]:
                        grup4033.append(grup40[i])
                    else:
                        grup4033.append("-")
                    i+=1
            else:
                grup4033=[]
        else:
            grup4030=[]
            grup4031=[]
            grup4032=[]
            grup4033=[]

        #---------------------------Return Grubu--------------------------------

        # print("***************0-1 grup******************")
        package01=[]
        # print(grup0010)
        if grup0010 != []:
            i=0
            j=0
            while i< len(grup0010):
                if grup0010[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package01.append(grup0010)

        # print(grup0011)
        if grup0011 != []:
            i=0
            j=0
            while i< len(grup0011):
                if grup0011[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package01.append(grup0011)

        # print(grup0012)
        if grup0012 != []:
            i=0
            j=0
            while i< len(grup0012):
                if grup0012[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package01.append(grup0012)

        # print(grup0013)
        if grup0013 != []:
            i=0
            j=0
            while i< len(grup0013):
                if grup0013[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package01.append(grup0013)

        # print("***************1-2 grup******************")
        package12=[]
        # print(grup1020)
        if grup1020 != []:
            i=0
            j=0
            while i< len(grup1020):
                if grup1020[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package12.append(grup1020)
        # print(grup1021)
        if grup1021 != []:
            i=0
            j=0
            while i< len(grup1021):
                if grup1021[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package12.append(grup1021)

        # print(grup1022)
        if grup1022 != []:
            i=0
            j=0
            while i< len(grup1022):
                if grup1022[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package12.append(grup1022)

        # print(grup1023)
        if grup1023 != []:
            i=0
            j=0
            while i< len(grup1023):
                if grup1023[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package12.append(grup1023)

        # print(grup1024)
        if grup1024 != []:
            i=0
            j=0
            while i< len(grup1024):
                if grup1024[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package12.append(grup1024)

        # print(grup1025)
        if grup1025 != []:
            i=0
            j=0
            while i< len(grup1025):
                if grup1025[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package12.append(grup1025)

        # print(grup1120)
        if grup1120 != []:
            i=0
            j=0
            while i< len(grup1120):
                if grup1120[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package12.append(grup1120)

        # print(grup1121)
        if grup1121 != []:
            i=0
            j=0
            while i< len(grup1121):
                if grup1121[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package12.append(grup1121)

        # print(grup1122)
        if grup1122 != []:
            i=0
            j=0
            while i< len(grup1122):
                if grup1122[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package12.append(grup1122)

        # print(grup1123)
        if grup1123 != []:
            i=0
            j=0
            while i< len(grup1123):
                if grup1123[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package12.append(grup1123)

        # print(grup1124)
        if grup1124 != []:
            i=0
            j=0
            while i< len(grup1124):
                if grup1124[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package12.append(grup1124)

        # print(grup1125)
        if grup1125 != []:
            i=0
            j=0
            while i< len(grup1125):
                if grup1125[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package12.append(grup1125)

        # print(grup1220)
        if grup1220 != []:
            i=0
            j=0
            while i< len(grup1220):
                if grup1220[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package12.append(grup1220)

        # print(grup1221)
        if grup1221 != []:
            i=0
            j=0
            while i< len(grup1221):
                if grup1221[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package12.append(grup1221)

        # print(grup1222)
        if grup1222 != []:
            i=0
            j=0
            while i< len(grup1222):
                if grup1222[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package12.append(grup1222)

        # print(grup1223)
        if grup1223 != []:
            i=0
            j=0
            while i< len(grup1223):
                if grup1223[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package12.append(grup1223)

        # print(grup1224)
        if grup1224 != []:
            i=0
            j=0
            while i< len(grup1224):
                if grup1224[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package12.append(grup1224)

        # print(grup1225)
        if grup1225 != []:
            i=0
            j=0
            while i< len(grup1225):
                if grup1225[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package12.append(grup1225)

        # print(grup1320)
        if grup1320 != []:
            i=0
            j=0
            while i< len(grup1320):
                if grup1320[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package12.append(grup1320)

        # print(grup1321)
        if grup1321 != []:
            i=0
            j=0
            while i< len(grup1321):
                if grup1321[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package12.append(grup1321)

        # print(grup1322)
        if grup1322 != []:
            i=0
            j=0
            while i< len(grup1322):
                if grup1322[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package12.append(grup1321)

        # print(grup1323)
        if grup1323 != []:
            i=0
            j=0
            while i< len(grup1323):
                if grup1323[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package12.append(grup1323)
        # else:
        #     print(grup1323)

        # print(grup1324)
        if grup1324 != []:
            i=0
            j=0
            while i< len(grup1324):
                if grup1324[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package12.append(grup1324)

        # print(grup1325)
        if grup1325 != []:
            i=0
            j=0
            while i< len(grup1325):
                if grup1325[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package12.append(grup1325)


        # print("****************2-3 grup*****************")
        package23=[]
        # print(grup2030)
        if grup2030 != []:
            i=0
            j=0
            while i< len(grup2030):
                if grup2030[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package23.append(grup2030)

        # print(grup2031)
        if grup2031 != []:
            i=0
            j=0
            while i< len(grup2031):
                if grup2031[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package23.append(grup2031)

        # print(grup2032)
        if grup2032 != []:
            i=0
            j=0
            while i< len(grup2032):
                if grup2032[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package23.append(grup2032)

        # print(grup2033)
        if grup2033 != []:
            i=0
            j=0
            while i< len(grup2033):
                if grup2033[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package23.append(grup2033)

        # print(grup2130)
        if grup2130 != []:
            i=0
            j=0
            while i< len(grup2130):
                if grup2130[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package23.append(grup2130)

        # print(grup2131)
        if grup2131 != []:
            i=0
            j=0
            while i< len(grup2131):
                if grup2131[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package23.append(grup2131)

        # print(grup2132)
        if grup2132 != []:
            i=0
            j=0
            while i< len(grup2132):
                if grup2132[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package23.append(grup2132)

        # print(grup2133)
        if grup2133 != []:
            i=0
            j=0
            while i< len(grup2133):
                if grup2133[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package23.append(grup2133)

        # print(grup2230)
        if grup2230 != []:
            i=0
            j=0
            while i< len(grup2230):
                if grup2230[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package23.append(grup2230)

        # print(grup2231)
        if grup2231 != []:
            i=0
            j=0
            while i< len(grup2231):
                if grup2231[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package23.append(grup2231)

        # print(grup2232)
        if grup2232 != []:
            i=0
            j=0
            while i< len(grup2232):
                if grup2232[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package23.append(grup2232)

        # print(grup2233)
        if grup2233 != []:
            i=0
            j=0
            while i< len(grup2233):
                if grup2233[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package23.append(grup2233)

        # print(grup2330)
        if grup2330 != []:
            i=0
            j=0
            while i< len(grup2330):
                if grup2330[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package23.append(grup2330)

        # print(grup2331)
        if grup2331 != []:
            i=0
            j=0
            while i< len(grup2331):
                if grup2331[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package23.append(grup2331)

        # print(grup2332)
        if grup2332 != []:
            i=0
            j=0
            while i< len(grup2332):
                if grup2332[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package23.append(grup2332)

        # print(grup2333)
        if grup2333 != []:
            i=0
            j=0
            while i< len(grup2333):
                if grup2333[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package23.append(grup2333)

        # print(grup2430)
        if grup2430 != []:
            i=0
            j=0
            while i< len(grup2430):
                if grup2430[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package23.append(grup2430)

        # print(grup2431)
        if grup2431 != []:
            i=0
            j=0
            while i< len(grup2431):
                if grup2431[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package23.append(grup2431)

        # print(grup2432)
        if grup2432 != []:
            i=0
            j=0
            while i< len(grup2432):
                if grup2432[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package23.append(grup2432)

        # print(grup2433)
        if grup2433 != []:
            i=0
            j=0
            while i< len(grup2433):
                if grup2433[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package23.append(grup2433)

        # print(grup2530)
        if grup2530 != []:
            i=0
            j=0
            while i< len(grup2530):
                if grup2530[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package23.append(grup2530)

        # print(grup2531)
        if grup2531 != []:
            i=0
            j=0
            while i< len(grup2531):
                if grup2531[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package23.append(grup2531)

        # print(grup2532)
        if grup2532 != []:
            i=0
            j=0
            while i< len(grup2532):
                if grup2532[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package23.append(grup2532)

        # print(grup2533)
        if grup2533 != []:
            i=0
            j=0
            while i< len(grup2533):
                if grup2533[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package23.append(grup2533)

        # print("****************3-4 grup*****************")
        package34=[]
        # print(grup4030)
        if grup4030 != []:
            i=0
            j=0
            while i< len(grup4030):
                if grup4030[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package34.append(grup4030)

        # print(grup4031)
        if grup4031 != []:
            i=0
            j=0
            while i< len(grup4031):
                if grup4031[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package34.append(grup4031)

        # print(grup4032)
        if grup4032 != []:
            i=0
            j=0
            while i< len(grup4032):
                if grup4032[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package34.append(grup4032)

        # print(grup4033)
        if grup4033 != []:
            i=0
            j=0
            while i< len(grup4033):
                if grup4033[i] == "-":
                    j+=1
                i+=1

            if j != 3 and j != 2 and j != 4:
                package34.append(grup4033)

        package=[package01,package12,package23,package34]

        return package

secondeMatch= secondeMatch(matchList)
secondeMatch.createSecondeMatch()
