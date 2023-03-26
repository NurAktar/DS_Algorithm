class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, priority, item):
        self.heap.append((priority, item))
        self.heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) > 1:
            self.swap(0, len(self.heap) - 1)
        priority, item = self.heap.pop()
        self.heapify_down(0)
        return priority, item

    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[parent][0] > self.heap[index][0]:
                self.swap(parent, index)
                index = parent
            else:
                break

    def heapify_down(self, index):
        while index * 2 + 1 < len(self.heap):
            left = index * 2 + 1
            right = index * 2 + 2 if index * 2 + 2 < len(self.heap) else left
            min_child = left if self.heap[left][0] < self.heap[right][0] else right
            if self.heap[index][0] > self.heap[min_child][0]:
                self.swap(index, min_child)
                index = min_child
            else:
                break

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

q = PriorityQueue()
q.push(3, 'item 3')
q.push(1, 'item 1')
q.push(2, 'item 2')
print(q.pop())
print(q.pop())
print(q.pop())
