def solve(expr):
    """Recursively solve the polish notation expression in the list `expr`.
    """
    operator = expr.pop(0)
    if operator in ("+", "-"):
        lhs = solve(expr)
        rhs = solve(expr)
        if operator == "+":
            return lhs + rhs
        else:
            return lhs - rhs
    else:
        # operator is actually a value; we are assuming
        # that the input expression is valid, so this
        # must be true
        return float(operator)


assert solve([e for e in "+ + 1 2 3" if e.strip()]) == 6
