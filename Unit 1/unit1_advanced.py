def words_with_char(words, x):
    result = []

    idx = 0
    for word in words:
        if x in word:
            result.append(idx)

        idx += 1

    return result


words = ["batman", "superman"]
x = "a"
print(words_with_char(words, x))

words = ["black panther", "hulk", "black widow", "thor"]
x = "a"
print(words_with_char(words, x))
