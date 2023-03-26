table = [-1]*9

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def hash(m,k):
    hash = k % m
    if table[hash] == -1:
        table[hash] = Node(k)
    else:
        node = table[hash]
        while True:
            if node.next == None:
                node.next = Node(k)
                break
            else:
                node = node.next
m = 9
n = int(input("How many data you want to enter?:"))
for x in range(n):
    k = int(input("Enter Key:"))
    hash(m,k)
for x in range(9):
    if(table[x] != -1):
        print("Index="+str(x)+" data="+str(table[x].data) + ",")
        if(table[x].next != None):
            print("Index.Next"+" data="+str(table[x].next.data) + ",")