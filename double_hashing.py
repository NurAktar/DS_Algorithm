#Double hashing
array = [-1]*10
overflow = 0
def hash(m,k):
    i=0
    n = m-2
    global overflow
    overflow = 1
    while i<m:
        hash = ((k % m) + i*(k % n)) % m
        if array[hash] == -1:
            array[hash] = k
            overflow = 0
            break
        i += 1
    return 0
m = int(input("Enter array size(max m=10):"))
while overflow == 0:
    k = int(input("Enter key:"))
    hash(m,k)
print(array)
