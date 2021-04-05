import re

"""
A valid postal code

have to fulfill both below requirements:

must be a number in the range from to
inclusive.

    must not contain more than one alternating repetitive digit pair.

Alternating repetitive digits are digits which repeat immediately after the next digit. In other words, an alternating repetitive digit pair is formed by two equal digits that have just a single digit between them.

For example:

121426 # Here, 1 is an alternating repetitive digit.
523563 # Here, NO digit is an alternating repetitive digit.
552523 # Here, both 2 and 5 are alternating repetitive digits.

Your task is to provide two regular expressions regex_integer_in_range and regex_alternating_repetitive_digit_pair. Where:

regex_integer_in_range should match only integers range from
to

inclusive

regex_alternating_repetitive_digit_pair should find alternating repetitive digits pairs in a given string.

Both these regular expressions will be used by the provided code template to check if the input string

is a valid postal code using the following expression:

(bool(re.match(regex_integer_in_range, P))
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


"""

regex_integer_in_range = re.compile(r"^[1-9][0-9]{5}$")
regex_alternating_repetitive_digit_pair = re.compile(r"(\d)(?=\d\1)")


assert regex_integer_in_range.match("111111") is not None
assert regex_integer_in_range.match("999999") is not None
assert regex_integer_in_range.match("011111") is None
assert regex_integer_in_range.match("99999") is None
assert regex_integer_in_range.match("9999999") is None
assert regex_integer_in_range.match("abcdefg") is None
assert regex_integer_in_range.match("0123456") is None


assert regex_alternating_repetitive_digit_pair.findall("121426") == ["1"]
assert regex_alternating_repetitive_digit_pair.findall("523563") == []
assert regex_alternating_repetitive_digit_pair.findall("552523") == ["5", "2"]
assert regex_alternating_repetitive_digit_pair.findall("0123456") == []


def verify(p):
    v1 = bool(regex_integer_in_range.match(p))
    v2 = len(regex_alternating_repetitive_digit_pair.findall(p)) < 2
    return v1 and v2


assert verify("0123456") is False
assert verify("1000000") is False
assert verify("1013439") is False
assert verify("123456799") is False


assert verify("123456") is True
assert verify("101234") is True

