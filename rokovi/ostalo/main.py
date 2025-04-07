# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def main2():
    q = 100003
    alpha = 99989
    xa = 10002
    xb = 9999
    ya = pow(alpha,xa,q)
    yb = pow(alpha,xb,q)
    k= pow(ya,xb,q)
    print(k)
    print(pow(35,-1,37))

def main1():
    n = 11 * 23
    M = "A9333A105A"
    plaintext = ""
    block_size = 2
    block_count = len(M)//block_size
    cipher_blocks = [int(M[block_size*i:block_size*i+2],base=16) for i in range(0,block_count)]
    plain_blocks = [pow(c,113,n) for c in cipher_blocks]
    for i in range(0,block_count):
        c = plain_blocks[i]
        plaintext += chr(c)
    print(plaintext)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #main1()
    main2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
