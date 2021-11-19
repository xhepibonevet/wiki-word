
def word_counter(words):
    count_words = {}
    for word in words:
        if len(word) > 1 and not word.isnumeric():
            if word in count_words:
                count_words[word] += 1
            else:
                count_words[word] = 1
    return dict(sorted(count_words.items(), key=lambda item: item[1]))
