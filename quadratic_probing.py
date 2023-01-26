#Quadratic Probing
notfull = 0
def hash(k,m):
    global notfull
    i = 0
    c1 = 1
    c2 = 3
    while i<10:
        hash = (k % m +c1*i+c2*i*i) % m
        if array[hash] == -1:
            array[hash] = k
            notfull =0
            break
        notfull = 1
        i += 1
    return 0

m = int(input("Enter array size:"))
array = [-1]*m
while notfull != 1:
    k = int(input("Enter key value:"))
    hash(k,m)

print(array)