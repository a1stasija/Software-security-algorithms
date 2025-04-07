# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def encrypt_vigenere(plaintext,key):
    ciphertext=''
    plaintext_lst = [ord(c) - 97 for c in plaintext]
    key_lst = [ord(c) - 97 for c in key]
    n = len(key)
    for i in range(len(plaintext)):
        ciphertext += chr(97 + (plaintext_lst[i] + key_lst[i % n]) % 26)
    print(ciphertext)

def decrypt_vigenere(ciphertext, key):
    plaintext = ''
    ciphertext_lst = [ord(c) - 97 for c in ciphertext]
    key_lst = [ord(c) - 97 for c in key]
    n = len(key)
    for i in range(len(ciphertext)):
        plaintext += chr(97 + (ciphertext_lst[i] - key_lst[i % n])%26)
    print(plaintext)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a="wearediscoveredsaveyourself"
    k="deceptive"
    a.lower()
    k.lower()
    encrypt_vigenere(a,k)

    b = "zicvtwqngrzgvtwavzhcqyglmgj"
    b.lower()
    decrypt_vigenere(b,k)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
