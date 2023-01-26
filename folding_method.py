# Folding Method
key = int(input("Enter key:"))
m = int(input("Table size:"))
rev = 0
count = 0

while key != 0:
    rev = rev * 10 + (key % 10)
    key //= 10
    count += 1
sum = 0
while count > 0:
    n = 0
    n = n * 10 + (rev % 10)
    rev //=10
    if rev != 0:
        n = n * 10 + (rev % 10)
        rev //=10
    count -= 2
    sum += n
hash = sum % m
print(hash)