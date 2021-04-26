"""
Write a function that returns the longest non-repeating substring for a string input.

longest_nonrepeating_substring("abcabcbb") ➞ "abc"

longest_nonrepeating_substring("aaaaaa") ➞ "a"

longest_nonrepeating_substring("abcde") ➞ "abcde"

longest_nonrepeating_substring("abcda") ➞ "abcd"

"""


def longest_nonrepeating_substring(substring):
    last_seen = dict()
    last_rewind = 0
    current_substring = []
    longest_substring = []
    for i, s in enumerate(substring):
        if s not in last_seen:
            current_substring.append(s)
        else:
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
            last_rewind = max(last_rewind, last_seen[s])
            current_substring = list(substring[last_rewind+1:i+1])
        last_seen[s] = i

    if len(current_substring) > len(longest_substring):
        longest_substring = current_substring

    return "".join(longest_substring)


print(longest_nonrepeating_substring("ccdddcccc"))
assert longest_nonrepeating_substring("ccdddcccc") == "cd"
assert longest_nonrepeating_substring("kjlmjsdeee") == "lmjsde"
assert longest_nonrepeating_substring("abc") == "abc"
assert longest_nonrepeating_substring("abcabcbb") == "abc"
assert longest_nonrepeating_substring("aaaaaa") == "a"
assert longest_nonrepeating_substring("abcde") == "abcde"
assert longest_nonrepeating_substring("abcda") == "abcd"
