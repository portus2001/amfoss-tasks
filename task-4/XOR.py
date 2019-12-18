from os import urandom
from ctypes import CDLL
import string
import hashlib
lst = ['sabefgijklmnopqrtuvwyABCDEFGHIJKLMNOPQRSTVWXYZ', 'ANBCDEFGHIJKLMOQRSUVWXYZ', 'AMCDEFHIJKLNOPQRSTUWXYZ',
      'adbcefghijklmnopqrstuvyz', 'ahbdefgijklmnopquvwxyzABCDFGHIJKLMNOPQRSTUVWXYZ']
lst1 = [a + b + c + d + e for a in lst[0] for b in lst[1] for c in lst[2] for d in lst[3] for e in lst[4]] 
 # These are the  possible key combinations for faster compilation.
def xor_decrypt(ciphertext):
    k = 1
    for key in lst1:
        plaintext = ""
        hex_key = key.encode("hex")
        key_list = [hex_key[i] + hex_key[i + 1] for i in range(0, len(hex_key), 2)]
        for j in range(len(ciphertext)):
            plaintext += chr(ord(ciphertext[j]) ^ int(key_list[j%5], 16))       
        if hashlib.md5(plaintext).digest().encode("hex") == "067abbb88d2201a393ba660728f83b84":
            print("Plaintext is:"+" "+plaintext+" and the key length is:"+" " +str(len(key)))
            print("You are a Genius")
            break
        k += 1
ciphertext = "2a2138440b1c233d080d072b29441c1b2b6d250c052f23070d176e152b3a"
ciphertext = bytearray.fromhex(ciphertext).decode()
xor_decrypt(ciphertext)