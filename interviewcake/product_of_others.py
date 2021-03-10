

def product_of_others(l):
    n = len(l)
    o = n * [1] 
    for i in xrange(1, n):
        o[i] = o[i-1] * l[i-1]

    ps = 1
    for i in xrange(n-1, -1, -1):
        o[i] = o[i] * ps
        ps *= l[i]

    return o


assert product_of_others([1, 7, 3, 4]) ==  [84, 12, 28, 21]
assert product_of_others([1, 7, 3, 0]) ==  [0, 0, 0, 21]
