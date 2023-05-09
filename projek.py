class Siswa:
    def __init__(self,nama,asal,umur,nilai):
        self.nama=nama
        self.asal=asal
        self.umur=umur
        self.nilai=nilai

siswa1 = Siswa("Adit Balmun","DKI Jakarta",15,90)
siswa2 = Siswa("Adit","DKI",15,90)
lst = LinkedList([siswa1,siswa2])
print(lst)