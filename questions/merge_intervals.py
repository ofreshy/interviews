
def merge_intervals(intervals):
    if not intervals or len(intervals) == 1:
        return intervals

    intervals = sorted(intervals, key=lambda x: x[0])
    merged_intervals = [intervals[0]]
    for i in xrange(1, len(intervals)):
        last_merged = merged_intervals.pop()
        current_interval = intervals[i]
        merged = merge(last_merged, current_interval)
        merged_intervals.extend(merged)

    return merged_intervals


def merge(i1, i2):
    # overlap
    i1_min, i1_max = i1
    i2_min, i2_max = i2
    if i1_min == i2_min or i1_min == i2_min + 1:
        imax = max(i1_max, i2_max)
        return [[i1[0], imax]]

    if i1_max == i2_min or i1_max + 1 == i2_min:
        return [[i1_min, i2_max]]

    if i1_max >= i2_max:
        return [[i1_min, i1_max]]

    if i1_max > i2_min:
        return [[i1_min, i2_max]]

    if i1_max < i2_min - 1:
        return [i1, i2]


assert merge_intervals([]) == []
assert merge_intervals([[0, 1]]) == [[0, 1]]

assert merge_intervals(([[0, 1], [0, 5]])) == [[0, 5]]

assert merge_intervals(([[0, 1], [1, 5]])) == [[0, 5]]
assert merge_intervals(([[0, 1], [2, 5]])) == [[0, 5]]

assert merge_intervals(([[0, 1], [3, 5]])) == [[0, 1], [3, 5]]
assert merge_intervals(([[0, 1], [2, 5], [4, 8]])) == [[0, 8]]
assert merge_intervals(([[0, 7], [2, 5]])) == [[0, 7]]


