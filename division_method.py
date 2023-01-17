# Division Method.
def hash(k,m):
    hash = int(k) % int(m)
    return str(hash)

array_size = input("Enter the size of Array:")
k = input("Enter Key:")
print("Index will be:" + hash(k,array_size))