# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def qr(first,second,third,fourth,key):
    a = key[first//4][first%4]
    b = key[second//4][second%4]
    c = key[third//4][third%4]
    d = key[fourth//4][fourth%4]

    a = a + b
    #d = ((a ^ d) << 4) & 0xff NE MOZE OVAKO JER JE KRUZNO POMERANJE
    d = a ^ d
    d = (d<<4) | ((d & 0xf0)>>4)
    c = c + d
    b = b ^ c
    b = (b<<3) | ((b&0xe0)>>5) #PAZI SA CIME POMERAS, POMERAS UDESNO ZA UKUPNO-ONOLIKO KOLIKO SI ULEVO

    key[first//4][first%4] = a & 0xff
    key[second // 4][second % 4] = b & 0xff
    key[third // 4][third % 4] = c & 0xff
    key[fourth // 4][fourth % 4] = d & 0xff


def neparna_runda(key):
    for i in range(0,4):
        qr(i,i+1*4,i+2*4,i+3*4,key)
        i+=1
def parna_runda(key):
    for i in range(0,4):
        qr(i,(i+1*4+1)%16,(i+2*4+2)%16,(i+3*4+3)%16,key)
        i+=1
def chacha_e(plaintext_matrix,key,rounds):
        ciphertext = ""
        initial = [row[:] for row in key]
        final = [[0x00 for _ in range(4)] for _ in range(4)]
        for j in range(1,rounds+1):
            if j%2 != 0: #neparne runde
                neparna_runda(key)
            else:
                parna_runda(key)
        for i in range(16):
            final[i//4][i%4] = ((initial[i//4][i%4] + key[i//4][i%4])&0xff)
        for i in range(16):
            c = hex(final[i//4][i%4]^plaintext_matrix[i//4][i%4])
            ciphertext += str(c).replace('0x','')
        print(ciphertext)
def main():
    plaintext = "D274EAA0926C5FD31972DD8605CA034C"
    key = [[0xab,0xcd,0xef,0x01],[0x12,0x34,0x56,0x78],[0x76,0x54,0x32,0x10],[0x00,0x00,0xba,0xba]]
    plaintext_matrix = [[0x00 for _ in range(4)] for _ in range(4)]
    for i in range(len(plaintext)//2):
            plaintext_matrix[i//4][i%4] = int(plaintext[2*i:2*i+2],16)
    rounds = 1
    chacha_e(plaintext_matrix,key,rounds)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
