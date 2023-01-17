# Mid square Method.
def hash(k,m):
    hash = 0
    k_sq = int(k)*int(k)
    temp = k_sq
    rev_n = 0
    count = 0
    while temp != 0:
        rev_n *= 10
        rev_n += temp % 10
        temp //= 10
        count += 1
    count //= 2
    print(count)
    while count != -2:
        if count > 0:
            rev_n //= 10
            count -= 1
        else:
            hash = hash * 10 + (rev_n % 10)
            rev_n //= 10
            count -= 1
    return str(hash)
array_size = input("Enter the size of Array:")
k = input("Enter Key:")
print("Index will be:" + hash(k,array_size))