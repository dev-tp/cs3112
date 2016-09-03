#!/usr/bin/python
# -*- coding: utf-8 -*-


import random
import sys


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


def free_tree_to_rooted_tree(tree):
    nodes = [(tree[x][y], (x, y)) for y in range(len(tree[0])) for x in
             range(len(tree)) if tree[x][y] != '_' and tree[x][y] != ' ']

    adjacency_list = {}
    for head in nodes:
        adjacency_list[head[0]] = get_node_neighbours(head[1], tree)
    del head, nodes, x, y

    root, child_nodes = adjacency_list.popitem()
    print root
    print_rooted_tree(child_nodes, adjacency_list, 1, {})


def print_rooted_tree(nodes, adjacency_list, level, tree):
    level += 1
    for node in nodes:
        if node in adjacency_list:
            tree.setdefault(level, []).append(node)
            nodes = adjacency_list[node]
            del adjacency_list[node]
            print_rooted_tree(nodes, adjacency_list, level, tree)
        else:
            return

    for _, value in tree.items():
        for node in value:
            sys.stdout.write("%s " % node)
        print


def get_node_neighbours(node_location, tree):
    result = []
    x_bounds, y_bounds = len(tree), len(tree[0])

    if node_location[0] - 1 >= 0 and node_location[0] - 1 < x_bounds:
        top = tree[node_location[0] - 1][node_location[1]]
        if top != '_':
            result.append(top)

    if node_location[0] + 1 >= 0 and node_location[0] + 1 < x_bounds:
        bottom = tree[node_location[0] + 1][node_location[1]]
        if bottom != '_':
            result.append(bottom)

    if node_location[1] - 1 >= 0 and node_location[1] - 1 < y_bounds:
        left = tree[node_location[0]][node_location[1] - 1]
        if left != '_':
            result.append(left)

    if node_location[1] + 1 >= 0 and node_location[1] + 1 < y_bounds:
        right = tree[node_location[0]][node_location[1] + 1]
        if right != '_':
            result.append(right)

    return result


def main():
    a = [2 ** i for i in range(1, 12)]

    random.shuffle(a)
    print a
    selection_sort(a)
    print str(a) + "; after selection sort\n"

    random.shuffle(a)
    print a
    insertion_sort(a)
    print str(a) + "; after insertion sort\n"

    free_tree_to_rooted_tree(["i_d_", "cbae", "hg_f"])


if __name__ == "__main__":
    main()