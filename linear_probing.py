#Linear Probing
array = [-1]*10
notfull = 0
def hash(k,m):
    global notfull
    i = 0
    while i<10:
        hash = (k % m + i) % m
        if array[hash] == -1:
            array[hash] = k
            notfull =0
            break
        notfull = 1
        i += 1
    return 0

m = int(input("Enter array size:"))
while notfull != 1:
    k = int(input("Enter key value:"))
    hash(k,m)

print(array)