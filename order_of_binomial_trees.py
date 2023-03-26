def decimal_to_binary(n):
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

def orders_of_binomial_trees(n):
    binary = int(decimal_to_binary(n))

    # exponents = [len(binary) - i - 1 for i, bit in enumerate(binary) if bit == '1']
    # exponents.sort()
    count = 0
    arr = []
    while binary != 0:
        digit = binary % 10
        if digit == 1:
            arr.append(count)
        count += 1
        binary = binary // 10
    return arr

# Example usage
n = int(input("Enter Number of nodes:"))
orders = orders_of_binomial_trees(n)
print(f"The binomial heap with {n} nodes contains trees of order: {orders}")
