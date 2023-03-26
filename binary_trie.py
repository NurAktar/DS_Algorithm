class BinaryTrieNode:
    def __init__(self, value=None):
        self.value = value
        self.children = {}

class BinaryTrie:
    def __init__(self):
        self.root = BinaryTrieNode()

    def insert(self, value):
        node = self.root
        for i in range(3, -1, -1):
            bit = (value >> i) & 1
            if bit not in node.children:
                node.children[bit] = BinaryTrieNode()
            node = node.children[bit]
        node.value = value

    def search(self, value):
        node = self.root
        for i in range(3, -1, -1):
            bit = (value >> i) & 1
            if bit not in node.children:
                return None
            node = node.children[bit]
        return node.value

trie = BinaryTrie()
trie.insert(5)   # 0101
trie.insert(6)   # 0110
trie.insert(10)  # 1010
print(trie.search(6))   # 6
print(trie.search(12))  # None
