#Linear Probing
array = [-1]*10
overflow = 0
def hash(k,m):
    global overflow
    i = 0
    while i<10:
        hash = (k % m + i) % m
        if array[hash] == -1:
            array[hash] = k
            overflow =0
            break
        overflow = 1
        i += 1
    return 0

m = int(input("Enter array size:"))
while overflow != 1:
    k = int(input("Enter key value:"))
    hash(k,m)

print(array)