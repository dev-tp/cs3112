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


# TODO: Optimise function to remove elements from dictionary. Time complexity is O(n^3)...
def free_tree_to_rooted_tree(free_tree):
    nodes = [node for level in free_tree for node in level if node != '_' and node != ' ']
    number_of_vertices = len(nodes)

    tree = {}
    for head in nodes:
        head_location = get_node_location_in_tree(head, free_tree)
        tree[head] = get_node_neighbours(head_location, free_tree)

    connected_nodes = [tree.keys()[0]]
    root = connected_nodes[0]
    for node in tree[root]:
        connected_nodes.append(node)

    print root
    print ' '.join(tree[root])

    previous_level = tree[root]
    # Two steps were deducted hence the root node and its children have already been displayed
    for _ in range(number_of_vertices / 2 - 2):
        current_level = []
        for node_name in previous_level:
            for node in tree[node_name]:
                if node not in current_level and node not in connected_nodes:
                    current_level.append(node)
                    connected_nodes.append(node)
        previous_level = current_level
        print ' '.join(current_level)


def get_node_location_in_tree(node, tree):
    for x in range(len(tree)):
        for y in range(len(tree[x])):
            if tree[x][y] == node:
                return (x, y)
    return (0, 0)


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

    shuffle(a)
    print a
    selection_sort(a)
    print str(a) + "; after selection sort\n"

    shuffle(a)
    print a
    insertion_sort(a)
    print str(a) + "; after insertion sort\n"

    free_tree_to_rooted_tree(["i_d_", "cbae", "hg_f"])


if __name__ == "__main__":
    main()