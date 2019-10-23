from heap import MaxHeap, MinHeap


class Median:
    def __init__(self):
        self.h_low = MaxHeap()
        self.h_high = MinHeap()

    def add_element(self, value):
        if self.h_low.heap_size == 0 or value < self.h_low.max():
            self.h_low.insert(value)
            if self.h_low.heap_size - self.h_high.heap_size > 1:
                self.h_high.insert(self.h_low.extract_max())
        else:
            self.h_high.insert(value)
            if self.h_high.heap_size - self.h_low.heap_size > 1:
                self.h_low.insert(self.h_high.extract_min())

    def get_median(self):
        if (self.h_low.heap_size + self.h_high.heap_size) % 2 == 0:
            return self.h_low.max(), self.h_high.min()
        else:
            if self.h_low.heap_size > self.h_high.heap_size:
                return self.h_low.max()
            else:
                return self.h_high.min()

    def get_maxheap_elements(self):
        return self.h_low.heap

    def get_minheap_elements(self):
        return self.h_high.heap
