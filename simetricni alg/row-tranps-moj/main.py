# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def find_i(key,k):
    for i in range(len(key)):
        if key[i] == k:
            return i
def rowtrans_e(plaintext,key):
    ciphertext = ""
    cols = len(key)
    while len(plaintext)%cols != 0:
        plaintext += "X"
    rows = len(plaintext)//cols
    key_dict = {}
    for i in range(cols):
        key[i] -= 1
    for i in range(cols):
        key_dict[i] = find_i(key,i)
    cipher_matrix = [["" for _ in range(rows)] for _ in range(cols)]
    for i in range(len(plaintext)):
        cipher_matrix[i%cols][i//cols] = plaintext[i]
    for i in range(cols):
        for j in range(rows):
            ciphertext += cipher_matrix[key_dict[i]][j]
    print(ciphertext)

def rowtrans_d(ciphertext,key):
    plaintext = ""
    cols = len(key)
    rows = len(ciphertext)//len(key)
    key_dict = {}
    for i in range(cols):
        key_dict[i] = find_i(key,i)
    plain_arr = [["" for _ in range(rows)] for _ in range(cols)]
    cnt = 0
    for i in range(cols):
        for j in range(rows):
            plain_arr[key_dict[i]][j] = ciphertext[cnt]
            cnt += 1
    for i in range(len(ciphertext)):
        plaintext += plain_arr[i%cols][i//cols]
    print(plaintext)
def main():
    plaintext = "NAPADAMOUPODNEAKONEBUDEVETRA"
    key = [4,3,1,2,5,6,7]
    rowtrans_e(plaintext,key)
    ciphertext = "PPOVAONEAUKENOADDDETANBRMEUA"
    rowtrans_d(ciphertext,key)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
