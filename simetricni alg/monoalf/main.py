# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def sif_monoalpha_moja(plaintext, key):
   ciphertext = ''
   for i in range(len(plaintext)):
       if plaintext[i].isalpha():
           ciphertext += key[ord(plaintext[i])-97]
       else:
           ciphertext += plaintext[i]
   print(ciphertext)

def sif_monoalpha(plaintext, key):
    key_dict = {}
    for i in range(26):
        key_dict[chr(97 + i)] = key[i]
    # encrypt
    plaintext = plaintext.replace(' ', 'x') #mora kod vukovog da bi radilo
    ciphertext = ''
    for char in plaintext:
        ciphertext += key_dict[char]

    print(ciphertext)

#def de_monoalpha_moja(ciphertext, key):
# prekomplikovano, zahteva da nadjemo redni broj u key-u za svako slovo

def de_monoalpha(ciphertext,key):
    inv_dict={}
    for i in range(26):
        inv_dict[key[i]] = chr(97 + i)

    plaintext = ''
    for char in ciphertext:
        plaintext += inv_dict[char]

    plaintext = plaintext.replace('x', ' ')
    print(plaintext)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = "tekst"
    k = "qwertzuiopasdfghjklyxcvbnm"
    sif_monoalpha_moja(a,k)
    b="ytaly"
    de_monoalpha(b,k)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
