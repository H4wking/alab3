from pairing_heap import PairingMinHeap, PairingMaxHeap


class PairingMedian:
    def __init__(self):
        self.h_low = PairingMaxHeap()
        self.h_high = PairingMinHeap()
        self.low_size = 0
        self.high_size = 0

    def add_element(self, value):
        if self.low_size == 0 or value < self.h_low.max():
            self.h_low.insert(value)
            self.low_size += 1
            if self.low_size - self.high_size > 1:
                self.h_high.insert(self.h_low.delete_max())
                self.low_size -= 1
                self.high_size += 1
        else:
            self.h_high.insert(value)
            self.high_size += 1
            if self.high_size - self.low_size > 1:
                self.h_low.insert(self.h_high.delete_min())
                self.high_size -= 1
                self.low_size += 1

    def get_median(self):
        if (self.low_size + self.high_size) % 2 == 0:
            return self.h_low.max(), self.h_high.min()
        else:
            if self.low_size > self.high_size:
                return self.h_low.max()
            else:
                return self.h_high.min()
