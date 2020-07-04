# Write code that will print out the anagrams (words that use the same
# letters) from a paragraph of text.
import random


word = "kanchan"
word = list(word)
print(word)
for words in word:
    random.shuffle(word)
    print(''.join(word))
    