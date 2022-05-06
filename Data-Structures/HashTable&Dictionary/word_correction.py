def edits1(word: str):
    """All edits that are one edit away from `word`."""
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transpose = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(inserts + deletes + transpose + replaces)


def edits2(word):
    return [e2 for e1 in edits1(word) for e2 in edits1(e1)]


def candidates(word, known):
    """
    Returns a list of spelling corrections that are 1 edit away, see edits1 for what types of edits there are

    :param word: word to make spelling recommendations for
    :param known: function that determines whether a word is spelled correctly or not
    :return: a list of words that are 1 edits away
    """
    ed1 = edits1(word)
    # ed2 = edits2(word)
    # all_candidates = set(ed1 + ed2)
    # known_words = known(list(all_candidates))
    known_words = known(list(ed1))
    return known_words


if __name__ == '__main__':
    print(edits1('smthing'))
