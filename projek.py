class Siswa:
    def __init__(self,nama,asal,nilai,kelas):
        self.nama=nama
        self.asal=asal
        self.nilai=nilai
        self.kelas=kelas

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
        print( temp.data.nama, "|" , temp.data.asal, "|" , temp.data.nilai, "|" , temp.data.kelas)
        temp = temp.next
     
def insertFirst( head_ref, new_data):
 
    new_node = Node(0)

    new_node.data = new_data

    new_node.next = (head_ref)

    (head_ref) = new_node
    return head_ref

list = None
filename = "data.txt"
with open(filename, "r") as f:
    lines = f.readlines()

for line in lines:
    dataMahasiswa = line.split(",")
    siswa = Siswa(dataMahasiswa[0],dataMahasiswa[1],dataMahasiswa[2],dataMahasiswa[3])
    list = insertFirst(list,siswa)


insertionSort(list)
printList(list)