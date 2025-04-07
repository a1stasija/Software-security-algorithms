# This is a sample Python script.
from math import sqrt


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def rsa_encrypt(plaintext,x,n):
    block_size = 2
    block_count = len(plaintext)//block_size
    plain_blocks = [ord(plaintext[block_size*i])*256 + ord(plaintext[block_size*i+1]) for i in range(0,block_count)]
    cipher_blocks = [pow(m,x,n) for m in plain_blocks]
    cipher_blocks= [hex(c) for c in cipher_blocks]
    ciphertext = ""
    for i in range(0,block_count):
        ciphertext += str(cipher_blocks[i]).replace('0x','')
    print(ciphertext)
def rsa_decrypt(ciphertext,x,n):
    block_size = 4
    block_count = len(ciphertext) // block_size
    cipher_blocks = [int(ciphertext[block_size*i:block_size*(i+1)], base = 16) for i in range(0,block_count)]
    plaintext = ""
    plain_blocks = [pow(c,x,n) for c in cipher_blocks]
    for i in range(0,block_count):
        plaintext += chr(plain_blocks[i]//256)
        plaintext += chr(plain_blocks[i]%256)
    print(plaintext)
def find_inverse(x,n):
    p = None
    q = None
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            p = i
            q = n//i
            break
    phi_n = (p-1)*(q-1)
    y = pow(x,-1,phi_n)
    return y

def main():
    ciphertext = "4209c15b6135828160d357324302b4b8b8b7563aa801d2b2c15b0cc1c15b082df1f2063eecbe618f0a72da373abae48460d30a724e4ae484266b68cdf27fa339545434d127a89094e061035668cd266b5e5e61446562ccb060d31d0ae4e57df1618f384b6865266b68cd430255eef1f2063ee6f75656739057321ce90898266bd7ea002073909a29604f2d403833790ce4846c1560f060d394145e5ef06f1d4161448f1b0cc161cb6144ee55f0f13833495cf1f2063ed9840f10f9d41ce9b4b81ce19aefdf03503c9d30e1a8f6063fc9f606ee5590946b055f5fc190c15bc0612916c15b0cc1c15b8b6ba212de92c2c1c15b4c1034d10cc1c15b1e1b6969bf37e91f29161ce9ba18618f4e4a80c4ab121d4161442d4000acf33e5f62e48460d3d937caaaaf00a9e57b1da0d461351ce160d35732389e1ce19093f1f6f6bdee556144a2126969bf37ecbe383324284ced38c8a80174942773ee5560d3f72a08981ce90898d5a7caaa1b02637f2d40a2126144b9bcf958277360d3e746a2120ba438c8f27f2e21b975389ea929a21269690d0cde381c8819f5a212de92b9bc1c88f0f1bffb61442d40ab12f6062e215e5e573275602b2fcaaa75225f5fa1a8604fc2c1614465627390f9d456563801266b68cd7df1c8e238330cc161cb43021a2d0b410d0cb7abf27f48e10f43f27f8f1b1e3e7b7cde924dba73905f6231117b6bc320bf37bd50c15b0fb26350e4846144656273902b8bcb0b61442d40614457323635614465627390b28df06fbf37d700b8b761445f6211b848e1f6063fc960d35732503c7e7e6c07e48460d3d7eaee550f430356839f5732604f61cb0bbeb4b8e1c11cb1b614a0d4ba1811b81d0acfbc0b410d0ca2a82d40bffb7390db1eaca8c15bcfbc1ce180dc60d357322627e1c1c320"
    n = 64507
    e = 509
    d = find_inverse(e,n)
    plaintext = '''She walks in beauty, like the night
	Of cloudless climes and starry skies;
And all that's best of dark and bright
	Meet in her aspect and her eyes
Thus mellow'd to that tender light
	Which heaven to gaudy day denies.

One shade the more, one ray the less,
	Had half impair'd the nameless grace
Which waves in every raven tress,
	Or softly lightens o'er her face;
Where thoughts serenely sweet express
	How pure, how dear their dwelling-place.

And on that cheek, and o'er that brow,
	So soft, so calm, yet eloquent,
The smiles that win, the tints that glow,
	But tell of days in goodness spent,
A mind at peace with all below,
	A heart whose love is innocent'''
    rsa_encrypt(plaintext,e,n)
    #rsa_decrypt(ciphertext,d,n)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
