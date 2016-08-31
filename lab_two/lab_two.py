#!/usr/bin/python
# -*- coding: utf-8 -*-


from random import shuffle


def selection_sort(a):
    for i in range(len(a) - 1):
        m = i  # (m)inimum value
        for j in range(i + 1, len(a)):
            if a[j] < a[m]:
                m = j
        if m != i:
            a[i], a[m] = a[m], a[i]


def insertion_sort(a):
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j - 1] > a[j]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1


def turn_free_tree_to_rooted():
    pass


def main():
    a = [2 ** i for i in range(1, 12)]

    shuffle(a)
    print a
    selection_sort(a)
    print str(a) + "; after selection sort\n"

    shuffle(a)
    print a
    insertion_sort(a)
    print str(a) + "; after insertion sort"


if __name__ == "__main__":
    main()