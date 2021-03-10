
def fab(n):
    if n in (0, 1):
        return n

    def _fab(running_sum, n_min_1, n_count):
        sum, n_min_1 = running_sum + n_min_1, running_sum
        if n_count == n:
            return sum
        return _fab(sum, n_min_1, n_count+1)

    res = _fab(1, 0, 2)
    return res


assert fab(0) == 0
assert fab(1) == 1
assert fab(2) == 1
assert fab(3) == 2
assert fab(4) == 3
assert fab(5) == 5
assert fab(6) == 8
assert fab(7) == 13


# (0, 1)  (1, 1) (2, 1)