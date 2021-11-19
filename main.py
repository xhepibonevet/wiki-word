from articles import Article
from utils import word_counter


a = Article()
a.remove_nonchar()
a.lower_case()

words = a.list_words()
count_words = word_counter(words)

for word, counter in count_words.items():
    print(f"{word} -> {counter}")

