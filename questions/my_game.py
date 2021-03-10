"""
Imagine a game where the player needs to shoot darts on a target-board.
Now imagine that there are different areas on the board, each corresponds to a different action.

This question starts easy and go harder with each extension.
It is important in each one to see if the candidate asks relevant questions,
and encourage them to discuss their approach (stack, recursive, mutation vs immutability etc.)

1. Write a function that calculates the total score, if each area on the board correspond to a different value

2. As 1, only now there are two special areas:
   a. A - means double last score
   b. Z - means delete last score

   Note to interviewer : Does candidate discuss the approach.
   What happens when there are multiple letters in succession.
   e.g. Does ZZ means delete the delete, and AA double the last double? (YES IMO)
        Important to see if candidate raises this
   Can we think in advance of some test cases ?

3. As 2 - only now a new area was added:
   a. N - double next score
"""


def display_v1(areas):
    """
    All values are numbers so just sum them up

    :param areas:
    :return:
    """
    return sum(areas)


def display_v2(areas):
    values = []
    for v in areas:
        if v == "A":
            if values:
                values.append(values[-1] * 2)
            continue
        if v == "Z":
            if values:
                values.append(values[-1] * -1)
            continue
        else:
            values.append(v)
    return sum(values)


def display_v3(values):
    stack = []
    for v in values:
        if v == "A":
            if stack and str(stack[-1]).isdigit():
                stack.append(stack[-1])
        elif v == "Z":
            if stack:
                stack.pop()
        elif v == "N":
            stack.append(v)
        else:
            # v is a digit
            if not stack or stack[-1] != "N":
                stack.append(v)
            else:
                stack.pop()
                stack.append(v * 2)
    # We may still have N's in the stack
    return sum([n for n in stack if n != "N"])


# Test case for v 1
assert display_v1([]) == 0
assert display_v1([1]) == 1
assert display_v1([1, 10]) == 11


# Test case for v 2
assert display_v2([]) == 0
assert display_v2([1]) == 1
assert display_v2([1, 10]) == 11
# -- deletes
assert display_v2(["Z"]) == 0
assert display_v2([1, "Z"]) == 0
assert display_v2([1, 10, "Z"]) == 1
# -- doubles
assert display_v2(["A"]) == 0
assert display_v2([1, "A"]) == 3
assert display_v2([1, 10, "A"]) == 31
# -- double and deletes interaction
assert display_v2(["A", "Z"]) == 0
assert display_v2([1, "A", "Z"]) == 1
assert display_v2([1, 10, "A", "Z"]) == 11
assert display_v2([1, 10, "Z", "A"]) == 3
# -- delete the delete
assert display_v2([1, 10, "Z", "Z"]) == 11



# # Test case for v 3
# assert display_v3([]) == 0
# assert display_v3([1]) == 1
# assert display_v3([1, 10]) == 11
# # -- deletes
# assert display_v3(["Z"]) == 0
# assert display_v3([1, "Z"]) == 0
# assert display_v3([1, 10, "Z"]) == 1
# # -- doubles
# assert display_v3(["A"]) == 0
# assert display_v3([1, "A"]) == 2
# assert display_v3([1, 10, "A"]) == 21
# # -- double and deletes interaction
# assert display_v3(["A", "Z"]) == 0
# assert display_v3([1, "A", "Z"]) == 1
# assert display_v3([1, 10, "A", "Z"]) == 11
# assert display_v3([1, 10, "A", "Z"]) == 11
# assert display_v3([1, 10, "Z", "A"]) == 2
# # Next interactions
# assert display_v3(["N"]) == 0
# assert display_v3(["N", "A"]) == 0
# assert display_v3(["N", "Z"]) == 0
# assert display_v3(["A", "N"]) == 0
# assert display_v3(["Z", "N"]) == 0
# assert display_v3(["N", "N"]) == 0
# assert display_v3([1, "N"]) == 1
# assert display_v3(["N", 1]) == 2
# assert display_v3(["N", 10, 1]) == 21
