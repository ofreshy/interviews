
from collections import defaultdict


def count_words(words):
    """
    You want to build a word cloud,
    an infographic where the size of a word corresponds to how often it appears in the body of text.

    :param words:
    :return:
    """
    counter = defaultdict(int)
    word_filter = make_word_filter()
    for word in words:
        word = normalize_word(word)
        if word_filter(word):
            continue
        counter[word] += 1
    word_counts = [(k, v) for k, v in counter.items()]
    return sorted(word_counts, key=lambda x: (x[1], x[0]))


def normalize_word(word):
    word = word or ""
    word = word.lower()
    word = "".join([c for c in word if c.isalnum()])
    return word


def make_word_filter():
    def is_empty(word):
        return not bool(word)

    def is_only_digits(word):
        return all(c.isdigit() for c in word)

    def is_prep(word):
        return word in ("in", "on", "after", "and", "or")

    filters = (is_empty, is_only_digits, is_prep)

    def word_filter(word):
        return any(
            f(word) for f in filters
        )

    return word_filter


assert count_words([]) == []
assert count_words([""]) == []
assert count_words(["word"]) == [("word", 1)]
assert count_words(["word", "Word", "WORD"]) == [("word", 3)]
assert count_words(["word,", "word.", "word!"]) == [("word", 3)]
assert count_words(["word", "on", "after"]) == [("word", 1)]
assert count_words(["word", "word!", "?word"]) == [("word", 3)]
assert count_words(["word", "1979"]) == [("word", 1)]
assert count_words(["word", "word-9"]) == [("word", 1), ("word9", 1)]


"""
Handle this !

'We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake.'
'The bill came to five dollars.'
'interest intereseting fill fealing '
"""