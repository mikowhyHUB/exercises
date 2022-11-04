l = ["Python", "Java", "C++", "C#", "VB.Net", "Javascript"]
n = len(l)
l_odd = []
l_even = []

for i in range(0, n):
    if i % 2 == 0:
        l_even.append(l[i])
    else:
        l_odd.append(l[i])
print((l_even, l_odd))
