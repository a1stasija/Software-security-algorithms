# This is a sample Python script.

def f(right):
    return pow(7,right,26)
def feistel_round(left,right):
    return right, left ^ f(right)

def feistel(left,right,rounds):
    for i in range(0,rounds):
        left,right=feistel_round(left,right)
    return right,left

def main():
    ciphertext = '10111100000100011010011110001010000011110011011100110110010111011001011000100010110101000001101101011101100101000010001001111000100100000010000111100011000111000111110100001100000000011001011000001111'
    plaintext = ""
    block_size = 10
    block_count = len(ciphertext)//block_size
    for i in range(0,block_count):
        x = int(ciphertext[block_size*i:block_size*i+5],2)
        y = int(ciphertext[block_size*i+5:block_size*i+10],2)
        x,y=feistel(x,y,16)
        plaintext += chr(65+x)
        plaintext += chr(65+y)
    print(plaintext)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
