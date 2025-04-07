# This is a sample Python script.
from math import sqrt


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def vigenere_auto_decrypt(ciphertext, key):
    plaintext = ""
    cipher_lst = [ord(c) - 65 for c in ciphertext]
    n = len(ciphertext)
    m = len(key)
    for i in range(m):
        plaintext += chr(65 + (cipher_lst[i] - key[i])%26)
    for i in range(m,n):
        plaintext += chr(65 + (cipher_lst[i] - (ord(plaintext[i-m]) - 65))%26)
    print(plaintext)
def rsa_decrypt(ciphertext,x,n):
    plaintext = pow(ciphertext,x,n)
    return plaintext


def find_inverse(x,n):
    p = None
    q = None
    for i in range(3,int(sqrt(n)+1),2):
        if n%i==0:
            p = i
            q = n//i
            break
    phi_n = (p-1)*(q-1)
    y = pow(x,-1,phi_n)
    return y

def main():
    n = 868165516507
    e = 52127
    d = find_inverse(e,n)
    key_encrypted = 453706198292
    key_decrypted = rsa_decrypt(key_encrypted,d,n)
    key_decrypted_str = str(key_decrypted)
    key_digits = [int(c) for c in key_decrypted_str]
    key_numbers = [
        key_digits[0]*10+key_digits[1],
        key_digits[2],
        key_digits[3]*10+key_digits[4],
        key_digits[5]*10+key_digits[6],
        key_digits[7],
        key_digits[8]*10+key_digits[9],
        key_digits[10]
    ]
    ciphertext = "SOYXBAEKOTVLHTLBYZUKTSBYLCXVQACUIIRLEZVGAOKQKRPXOBQYCRAR"
    vigenere_auto_decrypt(ciphertext,key_numbers)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
