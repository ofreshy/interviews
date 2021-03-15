"""
Write a program that prints the numbers from 1 to 100.
But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
For numbers which are multiples of both three and five print “FizzBuzz”.
"""


def helper(digit: int):

    digit_mod_3 = digit % 3 == 0
    digit_mod_5 = digit % 5 == 0
    if digit_mod_3 and digit_mod_5:
        return "fizzbuzz"
    if digit_mod_3:
        return "fizz"
    if digit_mod_5:
        return "buzz"

    dig_str = str(digit)
    dig_contains_3 = "3" in dig_str
    dig_contains_5 = "5" in dig_str
    if dig_contains_3 and dig_contains_5:
        return "fizzbuzz"
    if dig_contains_3:
        return "fizz"
    if dig_contains_5:
        return "buzz"

    return str(digit)


def fizz_buzz():
    fizzbuzz = [helper(d) for d in range(1,101)]
    return ", ".join(fizzbuzz)


assert helper(1) == "1"
assert helper(2) == "2"
assert helper(3) == "fizz"
assert helper(5) == "buzz"
assert helper(6) == "fizz"
assert helper(9) == "fizz"
assert helper(10) == "buzz"
assert helper(13) == "fizz"
assert helper(15) == "fizzbuzz"
assert helper(53) == "fizzbuzz"

print(fizz_buzz())





