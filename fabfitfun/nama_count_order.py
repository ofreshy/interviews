
from collections import defaultdict
from operator import itemgetter


def order(names):
    """
    Iterable of names
    :param names: list of names
    :return: the name that happens most frequently in the list. If there is a tie, name with highest lexical order
    """
    names_dict = defaultdict(int)
    for name in names:
        names_dict[name] += 1

    ordered_names = sorted(names_dict.items(), key=itemgetter(1, 0))
    return ordered_names[-1][0]


assert order(("Ben", )) == "Ben"
assert order(("Ben", "Valery", "Ben")) == "Ben"
assert order(("Ben", "Valery", "Ben", "Valery")) == "Valery"

