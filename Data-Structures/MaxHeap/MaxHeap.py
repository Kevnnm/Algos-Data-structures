class MaxHeap:
    def __init__(self):
        # 0th element is in invalid index, start at 1 instead.
        # This simplifies calculation for child/parent
        self.heapList = [0]
        self.currentSize = 0

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.perc_up(self.currentSize)

    def perc_up(self, i):
        while i // 2 > 0:
            if self.heapList[i] > self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def perc_down(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.max_child(i)
            if self.heapList[i] < self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def max_child(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] > self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def del_max(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.perc_down(1)
        return retval

    def build_heap(self, items):
        i = len(items) // 2
        self.currentSize = len(items)
        self.heapList = [0] + items[:]
        while i > 0:
            self.perc_down(i)
            i = i - 1


def main():
    hp = MaxHeap()
    pq = [7, 20, 2, 15, 5, 21, 6, 12, 1, 8, 3, 9, 10, 24]
    hp.build_heap(pq)
    hp.del_max()
    hp.del_max()
    hp.del_max()
    hp.del_max()
    hp.del_max()
    hp.del_max()
    hp.del_max()

    hp.insert(99)
    hp.insert(1)
    hp.insert(55)
    hp.insert(16)
    hp.insert(28)
    hp.insert(33)
    hp.insert(599)
    hp.insert(19)
    hp.insert(0)
    print(hp.heapList)


if __name__ == "__main__":
    main()
