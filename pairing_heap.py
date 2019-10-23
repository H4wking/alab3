class Node:
    def __init__(self, val):
        self.val = val
        self.child = None
        self.sibling = None


class PairingHeap:
    def __init__(self):
        self.root = None


class PairingMinHeap(PairingHeap):
    def min(self):
        return self.root.val

    def merge(self, r):
        if not self.root:
            self.root = r
        elif not r:
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

    def delete_min(self):
        if not self.root.child:
            return None
        m = self.root.val
        self.root = self.root.child
        sibs = []
        while self.root.sibling:
            sibs.append(self.root.sibling)
            self.root.sibling = self.root.sibling.sibling
        for sib in sibs:
            self.merge(sib)
        return m


class PairingMaxHeap(PairingHeap):
    def max(self):
        return self.root.val

    def merge(self, r):
        if not self.root:
            self.root = r
        elif not r:
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

    def delete_max(self):
        if not self.root.child:
            return None
        m = self.root.val
        self.root = self.root.child
        sibs = []
        while self.root.sibling:
            sibs.append(self.root.sibling)
            self.root.sibling = self.root.sibling.sibling
        for sib in sibs:
            self.merge(sib)
        return m
