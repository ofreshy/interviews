
def longest_seq(l):
    n = len(l)
    if n < 2:
        return 0
    cn, ln = 0, 0
    for i in xrange(n-1):
        e1, e2 = l[i], l[i+1]
        if e2 > e1:
            cn += 1
            if cn > ln:
                ln = cn
        else:
            cn = 0
    return ln


assert longest_seq([]) == 0
assert longest_seq([1]) == 0
assert longest_seq([1, 1]) == 0
assert longest_seq([1, 2]) == 1
assert longest_seq([1, 2, 3]) == 2
assert longest_seq([1, 2, 3, 4]) == 3
assert longest_seq([1, 2, 3, 0, 4, 5, 6]) == 3


