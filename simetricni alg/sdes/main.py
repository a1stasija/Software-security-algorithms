# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
pc1 = [3,5,2,7,4,10,1,9,8,6]
rotations = [1,2]
pc2 = [6,3,7,4,8,5,10,9]
ip = [2,6,3,1,4,8,5,7]
ip_inv = [4,1,3,5,7,2,8,6]
e = [4,1,2,3,2,3,4,1]
s1 = [[1,0,3,2],
      [3,2,1,0],
      [0,2,1,3],
      [3,1,0,2]]
s2 = [[0,1,2,3],
      [2,0,1,3],
      [3,0,1,2],
      [2,1,0,3]]
p = [2,4,3,1]

def find_i(arr,i):
    for k in arr:
        if k == i:
            return k
def permute(key,p):
    key_p = [0b0 for _ in range(10)]
    for i in key:
        key_p[i]=key[find_i(key,i-1)]
def generate_keys(key):
    key_p = permute(key,pc1)
    l = key_p[len(key)//2:]
    right = key_p[:len(key)//2]
    left_shift(l,rotations[0])
    left_shift(r,rotations[0])
def sdes_e(plaintext,key):
    k1,k2 = generate_keys(key)
def main():
    plaintext = "10111101"
    k= "1010000010"
    key = [bin(int(c,2)) for c in k]
    sdes_e(plaintext,key)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
