things = ["cat", "house", "dog", "apple", "pie", "lake"]

def is_short_word(word): # returns the string if its length
    if len(word) > 3:    # is greater than 3
        return word

print(list(filter(is_short_word, things)))


