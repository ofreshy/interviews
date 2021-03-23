"""

You are given a set and other sets.
Your job is to find whether set is a strict superset of each of the

sets.

Print True, if
is a strict superset of each of the

sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.

Example
Set
is a strict superset of set.
Set is not a strict superset of set.
Set is not a strict superset of set

.

Input Format

The first line contains the space separated elements of set
.
The second line contains integer , the number of other sets.
The next

lines contains the space separated elements of the other sets.

Constraints

Output Format

Print True if set
is a strict superset of all other sets. Otherwise, print False.

1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12

"""


def strict_superset(data):
    maybe_superset = set(data[0].strip().split(" "))
    for row in data[1:]:
        other_set = set(row.strip().split(" "))
        if len(maybe_superset) < len(other_set) or other_set - maybe_superset:
            return False

    return True


assert strict_superset(['1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78\n', '2\n', '1 2 3 4 5\n', '100 11 12']) is False
