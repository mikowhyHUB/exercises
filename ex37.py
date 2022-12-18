def response(hey_bob):
    if hey_bob == '' or hey_bob.isspace():
        return 'Fine. Be that way!'
    for words in hey_bob:
        if hey_bob.isupper() and '?' in hey_bob:
            return 'Calm down, I know what I\'m doing!'
        elif hey_bob.isupper():
            return 'Whoa, chill out!'
        elif hey_bob.endswith('?') or hey_bob.endswith('?   '):
            return 'Sure.'
        else:
            return 'Whatever.'


print(response('Okay if like my  spacebar  quite a bit?   '))
