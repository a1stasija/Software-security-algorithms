# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def vigenere_auto_decrypt(ciphertext,key):
    plaintext = ''
    ciphertext_lst = [ord(c) - 65 for c in ciphertext]
    key_lst = [ord(c) - 65 for c in key]
    n = len(ciphertext)
    m = len(key)
    for i in range(m):
        plaintext += chr(65 + (ciphertext_lst[i]-key_lst[i])%26)
    for i in range(m,n):
        plaintext+= chr(65 +(ciphertext_lst[i] - ord(plaintext[i-m])+65)%26)

    print(plaintext)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = "KNHFMMDVIMMPLZD"
    k = "HFCAEI"
    vigenere_auto_decrypt(a,k)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
