x = int(input())
lst = []
for _ in range(x):
    s = input()
    n = (s[0] + str(len(s) - 2) + s[-1] if len(s) > 10 else s)
    lst.append(n)
for i in range(x):
    print(lst[i])
