class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

stack = Stack()

# membuka file txt dan membaca setiap baris
with open('data.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        # memisahkan setiap kata dalam baris menggunakan koma sebagai pemisah
        data = line.strip().split(',')
        # menambahkan data ke dalam stack
        stack.push(data)

while True:
    print("1. Tampilkan data terakhir")
    print("2. Tambah data")
    print("3. Hapus data")
    print("4. Keluar")

    choice = int(input("Masukkan pilihan (1/2/3/4): "))

    if choice == 1:
        if stack.is_empty():
            print("Stack kosong")
        else:
            data = stack.peek()
            print(f"Data terakhir:\nNama: {data[0]}\nAlamat: {data[1]}\nNilai: {data[2]}\nKelas: {data[3]}\n")
    
    elif choice == 2:
        nama = input("Masukkan nama: ")
        alamat = input("Masukkan alamat: ")
        nilai = input("Masukkan nilai: ")
        kelas = input("Masukkan kelas: ")
        data = [nama, alamat, nilai, kelas]
        stack.push(data)
        print("Data telah ditambahkan ke dalam stack\n")

    elif choice == 3:
        if stack.is_empty():
            print("Stack kosong")
        else:
            stack.pop()
            print("Data terakhir telah dihapus dari stack\n")
    
    elif choice == 4:
        break
    
    else:
        print("Pilihan tidak valid\n")
