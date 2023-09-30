from collections.abc import Iterator


# the base algo only works for 0 <= m <= 1
def _bresenham_restricted(p1: tuple[int, int], p2: tuple[int, int]) -> \
        Iterator[tuple[int, int]]:
    del_x = p2[0] - p1[0]
    del_y = p2[1] - p1[1]
    x, y = p1
    yield x, y

    p = 2 * del_y - del_x

    while x < p2[0]:
        if p < 0:
            x += 1
            yield x, y
            p += 2 * del_y
        else:
            x += 1
            y += 1
            yield x, y
            p += 2 * del_y - 2 * del_x


def bresenham_line(p1: tuple[int, int], p2: tuple[int, int]) -> \
        list[tuple[int, int]]:
    # transform input to acceptable m -> compute bresenham -> inverse transform

    # functions to apply to undo the transformations
    undos = []

    # have to draw left to right
    # this does not change the points, only the order; no need to undo
    if p1[0] > p2[0]:
        tmp = p1
        p1 = p2
        p2 = tmp

    # if drawing downward, flip it up
    if p2[1] < p1[1]:
        def flip_y(p):
            # flips y coordinate w.r.t. p1's y
            return (p[0], -(p[1] - p1[1]) + p1[1])
        p2 = flip_y(p2)
        undos.append(flip_y)  # flip_y is it's own inverse

    # if m is > 1
    if p2[1] - p1[1] > p2[0] - p1[0]:
        # swap x and y axes for m > 1
        def swap(p):
            return (p[1], p[0])
        p1 = swap(p1)
        p2 = swap(p2)
        undos.append(swap)  # swap is it's own inverse

    # single function to apply all undos
    def undo_all(point):
        for f in reversed(undos):
            point = f(point)
        return point

    return list(map(undo_all, _bresenham_restricted(p1, p2)))
