class Node:
    def __init__(self, val):
        self.val = val
        self.child = None
        self.sibling = None


class PairingHeap:
    def __init__(self):
        self.root = Node(None)


class PairingMinHeap(PairingHeap):
    def min(self):
        return self.root.val

    def merge(self, r):
        if not self.root.val:
            self.root = r
        elif not r.val:
            pass
        else:
            if self.root.val < r.val:
                r.sibling = self.root.child
                self.root.child = r
            else:
                self.root.sibling = r.child
                r.child = self.root
                self.root = r

    def insert(self, key):
        self.merge(Node(key))

    # def delete_min(self):
    #     if not self.root.child:
    #         return None
    #     m = self.root.val
    #     self.root = self.root.child
    #     print(self.root.val)
    #     while self.root.sibling:
    #         print(self.root.sibling)
    #         self.merge(self.root.sibling)
    #         # if self.root.sibling.sibling:
    #
    #         self.root.sibling = self.root.sibling.sibling
    #         # print("siblsibl " + str(self.root.sibling.val))
    #         # else:
    #         #     self.root.sibling = None
    #     return m


class PairingMaxHeap(PairingHeap):
    def max(self):
        return self.root.val

    def merge(self, r):
        if not self.root.val:
            self.root = r
        elif not r.val:
            pass
        else:
            if self.root.val > r.val:
                r.sibling = self.root.child
                self.root.child = r
            else:
                self.root.sibling = r.child
                r.child = self.root
                self.root = r

    def insert(self, key):
        self.merge(Node(key))


if __name__ == "__main__":
    p = PairingMaxHeap()
    import random
    a = list(range(1, 11))
    random.shuffle(a)
    for el in a:
        p.insert(el)
    print(p.max())



