word_list = ["apple", "pear", "banana", "cherry", "orange"]
print(word_list)
print(type(word_list))

import random as r
word = r.choice(word_list)

print(word)

guess = input("Write a single letter")

if not guess.isalpha():
    print("The letter must be alphabetical")
else:
    print("Good guess!")