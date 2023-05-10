class Siswa:
    def __init__(self,nama,asal,nilai):
        self.nama=nama
        self.asal=asal
        self.nilai=nilai


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
def insertionSort(head_ref):

    sorted = None

    current = head_ref
    while (current != None):

        next = current.next

        sorted = sortedInsert(sorted,current)

        current = next
     
    head_ref = sorted
    return head_ref
 

def sortedInsert(head_ref, new_node):
    current = None
     
    if (head_ref == None or
       (head_ref).data.nilai >= new_node.data.nilai):   
        new_node.next = head_ref
        head_ref = new_node
     
    else:

        current = head_ref
        while (current.next != None and
               current.next.data.nilai < new_node.data.nilai):       
            current = current.next
         
        new_node.next = current.next
        current.next = new_node
         
    return head_ref

def printList(head):
    temp = head
    while(temp != None):   
        print( temp.data.nama, "|" , temp.data.asal, "|" , temp.data.nilai)
        temp = temp.next
     
def insertFirst( head_ref, new_data):
 
    new_node = Node(0)

    new_node.data = new_data

    new_node.next = (head_ref)

    (head_ref) = new_node
    return head_ref

def searchNilai(head,val):
    temp=head
    if(head.data.nilai == val):
            return head
    while(True):
        if(temp is None):
            print("Data tidak ditemukan")
            return False
        if(temp.data.nilai == val):
            return temp
        temp = temp.next

def searchNama(head,val):
    temp=head
    if(head.data.nama == val):
            return head
    while(True):
        if(temp is None):
            print("Data tidak ditemukan")
            return False
        if(temp.data.nama == val):
            return temp
        temp = temp.next

list = None
filename = "data.txt"
with open(filename, "r") as f:
    lines = f.readlines()

for line in lines:
    dataMahasiswa = line.split(",")
    siswa = Siswa(dataMahasiswa[0],dataMahasiswa[1],dataMahasiswa[2])
    list = insertFirst(list,siswa)


while True:
    print()
    print("1. Tampilkan semua data")
    print("2. Sort data")
    print("3. Tambah data")
    print("4. Cari data dengan nilai")
    print("5. Cari data dengan nama")
    print("6. Keluar")

    choice = int(input("Masukkan pilihan (1/2/3/4/5/6): "))

    if choice == 1:
        printList(list)
    
    elif choice == 2:
        insertionSort(list)
    
    elif choice == 3:
        nama = input("Masukkan nama: ")
        alamat = input("Masukkan alamat: ")
        nilai = input("Masukkan nilai: ")
        siswa = Siswa(nama, alamat, nilai)
        temp = Node(0)
        temp.data = siswa
        sortedInsert(list,temp)
        print("Data telah ditambahkan ke dalam list\n")

    elif choice == 4:
        nilai = input("Masukkan nilai: ")
        siswa = searchNilai(list,nilai)
        if(siswa!=False):
            print( siswa.data.nama, "|" , siswa.data.asal, "|" , siswa.data.nilai)

    elif choice == 5:
        nama = input("Masukkan nama: ")
        siswa = searchNama(list,nama)
        if(siswa!=False):
            print( siswa.data.nama, "|" , siswa.data.asal, "|" , siswa.data.nilai)

    elif choice == 6:
        break
    
    else:
        print("Pilihan tidak valid\n")