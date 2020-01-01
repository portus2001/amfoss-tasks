# amFOSS-tasks

# Table Of Contents

TASK                                                                      |  DESCRIPTION
--------------------------------------------------------------------------|----------------------------------------------------
[Task-0](https://github.com/portus2001/amfoss-tasks/tree/master/task-0)   | Installing Ubuntu
[Task-1](https://github.com/portus2001/amfoss-tasks/tree/master/task-1)   | Script to star all repos of amfoss
[Task-2](https://github.com/portus2001/amfoss-tasks/tree/master/task-2)   | Codeforces and Hackerrank problems
[Task-3](https://github.com/portus2001/amfoss-tasks/tree/master/task-3)   | Google Scraping using Ruby
[Task-4](https://github.com/portus2001/amfoss-tasks/tree/master/task-4)   | Advanced XOR
[Task-5](https://github.com/portus2001/amfoss-tasks/tree/master/task-5)   | Get it using JavaScript
[Task-6](https://github.com/portus2001/amfoss-tasks/tree/master/task-6)   | CLI app using GO
[Task-7](https://github.com/portus2001/amfoss-tasks/tree/master/task-7)   | Rust program to check validity of a mail address
[Task-8](https://github.com/portus2001/amfoss-tasks/tree/master/task-8)   | Captcha breaking using python
[Task-9](https://github.com/portus2001/amfoss-tasks/tree/master/task-9)   | Personal website in github pages
[Task-10](https://github.com/portus2001/amfoss-tasks/tree/master/task-10) | CS50
[Task-11](https://github.com/portus2001/amfoss-tasks/tree/master/task-11) | Pong game
[Task-12](https://github.com/portus2001/amfoss-tasks/tree/master/task-12) | Python Source
[Task-13](https://github.com/portus2001/amfoss-tasks/tree/master/task-13) | Project Euler
[Task-14](https://github.com/portus2001/amfoss-tasks/tree/master/task-14) | Bandit

# Task-0

# Install Ubuntu 18.04

As I am a Mac user, I had to skip this task as advised by my respectful senior, Harshith Pabbati.

# Task-1

# Star all amfoss repositories

## How I Did

* Followed the **[link](https://github.com/amfoss/star-me)**.
* Copied the script.
* Opened Deeloper Tools using **<kbd>⌘</kbd>+<kbd>⌥</kbd>+<kbd>I</kbd>** and pasted the copied script.
* Pressed enter to run the script.

## Screenshot of my work

![Alt text](star.png)

# Task-2

# Programming

This folder contains some programming tasks given in amFOSS.

There are two subfolders in which one contains problems from codeforces and other contain problems from hackerrank.

## Codeforces

CODEFORCES          |  LINK
--------------------|-----------------------------------------------
Theatre Square      | **[Theatre Square](http://codeforces.com/problemset/problem/1/A)**
Way Too Long Words  | **[Way Too Long Words](http://codeforces.com/problemset/problem/71/A)**
Next Round          | **[Next Round ](http://codeforces.com/problemset/problem/158/A)**
Bit++               | **[Bit++](http://codeforces.com/problemset/problem/282/A)**
Football            | **[Football](http://codeforces.com/problemset/problem/96/A)**

## Hackerrank

HACKERRANK             |  LINK
-----------------------|----------------------------------------------------------------------
Compare the Triplets   | **[Compare the Triplets](https://www.hackerrank.com/challenges/compare-the-triplets/problem)**
Diagonal Difference    | **[Diagonal Difference](https://www.hackerrank.com/challenges/diagonal-difference)**
Staircase              | **[Staircase](https://www.hackerrank.com/challenges/staircase/problem)**
Birthday Cake Candles  | **[Birthday Cake Candles](https://www.hackerrank.com/challenges/birthday-cake-candles/problem)**
Time Conversion        | **[Time Conversion](https://www.hackerrank.com/challenges/time-conversion/problem)**

# Codeforces

1. Theatre Square

   * The length and breadth of the rectangle and the side of the square are inputted from the user.
   * A function is used to calculate the number of squares needed to completely cover the rectangle.
   * We find the area of the rectangle and divide it by the area of the square.
   * We use ceil function to convert the value that we get after division to get the next possible integer number.
   * This value gives us the number of flagstones.

2. Way Too Long Words

   * The number of words and the words itself is input by the user.
   * Each of the strings is iterated through a for loop.
   * If the length of the string is greater than 10 then the word is manipulated as the first character, string length-2 the last character and is stored in a list.
   * Similarly we do this process to each inputted string.
   * Using another for loop, we output all the elements in the list one by one.

3. Next Round

   * The number of teams, the position k and the scores of the teams in descending order are input by the user.
   * A loop is used to iterate over each of the scores stored in an array.
   * If the score is greater than or equal to the score of the kth team and the if the score is positive(>0) then a variable num, which is the number of teams which will advance in the next round, is incremented.
   * Num is displayed which is the required output.

4. Bit++

   * The number of statements and the statements are input by the user.
   * Each of the statements is stored in a list.
   * We will then print the sum of the count of "X++" and count of "++X" and count of "X--" and count of "--X", which will give us the output.

5. Football

   * The string which contains 0s and 1s is input by the user.
   * If "0000000" or "00000000" or "000000000" or "0000000000" or "00000000000" or "1111111" or "11111111" or "111111111" or "1111111111" or "11111111111" is there in string, we will then print "YES".
   * Else we will print "NO".

# HackerRank

1. Compare the Triplets

   * Three arrays are created, to store the ratings of Alice and Bob in the first two and the final score of both in the third array.
   * Ratings of both Alice and Bob are input by the user.
   * A function is used to compare the ratings of Alice and Bob and increment the score of the person a higher rating.
   * The score of Alice and Bob is printed.

2. Diagonal Difference

   * The user inputs the number of rows and columns of the square and its elements.
   * A function is used to calculate the sum of primary and secondary array. Let x be first index and y be the second. Then:
      * Primary diagonal y == x
      * Secondary diagonal y == n-x-1
   * Then their difference is calculated and printed.

3. Staircase

   * The user input a single integer n.
   * A function is used which prints the required staircase pattern.
   * A nested loop is used in which the outer loop and inner loop executes n times but "#" is printed only when the inner loop variable is greater than an else prints " ", where a is equal to n-1 and is decremented after each outer loop execution.
   * This prints the required pattern.

4. Birthday Cake Candles

   * The user inputs the number of Candles and then all the heights of the candles.
   * A function is used to find the number of tallest candles.
   * A for loop is used to find the tallest candle from an array.
   * Another function is used to count the number of tallest candles which would be equal to the height found earlier.
   * This count is displayed which is the required output.

5. Time Conversion

   * The user inputs time in 12 Hours format.
   * A function is used to convert the time in 12-hour format to 24-hour format.
   * The whole string containing the time is copied into a new string except the AM-PM part.
   * But if the time is AM and the hour is 12 then the new time is assigned with two zero and the remaining minutes and seconds part.
   * But if the time is AM and the hour is not 12 then the time will remain unchanged.
   * On the other hand, if time is PM and the hour is less than 12 then the hours is added to 12 and assigned along with the minutes and seconds part.
   * But if the time is PM and the hour is 12 then the time will remain unchanged.

# Task-3

# Google Scraping using Ruby

## About

Given a keyword example, ”Linux”, you need to get the top 10 Google search results for the given particular word. You can use Ruby for doing this task. Ruby has a gem (library), nokogiri which is an HTML, CSS and XML parser. 
Here is the **[link](https://github.com/sparklemotion/nokogiri)**.

## Blockers

I had a problem with finding the correct **XPath selector**. The task became easy for me when I finally found out the right XPath selector.

# Task-4

# Advanced XOR

## How did I do it

   * First I went through the encryption script "xor_adv.py" and learnt how encryption is actually working.
   * Learnt about functions like encode(), decode(), urandom().
   * Learnt a lot about the use of importing hashlib, urandom and also about the use of "hex".
   * Tried taking all alphabets and making combinations for plaintext, but later realized that it would take a very long time.
   * So I made a list of several alphabets in such a way that this particular cyphertext can be decoded in a very less time.
   * Finally got it after after several attempts.
   
# Task-5

# Get it using Javascript

## About

* In this task, we need to generate a web page using the **GitHub API** by using **GraphQL** for accessing the data.
  **https://developer.github.com/v4/**
* Write a function to take GitHub username as an argument and display the information of the user (anyone valid information). If no user exists, return “No person exists”.
      1. Username
      2. Name
      3. Avatar
      4. Bio
      5. Identicon
* Here is the link for my Github Profile Finder: **[link](https://portus2001.github.io/GITHUB-PROFILE-FINDER/)**

# Task-6

# CLI App using Go

## About 

The task is to build a command-line tool that prints the details (count of followers, user handle, etc) of a Twitter user using the flags package in **Go**.You must give the Twitter handle as input to the flag. The output must be written to a text file (learn about file handling in Go).
Resources:
  * **https://tour.golang.org/**  (basic understanding of Go syntax)
  * **https://gobyexample.com/command-line-flags**  (learn about the flags package)

## How I Did

* I applied for a **twitter developer account** to get the Consumer key, Consumer secret, Token key, Token secret, as these were needed to retrieve the information of any twitter user.
* I refered to the following you tube videos to get a basic understanding of the Go language.
  * **https://www.youtube.com/watch?v=Q0sKAMal4WQ**
  * **https://www.youtube.com/watch?v=C8LgvuEBraI**
* Imported several packages like **dghubble**, which was necessary to run the program.

## How To Run The Program

* In order to run the program we have to enter the following command into the terminal
'''
**run twittercli.go**
'''

# Task-7

# Rusted Email

## About

Write a program in Rust to find whether the given input is an email or not.
Example: good@email.com is a **VALID EMAIL**.

## How I Did

* Went through **[Regex link](https://docs.rs/regex/1.1.9/regex/)** and understood about regex.

* Learnt the basics of rust programming with the help of this **[link](https://www.youtube.com/watch?v=zF34dRivLOw)**.

* Learnt the syntax of an email with the help of this **[link](https://help.returnpath.com/hc/en-us/articles/220560587-What-are-the-rules-for-email-address-syntax-)**.

* Created a regex crate in rust and made a default format of email ID.

* Input is then compared to the default email format using **is_match** function.

* If the inputted string(the email id) satisfies the regex, it prints **"Email Address is Valid."**, else prints **"Email Address is Invalid."**


# Task-9

# Setup a Simple Personal Website

## About

The task was to create our personal portfolio and blog.

## How I Did

* Learnt:
  * HTML from this **[link](https://www.w3schools.com/html/default.asp)**.
  * CSS from this **[link](https://www.w3schools.com/css/css_intro.asp)**.

* Learnt how to create a website by watching this youtube **[link](https://www.youtube.com/watch?v=uyaV_EWWRmo)**.

## My Website

Here is the **[link](https://portus2001.github.io)** to my personal website.

# Cash

## About

Implement a program that calculates the minimum number of coins required to give a user change.

## How I Did

* User is asked to input the amount.

* Using a **do-while loop**, the user is again asked to input, if he gives a negative value as the amount.

* The number of **dollars are converted into cents** by multiplying the amount with 100.

* A **while** loop is used, which iterates until the amount is equal to zero.

* After each iteration, the **amount is decremented by 25 or 10 or 5 or 1**, based on the current value of amount.

* A counter is set up such that after each iteration the counter gets incremented by one.

* After all the iterations the value of the counter is printed, which gives us the minimum number of coins.

# Task-10

# Hello

## About

Implement a program that prints out a simple greeting to the user, as per the name input by the user.

## How I Did

* Took an input from the user to enter a name.
* Printed hello with the inputted name.

# Mario

## About

Implement a program that prints out a half-pyramid of a specified height.

## How I Did

* User is asked to input the height of the pyramid.

* If the user enters any number which is less than zero, or greater than 23, then the user is again asked to input height using a **do while** loop.

* Using a **for** loop, where a variable is incremented till the height of the pyramid.

* Inside the for loop, another **two for loops** are used where one is used to print space and the other is used to print "#".

# Caesar

## About

Implement a program that encrypts messages using Caesar’s cipher, per the below.

'''
$ ./caesar 13
plaintext:  HELLO
ciphertext: URYYB
'''

## How I Did

* The program first checks if the program was run with a single argument and if each character of the argument is an integer.

* Converts the string into an Integer k using **atoi()**. If it is greater than 26 converts into k%26.

* User is asked to input the plaintext.

* Then a loop iterates over each charecter and increments by k preserving its case or leaves it as it is if not an alphabet.

* Loops over the plaintext and output ciphertext by using the below method:

'''
**cyphertext[i] = (plaintext[i] - ('a'or 'A') + k) % 26 + ('a'or 'A'))**
'''

# Vigenere

## About

Implement a program that encrypts messages using Vigenère’s cipher, per the below.

'''
$ ./vigenere ABC
plaintext:  HELLO
ciphertext: HFNLP
'''
## How I Did

* The program first checks if the program was run with a single argument and if each character of the argument is an integer.

* Converts the string into an Integer k using **atoi()**. If it is greater than 26 converts into k%26.

* User is asked to input the plaintext.

* Uses a for loop to iterate over each character of the plaintext and the key is also iterated along with it.

* Loops over the plaintext and output ciphertext by using the below method:

'''
**cyphertext[i] = (plaintext[i] - ('a'or 'A') + k) % 26 + ('a'or 'A'))**
'''

# Music

## About

Implement duration(), frequency() and is_rest() in helpers.c.

## How I Did

* This task was a bit difficult for me. So I referred to this **[link](https://github.com/atclarkson/CS50/blob/master/pset3/music/helpers.c)** in GitHub and understood the code.

# Task-11

# A Pong game

## About

To create a clone of Pong using Javascript (minimal GUI is enough).
    * It should be multiplayer.
    * It can be offline.

## My work

I have hosted the game in my **[website]( https://portus2001.github.io/Pong/)**.
I hope that you will like my work!

# task-12

# Python Source

## About

  * In this challenge, we are expected to find a string whose hash is similar to a given hash in the program, which when passed as input to program produces the output **"You are a Genius"**

  * Download the python code **[here](https://drive.google.com/file/d/0B3sOPp4yzeLTdHZiazhmNFZ2VEE/view?usp=sharing)**.

## How I Did

* Imported **string**.

* Defined three functions:
   * **xor()**- Which will **perform xor** operations on the characters.

   * **decode()**- Which will decode the binary characters **into ASCII**.

   * **shift()**- Which decrements the character,according to whether it is a digit or an alphabet,by 3.

* In ordre to decode, we have to use the three functions in the given way below:
    '''
    **your_code = "".join(shift(xor(decode(x))))**
    '''
* By doing this, we will be getting a string, which will then be printed.

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

# Task 14

# Bandit

## About

* Complete Bandit till level 10.

* Refer this **[link](http://overthewire.org/wargames/bandit/)**.

* The task is all about linux terminal commands.

* View **[passwords](https://github.com/portus2001/amfoss-tasks/blob/master/task-14/Bandit%20game%20passwords.md)** for Bandit.
