terimSayisi= input("Terim sayisi(2-4): ")
minterm= input("Mintermleri giriniz(virgul kullanarak): ")

class inputClass(object):

    def __init__(self,terimSayisi,minterm):
        self.terimSayisi= terimSayisi
        self.minterm= minterm

    def returnTerimSayisi(self):
        return self.terimSayisi
    def returnMinterm(self):
        return self.minterm

inputClass= inputClass(terimSayisi,minterm)
