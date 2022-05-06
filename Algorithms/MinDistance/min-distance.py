#!/usr/bin/env python3

import copy
import math
import random


class Point:
    def __init__(self, x_init: int, y_init: int):
        self.x = x_init
        self.y = y_init

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __repr__(self):
        return "".join(["(", str(self.x), ",", str(self.y), ")"])

    def __str__(self):
        return "(%s,%s)" % (self.x, self.y)


def dist(p1, p2):
    return math.sqrt((p1.x - p2.x) *
                     (p1.x - p2.x) +
                     (p1.y - p2.y) *
                     (p1.y - p2.y))


def brute_force(p: list, n: int):
    min_val = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            if dist(p[i], p[j]) < min_val:
                min_val = dist(p[i], p[j])

    return min_val


def strip_closest(strip, strip_size, upper_bound):
    min_val = upper_bound

    for i in range(strip_size):
        j = i + 1
        while j < strip_size and (strip[j].y - strip[i].y < min_val):
            min_val = dist(strip[i], strip[j])
            j += 1

    return min_val


def closest_utility(p, q, n):
    if n <= 3:
        return brute_force(p, n)

    mid = n // 2
    mid_point = p[mid]

    pl = p[:mid]
    pr = p[mid:]

    dl = closest_utility(pl, q, mid)
    dr = closest_utility(pr, q, n - mid)

    d = min(dl, dr)

    strip_p = []
    strip_q = []

    lr = pl + pr
    for i in range(n):
        if abs(lr[i].x - mid_point.x) < d:
            strip_p.append(lr[i])
        if abs(q[i].x - mid_point.x) < d:
            strip_q.append(q[i])

    strip_p.sort(key=lambda point: point.y)
    min_a = min(d, strip_closest(strip_p, len(strip_p), d))
    min_b = min(d, strip_closest(strip_q, len(strip_q), d))

    return min(min_a, min_b)


def closest(p, n):
    """
    Find the minimum distance between two points

    Parameters
    ----------
    p: List[Point]
        list of points to check
    n: int
        size of p

    """
    p.sort(key=lambda point: point.x)  # sort array by x
    q = copy.deepcopy(p)
    q.sort(key=lambda point: point.y)  # sort array by y

    return closest_utility(p, q, n)


if __name__ == "__main__":
    points = []
    for i in range(5):
        point = Point(random.randint(0, 200), random.randint(0, 200))
        print(f"Point #{i} is {dist(Point(0.0, 0.0), point)} units away from origin")
        points.append(point)

    size = len(points)
    print(f"Starting array: {points}\n")

    result = closest(points, size)
    print(f"Simon says closest distance between two points is {result} units away")
