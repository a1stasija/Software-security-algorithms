# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def find_i(key,i):
    for j in range(len(key)):
        if key[j] == i:
            return j
def rowtrans_e(plaintext,key):
    ciphertext = [0x0 for _ in range(len(plaintext))]
    #ciphertext = ""
    rows = len(plaintext)//len(key)
    cols = len(key)
    matrix = [[0x0 for _ in range(rows)] for _ in range(cols)]
    for i in range(cols):
        key[i] -= 1
    key_dict = {}
    for i in range(cols):
        key_dict[i] = find_i(key,i)
    for i in range(len(plaintext)):
        matrix[i%4][i//4] = plaintext[i]
    cnt = 0
    for i in range(cols):
        for j in range(rows):
            ciphertext[cnt] = matrix[key_dict[i]][j]
            cnt += 1
    return ciphertext

def main():
    plaintext = "1234ABCD"
    ciphertext = ""
    block_size = 4
    iv = "0123456789"
    key = [3,1,4,2]
    while len(plaintext)%block_size!=0:
        plaintext += "0"
    while len(iv)!=12:
        iv+="0"
    block_count = len(plaintext)//block_size
    plain_blocks =[[0x0 for _ in range(block_size)] for _ in range(block_count)]
    output_blocks = [[0x0 for _ in range(12)] for _ in range(block_count)]
    cipher_blocks = [[0x0 for _ in range(block_size)] for _ in range(block_count)]
    for i in range(len(plaintext)):
        plain_blocks[i//4][i%4]=int(plaintext[i],16)
    input = [0x0 for _ in range(12)]
    for i in range(block_count):
        if i == 0:
            input = [int(c,16) for c in iv]
        else:
            for j in range(4,12):
                input[j] = input[j-4]
            for j in range(0,4):
                input[j] = cipher_blocks[i][j]
        output_blocks[i]=rowtrans_e(input,key)
        for j in range(block_size):
            cipher_blocks[i][j] = plain_blocks[i][j]^output_blocks[i][j]
    for j in range(block_count):
        ciphertext+=str(hex(cipher_blocks[j])).replace('0x','')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
