from functools import reduce


def lcm(*lst):
    lst = list(lst)
    if lst:
        n = max(lst)
        m = n
        lst.remove(n)
        for i in lst:
            while n % i:
                n += m
        return n


x = int(input())
for i in range(x):
    a = int(input())
    print(reduce(lcm, range(1, a + 1)))

"""  Working of reduce function: 

At first step, first two elements of sequence are picked and the result is obtained.
Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
This process continues till no more elements are left in the container.
The final returned result is returned and printed on console.
"""
  
