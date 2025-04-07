# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from math import sqrt
def vigenere_decrypt(ciphertext,key):
    plaintext = ''
    cipher_lst = [ord(c) - 65 for c in ciphertext]
    key_lst = [ord(c) - 65 for c in key]
    n = len(ciphertext)
    m = len(key)
    for i in range(n):
        plaintext += chr(65 + (cipher_lst[i] - key_lst[i%m])%26)

    print(plaintext)

def vigenere_encrypt(plaintext, key):
    ciphertext = ''
    plain_lst = [ord(c) - 65 for c in plaintext]
    key_lst = [ord(c) -65 for c in key]
    n = len(plaintext)
    m = len(key)
    for i in range(n):
        ciphertext+= chr(65 + (plain_lst[i]+key_lst[i%m])%26)
    print(ciphertext)

def vigenere_auto_encrypt(plaintext,key):
    ciphertext = ''
    plain_lst = [ord(c) - 65 for c in plaintext]
    key_lst = [ord(c) - 65 for c in key]
    n = len(plaintext)
    m = len(key)
    for i in range(m):
        ciphertext += chr(65 + (plain_lst[i]+key_lst[i])%26)
    for i in range(m,n):
        ciphertext += chr(65 + (plain_lst[i]+plain_lst[i-m])%26)

    print(ciphertext)

def vigenere_auto_decrypt(ciphertext, key):
    plaintext = ''
    cipher_lst = [ord(c) - 65 for c in ciphertext]
    key_lst = [ord(c) - 65 for c in key]
    n = len(ciphertext)
    m = len(key)
    for i in range(m):
        plaintext += chr(65 + (cipher_lst[i] - key_lst[i])%26)
    for i in range(m,n):
        plaintext += chr(65 + (cipher_lst[i] - (ord(plaintext[i-m])-65))%26)
    print(plaintext)

def main():
    p = None
    q = None
    n = 437
    for i in range(3, int(sqrt(n)),2):
        if n % i == 0:
            p = i
            q = n//i
            break
    print("p=")
    print(p)
    print("q=")
    print(q)
    print("phi=")
    phi_n=(p-1)*(q-1)
    print(phi_n)
    print("d=")
    e=317
    d=pow(e,-1,phi_n)
    print(d)
    print("proba=")
    print(pow(2,-1,26))

if __name__ == "__main__":
    main()