#Quadratic Probing
overflow = 0
def hash(k,m):
    global overflow
    i = 0
    c1 = 1
    c2 = 3
    while i<10:
        hash = (k % m +c1*i+c2*i*i) % m
        if array[hash] == -1:
            array[hash] = k
            overflow =0
            break
        overflow = 1
        i += 1
    return 0

m = int(input("Enter array size:"))
array = [-1]*m
while overflow != 1:
    k = int(input("Enter key value:"))
    hash(k,m)

print(array)