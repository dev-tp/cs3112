#!/usr/bin/python
# -*- coding: utf-8 -*-

from Queue import PriorityQueue


# Problem 1
def heapsort(array):
    size = len(array) - 1

    for i in range(size / 2, -1, -1):
        heapify(array, i, size)

    for i in range(size, 0, -1):
        array[0], array[i] = array[i], array[0]
        size -= 1
        heapify(array, 0, size)


def heapify(array, index, size):
    left = index * 2
    right = left + 1
    largest = index

    if left <= size and array[left] > array[largest]:
        largest = left
    elif right <= size and array[right] > array[largest]:
        largest = right

    if largest != index:
        array[largest], array[index] = array[index], array[largest]
        heapify(array, largest, size)


# Problem 2
class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __cmp__(self, other):
        if self.value > other.value:
            return 1
        elif self.value < other.value:
            return -1
        return 0

    def __str__(self):
        nodes = ""
        node = self

        while node:
            nodes = nodes + "%s -> " % str(node.value)
            node = node.next
        nodes = nodes + "null"

        return nodes


def merge_k_lists(linkedlists):
    if linkedlists is None or len(linkedlists) == 0:
        return None

    queue = PriorityQueue()

    head = Node()
    pointer = head

    for linkedlist in linkedlists:
        if linkedlist:
            queue.put(linkedlist)

    while not queue.empty():
        node = queue.get()
        pointer.next = node
        pointer = pointer.next

        if node.next:
            queue.put(node.next)

    return head.next


def main():
    array = [3, 2, 1, 5, 4, 10, -21]
    heapsort(array)
    print "Problem 1: Implement Heapsort\n%r\n" % array

    print "Problem 2: Merge k lists"
    a = Node(1)
    a.next = Node(2)
    a.next.next = Node(4)
    print a

    b = Node(3)
    b.next = Node(5)
    b.next.next = Node(7)
    print b

    c = Node(6)
    c.next = Node(8)
    c.next.next = Node(9)
    print c

    print merge_k_lists([a, b, c])


if __name__ == "__main__":
    main()
