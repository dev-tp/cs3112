#!/usr/bin/python
# -*- coding: utf-8 -*-

def power(base, exponent):
    if exponent == 0:
        return 1

    total = power(base, exponent / 2)

    if exponent % 2 == 0:
        return total ** 2
    else:
        return base * total ** 2 if exponent > 0 else (total ** 2) / base


def merge_sort(array):
    array_length = len(array)
    side_array = [0 for i in range(array_length)]

    i = 1
    while i < array_length:
        j = 0
        while j < array_length:
            merge(array, j, min(i + j, array_length),
                  min(j + 2 * i, array_length), side_array)
            j += i * 2
        array = side_array[:]
        i *= 2

    return array


def merge(array, left_index, right_index, tip, side_array):
    i, j = left_index, right_index
    for k in range(left_index, tip):
        if i < right_index and (j >= tip or array[i] <= array[j]):
            side_array[k] = array[i]
            i += 1
        else:
            side_array[k] = array[j]
            j += 1


def binary_search(array, element):
    lowest_index, highest_index = 0, len(array) - 1

    while lowest_index <= highest_index:
        index_in_between = lowest_index + (highest_index - lowest_index) / 2
        if element < array[index_in_between]:
            highest_index = index_in_between - 1
        elif element > array[index_in_between]:
            lowest_index = index_in_between + 1
        else:
            return index_in_between

    return -1


def main():
    array = [5, 1, 3, 6, 21, 10, 35, 44, 12]
    print "Unsorder array: %r" % array
    array = merge_sort(array)
    print "Sorted array: %r" % array

    print "Found 21 at index: %d" % binary_search(array, 21)

    print "5^5 = %.0f" % power(5, 5)
    print "20^21 = %.0f" % power(20, 21)


if __name__ == "__main__":
    main()
