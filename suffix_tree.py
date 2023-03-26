class Node:
    def __init__(self):
        self.children = {}
        self.start_index = None
        self.end_index = None

class SuffixTree:
    def __init__(self, string):
        self.string = string
        self.root = Node()
        self.build_tree()

    def build_tree(self):
        n = len(self.string)
        for i in range(n):
            current = self.root
            for j in range(i, n):
                if self.string[j] not in current.children:
                    node = Node()
                    node.start_index = j
                    current.children[self.string[j]] = node
                    current = node
                else:
                    current = current.children[self.string[j]]
                current.end_index = j

    def search(self, pattern):
        current = self.root
        for char in pattern:
            if char not in current.children:
                return False
            current = current.children[char]
        return True
    
suffix_tree = SuffixTree('banana')

print(suffix_tree.search('ana')) #returns true or false
