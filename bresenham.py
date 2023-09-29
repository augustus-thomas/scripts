from collections.abc import Iterator


# the base algo only works for |m| <= 1
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
    del_x = p2[0] - p1[0]
    del_y = p2[1] - p1[1]

    if abs(del_y) <= abs(del_x):
        return list(_bresenham_restricted(p1, p2))

    else:
        # swap x and y for |m| > 1
        def swap(point: tuple[int, int]) -> tuple[int, int]:
            return (point[1], point[0])
        return list(map(swap, _bresenham_restricted(swap(p1), swap(p2))))
