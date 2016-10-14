#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def bruteforce_maximum_subarray(array):
    maximum = 0
    for i in range(0, len(array)):
        current = 0
        for j in range(i, len(array)):
            current += array[j]
            if current > maximum:
                maximum = current
    return maximum


def divide_and_conquer_maximum_subarray(array, low, high):
    if low == high:
        return array[low]
    else:
        mid = (low + high) / 2
        return max(divide_and_conquer_maximum_subarray(array, low, mid),
                   divide_and_conquer_maximum_subarray(array, mid + 1, high),
                   maximum_crossing_subarray(array, low, mid, high))


def maximum_crossing_subarray(array, low, mid, high):
    current_left_sum = 0
    left_sum = -(sys.maxint)
    for i in range(mid, low - 1, -1):
        current_left_sum += array[i]
        if current_left_sum > left_sum:
            left_sum = current_left_sum

    current_right_sum = 0
    right_sum = -(sys.maxint)
    for i in range(mid + 1, high + 1):
        current_right_sum += array[i]
        if current_right_sum > right_sum:
            right_sum = current_right_sum

    return left_sum + right_sum


def main():
    a = [4, -1, 2, 1]
    print bruteforce_maximum_subarray(a)
    print divide_and_conquer_maximum_subarray(a, 0, len(a) - 1)


if __name__ == "__main__":
    main()
