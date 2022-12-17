def value(colors):
    color = {'black': '0', 'brown': '1', 'red': '2', 'orange': '3', 'yellow': '4',
             'green': '5', 'blue': '6', 'violet': '7', 'grey': '8', 'white': '9'}
    return int(color[colors[0]] + color[colors[1]])


print(value(['black', 'brown', 'orange']))
