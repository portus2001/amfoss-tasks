# Task-13

# Project Euler

## About

* **[Problem-1](https://www.hackerrank.com/contests/projecteuler/challenges/euler001)**
* **[Problem-2](https://www.hackerrank.com/contests/projecteuler/challenges/euler002)**
* **[Problem-3](https://www.hackerrank.com/contests/projecteuler/challenges/euler003)**
* **[Problem-4](https://www.hackerrank.com/contests/projecteuler/challenges/euler004)**
* **[Problem-5](https://www.hackerrank.com/contests/projecteuler/challenges/euler005)**

## How I Did

### Problem-1

#### Find the sum of all the multiples of 3 or 5 below N

* User is asked to input a number n.

* The formula given below will give the sum of multiples of any number m:

'''
**(m * n * (n + 1) // 2)** gives the sum of multiples of m
'''

### Problem-2

#### Find the sum of Even valued terms of the Fibonacci series less than N

* User is asked to input a number n.

* The value of f gives us the sum of the even numbers in the Fibonacci series:

'''
**f = 4 * t1 + t2**
'''
Here t1 is the sum of even numbers just before the number n and t2 is the sum of even numbers just before t1.

### Problem-3

#### Find the largest prime factor of a number N

* User is asked to input a number n.

* The number, n is converted to n/2 after each iteration in a while loop until n becomes an odd number.

* We put **int(math.sqrt(n)) + 1** instead of 'n' in a for loop, in order to reduce the time complexity.

### Problem-4

#### Find the largest palindrome made from the product of two 3-digit numbers which is less than N

* A for loop iterates from 100 to 1000.

* Inside the loop, there is another loop which iterates from 100 to 1000,

* The two loops are used to check whether multiplying the loop variables gets us a palindrome. If it does, then it is appended to a list.

* Then in another two nested for loops, we will check whether each element in the list is less than an inputted value by sorting the list and taking each element from the end of the loop. If it is less then we will print that element exit out of the loop.

### Problem-5

#### Find the smallest number which is divisible by all the numbers divisible from 1 to N

* Working of reduce function:

  * At first step, the first two elements of the sequence are picked and the result is obtained.
  * The next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
  * This process continues till no more elements are left in the container.
  * The final returned result is returned and printed on the console.
