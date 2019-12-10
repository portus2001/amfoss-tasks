t = int(input())
for i in range(t):
    n = int(input())
    a = (n - 1) // 3#Gives the number of multiples of 3
    b = (n - 1) // 5#Gives the number of multiples of 5
    c = (n - 1) // 15#Gives the number of multiples of 15
    s = (3 * a * (a + 1) // 2) + (5 * b * (b + 1) // 2) - (15 * c * (c + 1) // 2)
    print(s)"""(3 * a * (a + 1) // 2) gives the sum of multiples of 3
               (5 * b * (b + 1) // 2) gives the sum of multiples of 5
               (15 * c * (c + 1) // 2) gives the sum of the multiples of 15
            """   
    
