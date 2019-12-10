a = int(input())
for i in range(a):
    n = int(input())
    t1 = 2
    t2 = 0
    c = 0
    s = 0
    while t1 < n:
        s += t1
        f = 4 * t1 + t2#Value of f gives us the sum of the even numbers in the Fibonacci series. 
        t2 = t1
        t1 = f
    print(s)
