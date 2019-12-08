n, k = map(int, input().split())
a = list(map(int, input().split()))
c = 0
for i in range(n):
    if a[i] >= a[k - 1] and a[i] > 0:
        c = c + 1
print(c)
