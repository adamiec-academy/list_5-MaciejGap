def reversed_words():
    data = set()
    for line in open("words.txt", encoding="utf-8"):
        data.add(line.strip())
    reversed_words_pairs = []
    for word in data:
        reversed_word = word[::-1]
        pair = tuple(sorted((word, reversed_word)))
        if reversed_word in data and word != reversed_word and pair not in reversed_words_pairs:
            reversed_words_pairs.append(pair)
    reversed_words_pairs.sort()
    return reversed_words_pairs
