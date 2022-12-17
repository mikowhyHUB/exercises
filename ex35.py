def is_pangram(sentence):
    pangram = 'abcdefghijklmnopqrstuvwxyz'
    for letter in pangram:
        if letter not in sentence.lower():
            return False
    return True


print(is_pangram('The quick brown fox JUMPS over the lazy dog'))
