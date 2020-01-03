# Caesar

## About

Implement a program that encrypts messages using Caesar’s cipher, as per below.

```c
$ ./caesar 13
plaintext:  HELLO
ciphertext: URYYB
```

## How I Did

* The program first checks if the program was run with a single argument and if each character of the argument is an integer.

* Converts the string into an Integer k using **atoi()**. If it is greater than 26 converts into k%26.

* User is asked to input the plaintext.

* Then a loop iterates over each charecter and increments by k preserving its case or leaves it as it is if not an alphabet.

* Loops over the plaintext and output ciphertext by using the below method:

```c
**cyphertext[i] = (plaintext[i] - ('a'or 'A') + k) % 26 + ('a'or 'A'))**
```
