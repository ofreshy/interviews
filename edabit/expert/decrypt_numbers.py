"""
Given a string s consisting from digits and #, translate s to English lowercase characters as follows:

    Characters ("a" to "i") are represented by ("1" to "9").
    Characters ("j" to "z") are represented by ("10#" to "26#").
"""

def decrypt(s):
    def decrypt_inner(string, letters):
        if not string:
            return letters
        if len(string) > 2 and string[2] == "#":
            val = string[:2]
            rest = string[3:]
        else:
            val = string[:1]
            rest = string[1:]

        letters.append(chr(int(val) + 96))
        return decrypt_inner(rest, letters)
    return "".join(decrypt_inner(s, []))

assert decrypt("1") == "a"
assert decrypt("10#") == "j"
assert decrypt("10#11#12") == "jkab"
assert decrypt("1326#") == "acz"
assert decrypt("25#") ==  "y"