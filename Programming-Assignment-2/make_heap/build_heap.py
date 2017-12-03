# python3
import math
import sys


class myHeap:
    def __init__(self):
        self.h = []
        self.size = 0
        self.swaps = []

    def buildHeap(self, a):
        self.size = len(a)
        self.h = a[:]
        for i in range(len(a) // 2, -1, -1):
            print("HERE:" + str(i))
            self.siftDown(i)

    def parent(self, i):
        return math.floor(i - 1 // 2)

    def leftChild(self, i):
        return 2 * i + 1

    def rightChild(self, i):
        return 2 * i + 2

    def siftUp(self, i):
        while i > 0 and self.h[self.parent(i)] < self.h[i]:
            self.h[i], self.h[self.parent(i)] = self.h[self.parent(i)], self.h[i]
            i = self.parent(i)

    def siftDown(self, i):
        maxIndex = i
        left = self.leftChild(i)
        if left < self.size and self.h[left] < self.h[maxIndex]:
            maxIndex = left
        right = self.rightChild(i)
        if right < self.size and self.h[right] < self.h[maxIndex]:
            maxIndex = right
        if i != maxIndex:
            self.swaps.append((i, maxIndex))
            self.h[i], self.h[maxIndex] = self.h[maxIndex], self.h[i]
            self.siftDown(maxIndex)

    def Insert(self, p):
        self.h.append(p)
        self.size = self.size + 1
        self.siftUp(self.size)

    def extractMax(self):
        result = self.h[1]
        self.h[1] = self.h[self.size]
        self.size = self.size - 1
        self.siftDown(1)
        return result

    def remove(self, i):
        self.h[i] = sys.maxsize
        self.siftUp(i)
        self.extractMax()

    def changePriority(self, i, p):
        oldp = self.h[i]
        self.h[i] = p
        if p > oldp:
            self.siftUp(i)
        else:
            self.siftDown(i)


class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []

    def ReadData(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        assert n == len(self._data)

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def GenerateSwaps_naive(self):
        # The following naive implementation just sorts
        # the given sequence using selection sort algorithm
        # and saves the resulting sequence of swaps.
        # This turns the given array into a heap,
        # but in the worst case gives a quadratic number of swaps.
        #
        # TODO: replace by a more efficient implementation
        for i in range(len(self._data)):
            for j in range(i + 1, len(self._data)):
                if self._data[i] > self._data[j]:
                    self._swaps.append((i, j))
                    self._data[i], self._data[j] = self._data[j], self._data[i]

    def GenerateSwaps_better(self):
        heap = myHeap()
        heap.buildHeap(self._data)
        self._data = heap.h
        self._swaps = heap.swaps

    def Solve(self):
        self.ReadData()
        self.GenerateSwaps_better()
        self.WriteResponse()


if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
