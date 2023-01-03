class waktu :

    def __init__(self, jam, menit, detik):
        self.jam = jam 
        self.menit = menit
        self.detik = detik 

jam = int(input("Masukan jam :"))
menit = int(input("Masukan menit :"))
detik = int(input("Masukan detik :"))

if jam <= 10:
    print(f"(jam),(menit),(detik)")
elif menit <= 
