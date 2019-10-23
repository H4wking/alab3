import math


class Heap:
    def __init__(self):
        self.heap = []
        self.heap_size = 0

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def __str__(self):
        return str(self.heap)


class MaxHeap(Heap):
    def maxheapify(self, i):
        p = self.left(i)
        q = self.right(i)
        if p < self.heap_size and self.heap[p] > self.heap[i]:
            largest = p
        else:
            largest = i
        if q < self.heap_size and self.heap[q] > self.heap[largest]:
            largest = q
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.maxheapify(largest)

    def max(self):
        return self.heap[0]

    def extract_max(self):
        if self.heap_size < 1:
            return -1
        m = self.max()
        self.heap[0] = self.heap[self.heap_size - 1]
        self.heap.pop()
        self.heap_size -= 1
        self.maxheapify(0)
        return m

    def change_key(self, i, key):
        self.heap[i] = key
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def insert(self, key):
        self.heap_size += 1
        self.heap.append(- math.inf)
        self.change_key(self.heap_size - 1, key)


class MinHeap(Heap):
    def minheapify(self, i):
        p = self.left(i)
        q = self.right(i)
        if p < self.heap_size and self.heap[p] < self.heap[i]:
            smallest = p
        else:
            smallest = i
        if q < self.heap_size and self.heap[q] < self.heap[smallest]:
            smallest = q
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.minheapify(smallest)

    def min(self):
        return self.heap[0]

    def extract_min(self):
        if self.heap_size < 1:
            return -1
        m = self.min()
        self.heap[0] = self.heap[self.heap_size - 1]
        self.heap.pop()
        self.heap_size -= 1
        self.minheapify(0)
        return m

    def change_key(self, i, key):
        self.heap[i] = key
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def insert(self, key):
        self.heap_size += 1
        self.heap.append(- math.inf)
        self.change_key(self.heap_size - 1, key)



# import random
#
#
# a = list(range(1, 8))
# random.shuffle(a)
# print(a)
# h = MinHeap(a)
# print(h.heap)
# h.extract_min()
# print(h.heap)
# h.insert(1)
# print(h.heap)
