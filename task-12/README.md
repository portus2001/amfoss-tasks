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

