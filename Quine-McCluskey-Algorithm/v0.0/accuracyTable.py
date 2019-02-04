from accuracyClass import accuracy

term= accuracy.termCreator()
minterm= accuracy.mintermCreator()


class accuracyTable(object):

    def __init__(self,term,minterm):
        self.term= term
        self.minterm= minterm

    def accuracyTable(self):

        print("**DOGRULUK TABLOSU**")
        print(self.term)
        print("********************")
        for everyMinterm in self.minterm:
            print(everyMinterm)



accuracyTable(term,minterm).accuracyTable()
