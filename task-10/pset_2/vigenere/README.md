# Vigenere

## About

Implement a program that encrypts messages using Vigenère’s cipher, as per below.

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

```c
**cyphertext[i] = (plaintext[i] - ('a'or 'A') + k) % 26 + ('a'or 'A'))**
```
