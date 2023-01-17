# Multiplication Method.
from math import sqrt
def hash(k,m):
    A = ((sqrt(5)-1)/2) % 1
    hash = (int(k)*A) % int(m)
    return str(hash)

array_size = input("Enter the size of Array:")
k = input("Enter Key:")
print("Index will be:" + hash(k,array_size))