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


# Membuka file txt dan membaca baris per baris
filename = "data.txt"
with open(filename) as f:
    lines = f.readlines()

# Membuat stack kosong
stack = Stack()

# Memasukkan setiap baris ke dalam stack
for line in lines:
    stack.push(line.strip())

# Mengeluarkan setiap item dari stack dan memisahkan nama dari tempat tinggal
while not stack.is_empty():
    item = stack.pop()
    name, location = item.split(", ")
    print(f"{name} tinggal di {location}")
