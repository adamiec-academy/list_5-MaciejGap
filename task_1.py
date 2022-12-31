def longest_word():
    long = ""
    data = []
    for line in open("words.txt", encoding="utf-8"):
        data.append(line.strip())
    for word in data:
        if len(word) > len(long):
            long = word
    return long
