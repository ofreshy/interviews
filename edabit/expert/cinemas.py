"""
Given a list of seats, return the maximum number of new people which can be seated, as long as there is at least a gap of 2 seats between people.

    Empty seats are given as 0.
    Occupied seats are given as 1.
    Don't move any seats which are already occupied, even if they are less than 2 seats apart. Consider only the gaps between new seats and existing seats.

Examples

maximum_seating([0, 0, 0, 1, 0, 0, 1, 0, 0, 0]) ➞ 2
# [1, 0, 0, 1, 0, 0, 1, 0, 0, 1]

maximum_seating([0, 0, 0, 0]) ➞ 2
# [1, 0, 0, 1]

maximum_seating([1, 0, 0, 0, 0, 1]) ➞ 0
# There is no way to have a gap of at least 2 chairs when adding someone else.

Notes

    Notice how there may be several possibilities for assigning seats to people, but these cases won't affect the results.
    All seats will be valid.
"""


def maximum_seating(seats):
    new_seats = 0
    seats = [0, 0] + seats + [0, 0]
    for i in range(2, len(seats) - 2):
        seat_is_free = all([seats[j] == 0 for j in range(i, i+1)])
        ahead_is_free = all([seats[j] == 0 for j in range(i + 1, i + 3)])
        back_is_free = all([seats[j] == 0 for j in range(i - 2, i)])
        if seat_is_free and ahead_is_free and back_is_free:
            # Place a seat and increment counter
            seats[i] = 1
            new_seats += 1

    return new_seats


assert maximum_seating([0, 0, 0, 0]) == 2
assert maximum_seating([0, 0, 0, 1, 0, 0, 1, 0, 0, 0]) == 2
assert maximum_seating([1, 0, 0, 0, 0, 1]) == 0
