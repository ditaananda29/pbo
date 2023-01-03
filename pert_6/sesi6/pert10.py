# Nama : Dita Ananda
# NIM : 20210801332
# PBO tugas 10


# parent class
class plant(object):

    def __init__(self, Jumlah_Air, Jumlah_Pupuk, Status_tumbuh):
        self.Jumlah_Air = Jumlah_Air 
        self.Jumlah_Pupuk = Jumlah_Pupuk 
        self.Status_Tumbuh = Status_tumbuh 

    def tumbuh(self):
        if self.Status_tumbuh < 4:
            self.Jumlah_Air -= 3
            self.Jumlah_Pupuk -= 1
            self.Status_tumbuh += 1

    def cek_kondisitumbuh(self):
        if self.Jumlah_Air >= 3 and self.Jumlah_Pupuk >= 1:
            plant.tumbuh(self)

    def Beri_Air(self):
        self.Jumlah_Air += 1
        plant.cek_kondisitumbuh(self)

    def Beri_Pupuk(self):
        self.Jumlah_Pupuk += 1
        plant.cek_kondisitumbuh(self)

    def get_statustumbuhtext(self):
        if self.Status_tumbuh == 0:
            print("Benih")
        elif self.Status_tumbuh == 1:
            print("Tunas")
        elif self.Status_tumbuh == 2:
            print("Tanaman Kecil")
        elif self.Status_tumbuh == 3:
            print("Tanaman Dewasa")
        else:
            print("Berbunga")
            
    def DisplayPlant(self):
        #print(Plant.getstatustumbuh)
        print("Jumlah_Air \t: {} \nJumlah_Pupuk \t: {}".format(self.Jumlah_Air, self.Jumlah_Pupuk))\
        

    def getJumlah_Air(self):
        return self.Jumlah_Air
    
    def setJumlah_Air(self, n):
        self.Jumlah_Air = n

    def getJumlah_Pupuk(self):
        return self.Jumlah_Pupuk

    def setJumlah_Pupuk(self, n):
        self.Jumlah_Pupuk = n

    def getStatus_tumbuh(self):
        return self.Status_tumbuh

    def setStatus_tumbuh(self, n):
        self.Status_tumbuh = n

#child class
class Anggrek(plant):

    def __init__(self, Jumlah_Air, Jumlah_Pupuk, Status_tumbuh, Jenis):
        self.Jenis = Jenis
        Plant. __init__(self, Jumlah_Air, Jumlah_Pupuk, Status_tumbuh)

    def anggrektumbuh(self):
        if self.Status_tumbuh < 4:
            self.Jumlah_Air -= 3
            self.Jumlah_Pupuk -=2
            self.Status_tumbuh += 1

    def cek_kondisitumbuh(self):
        if self.Jumlah_Air >= 3 and self.Jumlah_Pupuk >= 2:
                Anggrek.anggrektumbuh()
        
    def getJenis(self):
        return self.Jenis

#child class
class Mawar(plant):

    def __init__(self, Jumlah_Air, Jumlah_Pupuk, Status_tumbuh, Jenis):
        self.Jenis = Jenis
        Plant.__init__(self, Jumlah_Air, Jumlah_Pupuk, Status_tumbuh)

    def mawartumbuh(self):
        if self.Status_tumbuh < 4:
            self.Jumlah_Air -= 3
            self.Jumlah_Pupuk -= 1
            self.Status_tumbuh += 1

    def cek_kondisitumbuh(self):
        if self.Jumlah_Air >= 3 and self.Jumlah_Pupuk >= 1:
            Mawar.mawartumbuh()
        
    def getJenis(self):
        return self.Jenis

#child class
class Melati(plant):

    def __init__(self, Jumlah_Air, Jumlah_Pupuk, Status_tumbuh, Jenis):
        self.Jenis = Jenis 
        plant.__init__(self, Jumlah_Air, Jumlah_Pupuk, Status_tumbuh)
        
    def melatitumbuh(self):
        if self.Status_tumbuh < 4:
            self.Jumlah_Air -= 3
            self.Jumlah_Pupuk -= 1
            self.Status_tumbuh += 1

    def cek_kondisitumbuh(self):
        if self.Jumlah_Air >= 3 and self.Jumlah_Pupuk >= 1:
            Melati.melatitumbuh()

    def getJenis(self):
        return self.Jenis
    
class Garden(plant):

    def __init__(self,Jumlah_Air, Jumlah_Pupuk, Status_tumbuh, Size, ntanaman, mGardenName, hasilpanen):
        self.Size = Size 
        self.ntanaman = ntanaman
        self.mGardenName = mGardenName
        self.pArrList = [" "]
        self.hasilpanen = hasilpanen
        plant.__init__(self, Jumlah_Air, Jumlah_Pupuk, Status_tumbuh)

    def Garden(self, pName):
        self.mGardenName = pName

    def addPlant(self):
        if self.ntanaman < self.Size:
            self.pArrList.append += 1
            self.ntanaman += 1
            return True
        else:
            return False

    def harvestPlant(self):
        tmpN = 0
        i = 0
        lenght = len(self.pArrList)
        while self.pArrList !=0 and i < lenght:
            if self.pArrList[i] == 4 and plant.getstatustumbuh() == 4:
                self.pArrList.remove[i]
                self.ntanaman -= 1
                tmpN -= 1
                i = 0
            else:
                i += 1

            self.hasilpanen = self.hasilpanen + (tmpN *100)
            return tmpN 

    def BeriAir(self):
        for i in range(0, len(self.pArrList)):
            self.pArrList[i] = Garden.BeriAir()

    def BeriPupuk(self):
        for i in range(0, len(self.pArrList[i]-1)):
            self.pArrList[i] = Garden.BeriPupuk()

    def displayPlant(self):
        print("------- {}".format(self.mGardenName))
        print("There Are {} plants in the garden".format(self.ntanaman))
        print("Your harvest point : {}".format(self.hasilpanen))

        for i in range(0, len(self.pArrList)-1):
            self.pArrList[i] = Garden.displayPlant()

    def getHasilPanen(self):
        return self.hasilpanen


# tanaman1 = Anggrek(2, 3, 4, 'Anggrek')
# print("Jenis tanaman\t: {}".format(tanaman1.Jenis))
# tanaman1.getStatus_tumbuhtext()
# tanaman1.DisplayPlant() 

# tanaman2 = Mawar(1, 4, 2, 'Mawar')
# print("\nJenis tanaman \t: {}".format(tanaman2.Jenis)
# tanaman2.getStatus_tumbuhtext()
# tanaman2.DisplayPlant()

# tanaman3 = Mawar(3, 1, 1, 'Melati')
# print("\nJenis tanaman \t: {}".format(tanama3.Jenis)
# tanaman3.getStatus_tumbuhtext()
# tanaman3.DisplayPlant()

tanaman1 = Garden(2, 3, 4, 10, 2, 'Kebun Bunga', 2)
tanaman1.displayPlant()

