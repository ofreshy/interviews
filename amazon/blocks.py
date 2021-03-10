
def score_blocks(blocks, N=1):
    register = []
    for b in blocks:
        if b == "X":
            if register:
                register.append(2 * register[-1])
        elif b == "+":
            if not register:
                continue
            if len(register) == 1:
                register.append(register[-1])
            else:
                register.append(register[-1] + register[-2])
        elif b == "Z":
            if register:
                register = register[:-1]
        elif isinstance(b, int):
            register.append(b)
        else:
            raise ValueError("dont know what to do with block '%s'" % b)

    return sum(register)

assert score_blocks([], 1) == 0
assert score_blocks([1, 2], 1) == 3
assert score_blocks([10, -2], 1) == 8

assert score_blocks([1, "X"], 1) == 3
assert score_blocks([1, 2, "X"], 1) == 7
assert score_blocks([1, -2, "X"], 1) == -5
assert score_blocks(["X"], 1) == 0
assert score_blocks(["X", 1], 1) == 1


assert score_blocks(["+"], 1) == 0
assert score_blocks([1, "+"], 1) == 2
assert score_blocks([1, 5, "+"], 1) == 12
assert score_blocks([1, -2, "+"], 1) == -2
assert score_blocks([1, 2, "X", "+"], 1) == 13
assert score_blocks(["X", "+"], 1) == 0

assert score_blocks(["Z"]) == 0
assert score_blocks(["Z", "X", "+"]) == 0
assert score_blocks([1, "Z"]) == 0
assert score_blocks([1, 2, "Z"]) == 1
assert score_blocks([1, "X", "Z"]) == 1
assert score_blocks([1, 2, "+", "Z"]) == 3



