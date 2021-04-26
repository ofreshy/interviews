
"""
A countdown sequence is a descending sequence of k integers from k down to 1 (e.g. 5, 4, 3, 2, 1). Write a function that returns a list [x, y] where x is the number that represents how many of countdown sequences are in a given list and y is a list of those sequences in order which they appear in the list.
Examples

final_countdown([4, 8, 3, 2, 1, 2]) ➞ [1, [[3, 2, 1]]]
# In this example we have 1 countdown sequence: 3, 2, 1

final_countdown([4, 4, 5, 4, 3, 2, 1, 8, 3, 2, 1]) ➞ [2, [[5, 4, 3, 2, 1], [3, 2, 1]]]
# We have 2 countdown sequences:
# 5, 4, 3, 2, 1 and 3, 2, 1

final_countdown([4, 3, 2, 1, 3, 2, 1, 1]) ➞ [3, [[4, 3, 2, 1], [3, 2, 1], [1]]]
# We have 3 countdown sequences:
# 4, 3, 2, 1 ; 3, 2, 1 and 1

final_countdown([1, 1, 2, 1]) ➞ [3, [[1], [1], [2, 1]]]

final_countdown([]) ➞  [0, []]
"""


def final_countdown(l):
    def add_to_sequences(rest, current_sequence, sequences):
        if not rest:
            return sequences

        element = rest[0]
        if not current_sequence or current_sequence[-1] == element+1:
            current_sequence.append(element)
        else:
            current_sequence = [element]

        if current_sequence[-1] == 1:
            sequences.append(current_sequence)
            current_sequence = []

        return add_to_sequences(rest[1:], current_sequence, sequences)

    answer = add_to_sequences(l, [], [])
    return [len(answer), answer]


print(final_countdown([2,5,4,3,2,1,2]))
assert final_countdown([2,5,4,3,2,1,2]) == [1, [[5, 4, 3, 2, 1]]]
assert final_countdown([]) == [0, []]
assert final_countdown([1]) == [1, [[1]]]
assert final_countdown([1, 1, 2, 1]) == [3, [[1], [1], [2, 1]]]
assert final_countdown([4, 3, 2, 1, 3, 2, 1, 1]) == [3, [[4, 3, 2, 1], [3, 2, 1], [1]]]
assert final_countdown([5,4,3,2,1]) == [1, [[5, 4, 3, 2, 1]]]
