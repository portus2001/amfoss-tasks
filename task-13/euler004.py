lst = []
for i in range(100, 1000):
    for j in range(100, 1000):
        a = i * j
        if str(a) == str(a)[::-1] and a not in lst:
            lst.append(a)
lst.sort()
n = int(input())
for l in range(n):
    a = int(input())
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] < a:
            print(lst[i])
            break
