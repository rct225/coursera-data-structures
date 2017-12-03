# python3
from functools import reduce
import operator
from collections import Counter


class disJoint_naive:
    def __init__(self):
        self.smallest = []

    def makeSet(self, i):
        self.smallest.append(i)

    def find(self, i):
        return self.smallest[i]

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)

        if i_id == j_id:
            return
        m = min(i_id, j_id)
        for k in range(0, len(self.smallest)):
            if self.smallest[k] in [i_id, j_id]:
                self.smallest[k] = m


class disJoint_rank:
    def __init__(self):
        self.parent = []
        self.rank = []

    def makeSet(self, i):
        self.parent.append(i)
        self.rank.append(0)

    def find(self, i):
        while i != self.parent[i]:
            i = self.parent[i]
        return i

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)

        if i_id == j_id:
            return

        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
        else:
            self.parent[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] = self.rank[j_id] + 1


class disJoint_rank_compression:
    def __init__(self):
        self.parent = []
        self.rank = []

    def makeSet(self, i):
        self.parent.append(i)
        self.rank.append(0)

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)

        if i_id == j_id:
            return

        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
        else:
            self.parent[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] = self.rank[j_id] + 1


dj = disJoint_naive()

for i in range(0, 13):
    dj.makeSet(i)

print(dj.smallest)
dj.union(2, 10)
dj.union(7, 5)
dj.union(6, 1)
dj.union(3, 4)
dj.union(5, 11)
dj.union(7, 8)
dj.union(7, 3)
dj.union(12, 2)
dj.union(9, 6)
print(dj.find(6))
print(dj.find(3))
print(dj.find(11))
print(dj.find(9))

djr = disJoint_rank()

for i in range(0, 13):
    djr.makeSet(i)

djr.union(2, 10)
djr.union(7, 5)
djr.union(6, 1)
djr.union(3, 4)
djr.union(5, 11)
djr.union(7, 8)
djr.union(7, 3)
djr.union(12, 2)
djr.union(9, 6)

print(djr.rank)
print(reduce(operator.mul, [x for x in djr.rank if x > 0], 1))

djr3 = disJoint_rank()

n = 100
for i in range(0, n + 1):
    djr3.makeSet(i)

for i in range(0, n):
    djr3.union(i, i + 1)

print(djr3.rank)
print(max(djr3.rank))

djc = disJoint_rank_compression()

for i in range(0, 61):
    djc.makeSet(i)
for i in range(0, 31):
    djc.union(i, 2 * i)
for i in range(0, 21):
    djc.union(i, 3 * i)
for i in range(0, 13):
    djc.union(i, 5 * i)
for i in range(0, 61):
    djc.find(i)

print(djc.rank)
print(max(djc.rank))
print(djc.parent)
print(Counter(djc.parent).most_common(3))
