# python3

import sys
import threading
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

        def compute_height_naive(self):
                # Replace this code with a faster implementation
                maxHeight = 0
                for vertex in range(self.n):
                        height = 0
                        i = vertex
                        while i != -1:
                                height += 1
                                i = self.parent[i]
                        maxHeight = max(maxHeight, height)
                return maxHeight


def fillDepth(parent, i, depth):

    # If depth[i] is already filled
    if depth[i] != 0:
        return

    # If node at index i is root
    if parent[i] == -1:
        depth[i] = 1
        return

    # If depth of parent is not evaluated before,
    # then evaluate depth of parent first
    if depth[parent[i]] == 0:
        fillDepth(parent, parent[i], depth)

    # Depth of this node is depth of parent plus 1
    depth[i] = depth[parent[i]] + 1


# This function reutns height of binary tree represented
# by parent array
def findHeight(parent):
    n = len(parent)
    # Create an array to store depth of all nodes and
    # initialize depth of every node as 0
    # Depth of root is 1
    depth = [0 for i in range(n)]

    # fill depth of all nodes
    for i in range(n):
        fillDepth(parent, i, depth)

    # The height of binary tree is maximum of all
    # depths. Find the maximum in depth[] and assign
    # it to ht
    ht = depth[0]
    for i in range(1, n):
        ht = max(ht, depth[i])

    return ht


def main():
    tree = TreeHeight()
    tree.read()
    # print(tree.compute_height_naive())
    print(findHeight(tree.parent))


threading.Thread(target=main).start()
