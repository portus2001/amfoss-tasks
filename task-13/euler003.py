import math
x = int(input())
for i in range(x):
    n = int(input())
    lst = []
    while n % 2 == 0:
        n = n / 2#after this while lopp the value of 'n' will be an odd number.
    for c in range(3, int(math.sqrt(n)) + 1, 2):#We put "int(math.sqrt(n)) + 1" instead of 'n', in order to reduce the time complexity.
        while n % c == 0: 
            lst.append(c)
            n = n / c
    if n > 2:
        lst.append(n)
    print(int(lst[-1]))
