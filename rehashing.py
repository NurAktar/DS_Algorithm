#Rehashing a hashtable
table = [-1,26,32,43,19]
def hash(m,k):
    global array
    hash = k % m
    array[hash] = k

m = int(input("Enter size of m:"))
array = [-1]*m
for each in table:
    hash(m,each)
print(array)