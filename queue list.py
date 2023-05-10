class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()
    
    def peek_first(self):
        return self.items[-1]
    
    def peek_last(self):
        return self.items[0]
    
    def size(self):
        return len(self.items)

queue = Queue()

# membuka file txt dan membaca setiap baris
with open('data.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        # memisahkan setiap kata dalam baris menggunakan koma sebagai pemisah
        data = line.strip().split(',')
        # menambahkan data ke dalam queue
        queue.enqueue(data)

while True:
    print("1. Tampilkan data pertama")
    print("2. Tampilkan data terakhir")
    print("3. Tambah data")
    print("4. Hapus data")
    print("5. Keluar")

    choice = int(input("Masukkan pilihan (1/2/3/4/5): "))

    if choice == 1:
        if queue.is_empty():
            print("Queue kosong")
        else:
            data = queue.peek_last()
            print(f"Data pertama:\nNama: {data[0]}\nAlamat: {data[1]}\nNilai: {data[2]}\nKelas: {data[3]}\n")
    
    elif choice == 2:
        if queue.is_empty():
            print("Queue kosong")
        else:
            data = queue.peek_first()
            print(f"Data terakhir:\nNama: {data[0]}\nAlamat: {data[1]}\nNilai: {data[2]}\nKelas: {data[3]}\n")
    
    elif choice == 3:
        nama = input("Masukkan nama: ")
        alamat = input("Masukkan alamat: ")
        nilai = input("Masukkan nilai: ")
        kelas = input("Masukkan kelas: ")
        data = [nama, alamat, nilai, kelas]
        queue.enqueue(data)
        print("Data telah ditambahkan ke dalam queue\n")

    elif choice == 4:
        if queue.is_empty():
            print("Queue kosong")
        else:
            queue.dequeue()
            print("Data pertama telah dihapus dari queue\n")
    
    elif choice == 5:
        break
    
    else:
        print("Pilihan tidak valid\n")
