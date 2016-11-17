#!/usr/bin/python
# -*- coding: utf-8 -*-

import random


def randomised_quicksort(array, start=0, end=-1):
    if end == -1:
        end = len(array) - 1

    if start < end:
        midpoint = random_partition(array, start, end)
        randomised_quicksort(array, start, midpoint - 1)
        randomised_quicksort(array, midpoint + 1, end)


def random_partition(array, start, end):
    pivot_index = random.randint(start, end)
    pivot = array[pivot_index]

    array[pivot_index], array[end] = array[end], array[pivot_index]
    pivot_index = end

    i = start - 1
    for j in range(start, end):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[pivot_index] = array[pivot_index], array[i + 1]

    return i + 1


def counting_sort(array):
    maximum = max(array)
    result_set = [0 for _ in range(maximum + 2)]
    tallies = [0 for _ in range(maximum + 2)]

    for i in array:
        tallies[i] += 1

    for i in range(1, maximum + 1):
        tallies[i] += tallies[i - 1]

    for i in array:
        result_set[tallies[i] - 1] = i
        tallies[i] -= 1

    return [result_set[i] for i in range(len(array))]


def radix_sort(array):
    exponent = 1
    maximum = max(array)

    while maximum / exponent > 0:
        stable_sort(array, exponent)
        exponent *= 10


# A specialised version of counting sort
def stable_sort(array, exponent):
    array_size = len(array)
    result_set = [0 for _ in array]
    tallies = [0 for _ in range(10)]

    for element in array:
        tallies[(element / exponent) % 10] += 1

    for i in range(1, 10):
        tallies[i] += tallies[i - 1]

    i = array_size - 1
    while i >= 0:
        index = array[i] / exponent
        result_set[tallies[index % 10] - 1] = array[i]
        tallies[index % 10] -= 1
        i -= 1

    for i in range(array_size):
        array[i] = result_set[i]


def main():
    array = [9, 8, 3, 2, 2, 1, 0, 1, 9, 21, 10]

    randomised_quicksort(array)
    print "Problem one: %r" % array

    random.shuffle(array)
    print "Problem two: %r" % counting_sort(array)

    random.shuffle(array)
    radix_sort(array)
    print "Problem three: %r" % array


if __name__ == "__main__":
    main()
