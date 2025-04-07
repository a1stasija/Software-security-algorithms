# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def vigenere_encrypt(plaintext,key):
    ciphertext = ""
    key_lst = [int(c,16) for c in key]
    plaintext_lst = [c%16 for c in plaintext]
    n = len(plaintext)
    m = len(key)
    for i in range(n):
        ciphertext += str(hex((plaintext_lst[i] + key_lst[i%m])%16)).replace('0x','')
    return ciphertext
def main():
    plaintext = "0123456789"
    key = "05A"
    iv = "ABCDE"
    ciphertext = ""
    while len(plaintext)%5 != 0 :
        plaintext += "0"
    block_size = 5
    block_count = len(plaintext)//block_size
    plain_blocks = [plaintext[block_size*i:block_size*(i+1)] for i in range(block_count)]
    cipher_blocks = [["" for _ in range(block_size)] for _ in range(block_count)]
    for i in range(block_count):
        plain_digits = [int(plain_blocks[i][j],16) for j in range(block_size)]
        if(i == 0):
            iv_digits = [int(iv[j],16) for j in range(block_size)]
        else:
            iv_digits = [int(cipher_blocks[i-1][j],16) for j in range(block_size)]
        xor_out = [plain_digits[i]^iv_digits[i] for i in range(block_size)]
        cipher_blocks[i] = vigenere_encrypt(xor_out,key)
    for i in range(block_count):
        ciphertext+=cipher_blocks[i]
    print(ciphertext)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
