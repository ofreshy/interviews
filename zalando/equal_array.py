# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"


def solution(A):
    if not A:
        return -1

    solutions = []
    total_sum = sum(A)
    sum_up_to_i_minus_1 = 0
    sum_from_i_plus_1_to_n = total_sum
    for i in xrange(len(A)):
        sum_from_i_plus_1_to_n -= A[i]
        if sum_up_to_i_minus_1 == sum_from_i_plus_1_to_n:
            solutions.append(i)
        sum_up_to_i_minus_1 += A[i]

    return solutions[0] if solutions else -1


assert solution([]) == -1

assert solution([-1, 3, -4, 5, 1, -6, 2, 1]) == 1
