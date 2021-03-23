"""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string,
.
Both players have to make substrings using the letters of the string

.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string

.

For Example:
String
= BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

Print one line: the name of the winner and their score separated by a space.

If the game is a draw, print Draw.

"""


def minion_game(string):
    len_s = len(string)
    all_perms = (
        [string[i: j] for i in range(len_s) for j in range(i + 1, len_s + 1)]
    )
    vowels_sum = sum((1 for p in all_perms if p.startswith(("A", "I", "O", "U", "Y", "E"))))
    consonants_sum = len(all_perms) - vowels_sum

    if vowels_sum == consonants_sum:
        return "Draw"
    if vowels_sum > consonants_sum:
        winner = "Kevin"
        winning_sum = vowels_sum
    else:
        winner = "Stuart"
        winning_sum = consonants_sum

    return "{} {}".format(winner, winning_sum)


assert minion_game(string="ADA") == "Kevin 4"
assert minion_game(string="BANANA") == "Stuart 12"
