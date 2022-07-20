import sys
a = {x: x**2 for x in range(1, 5)}
print(a, type(a))
print(*a.items())
d = [1, 2, '1', '2', -4, 3, 4]
a = {int(x) for x in d if int(x) > 0}
print(a)
m = {'безнадежно': 0,'убого': 1,'неудовлет.': 2, 'удовлет.': 3, 'хорошо': 4, 'отлично': 5}
a = {key.title(): int(value) for key, value in m.items()}
print(a)
b = {int(value): key for key, value in m.items() if 2 <= int(value) <= 5}
print(b)


# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_a = [x.split(': ') for x in lst_in]
d = {}
for j in lst_a:
    if j[0] not in d:
        d[j[0]] = {j[1]}
    d[j[0]].add(j[1])
print(d)
