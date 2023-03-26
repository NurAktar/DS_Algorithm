class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
        else:
            curr = self.root
            i = 0
            while i < 4:
                if val[i] == '0':
                    if curr.left is None:
                        curr.left = new_node
                        break
                    else:
                        curr = curr.left
                elif val[i] == '1':
                    if curr.right is None:
                        curr.right = new_node
                        break
                    else:
                        curr = curr.right
                i += 1

    def search(self, val):
        curr = self.root
        i = 0
        while curr is not None:
            if val == curr.val:
                return True
            elif val[i] == '0':
                curr = curr.left
            else:
                curr = curr.right
            i += 1
        return False


# Create a new binary search tree
bst = BinarySearchTree()

# Insert some 4-bit binary numbers
bst.insert("0000")
bst.insert("0001")
bst.insert("0010")
bst.insert("1110")
bst.insert("1111")

# Search for a binary number
print(bst.search("0101"))  # False
print(bst.search("0000"))  # True
print(bst.search("0001"))  # True
print(bst.search("1111"))  # True
print(bst.search("0100"))  # False
print(bst.search("1010"))  # Flase
print(bst.search("11111"))  # False