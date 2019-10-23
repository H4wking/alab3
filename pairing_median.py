from pairing_heap import PairingMinHeap, PairingMaxHeap


class PairingMedian:
    def __init__(self):
        self.h_low = PairingMaxHeap()
        self.h_high = PairingMinHeap()
        self.low_size = 0
        self.high_size = 0

    def add_element(self, value):
        if self.low_size == 0 or (value < self.h_low.max() and self.low_size - self.high_size < 1):
            print("l", value)
            self.h_low.insert(value)
            self.low_size += 1
        else:
            print("h", value)
            self.h_high.insert(value)
            self.high_size += 1

    def get_median(self):
        if (self.low_size + self.high_size) % 2 == 0:
            return self.h_low.max(), self.h_high.min()
        else:
            if self.low_size > self.high_size:
                return self.h_low.max()
            else:
                return self.h_high.min()


import random


a = list(range(1, 12))
# random.shuffle(a)
a.reverse()
print(a)
h = PairingMedian()
for el in a:
    h.add_element(el)
    print(h.get_median())
# for el in a:
#     ha.add_element(el)
#     print(ha.get_median())
# print(h.h_low, h.h_high)
print(h.get_median())
# print(ha.get_median())