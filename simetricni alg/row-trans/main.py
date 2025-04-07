# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def rowtrans_encrypt(plaintext,key):
    cols = len(key)
    res = ["" for _ in range(len(plaintext))]
    rows = len(plaintext) // cols

    for i in range(len(plaintext)):
        j = (key[i%cols]-1)*rows + i//cols
        res[j]=plaintext[i]

    print(res)

def rowtrans_decrypt(ciphertext,key):
    cols = len(key)
    res = ""
    rows = len(ciphertext)//cols
    for i in range(len(ciphertext)):
        j = (key[i%cols]-1)*rows + i//cols
        res+=ciphertext[j]
    print(res)
def main():
    plaintext = ""
    key = [4,3,1,2]
    plaintext = plaintext.upper()
    while len(plaintext)%len(key) != 0:
        plaintext += "X"
    rowtrans_encrypt(plaintext,key)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
