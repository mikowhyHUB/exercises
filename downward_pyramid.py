'''
Print downward Half-Pyramid Pattern with Star (asterisk)
'''

for i in range(6):
    for j in range(6, i, -1):
        print('*', end=' ')
    print('\n')
