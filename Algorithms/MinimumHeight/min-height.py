#!/usr/bin/env python3

def minimum_root_heights(n, edges):
    """Brute force method for finding minimum tree given a number of vertices and a list of connections. We will enumerate the different vertices as possible roots."""
    adj_l = adjacency_matrix_to_list(n, edges)  # Creating an adjacency list to be traversed uni-directionally
    heights = []
    for v in range(n):
        prev = {}
        prev[v] = True
        for neighbor in adj_l[v]:
            prev[neighbor] = True
            height = 0
            height = find_height(neighbor, adj_l, prev, height)
        heights.append(height)

    print(heights)
    return min(heights)


def find_height(v, adj_l, prev, height):
    height += 1
    orig_height = height
    if adj_l[v] is None:
        return height
    for neighbor in adj_l[v]:
        if neighbor not in prev:
            prev[neighbor] = True
            branch_height = find_height(neighbor, adj_l, prev, orig_height)
            if branch_height > height:
                height = branch_height

    return height


def adjacency_matrix_to_list(n, edges):
    """Takes an adjacency matrix and creates an adjacency list"""
    ret = [[] for i in range(n)]
    for edge in edges:
        ret[edge[0]].append(edge[1])
        ret[edge[1]].append(edge[0])

    return ret


def main():
    edges = [[1, 0], [1, 2], [1, 3]]
    n = 4
    root_vertex = minimum_root_heights(n, edges)
    print(root_vertex)


if __name__ == '__main__':
    main()
