'''
Write a Python function to check whether a string is a pangram or not. Go to the editor
Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"
'''
# 1.sprawdź czy zdanie ma chocia raz wystepującą kazdą literę alfabetu
# 2. napisz w zmiennej wszystkie litery alfabetu
# 3. stworz for loopa i przejdz przez wszystkie litery w alphabecie i porownaj ze zdaniem
# 4. jezeli jakiejś litery z alfabetu nie ma w zdnaniu, zwróc false


def pangram(sentence):
    alphabet = 'abcdefghijklmnopqrstuwvxyz'
    for char in alphabet:
        if char not in sentence.lower():
            return False
    return True


sentence = 'The quick brown fox jumps over the lazy dog'
print(pangram(sentence))
