# Multiplication Method.
from math import sqrt
def hash(k,m):
    A = (sqrt(5)-1)/2
    hash = ( int(m) * (int(k) * A % 1) ) / 1
    return str(int(hash))

array_size = input("Enter the size of Array:")
k = input("Enter Key:")
print("Index will be:" + hash(k, array_size))