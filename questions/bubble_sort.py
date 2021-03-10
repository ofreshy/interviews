
def sort(l):
    for i in xrange(len(l)-1, 0, -1):
        exchanges = False
        for j in xrange(i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                exchanges = True
        if not exchanges:
            break
    return l

l = [9, 19, 0, 9, 18, 12]

assert sort(l) == [0, 9, 9, 12, 18, 19]
