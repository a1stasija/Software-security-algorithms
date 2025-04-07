# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def railfence_e(plaintext,key):
    ciphertext = ""
    rails = ['' for _ in range(key)]
    rail = 0
    direction = -1
    for c in plaintext:
        rails[rail] += c
        if rail == 0 or rail == key - 1:
            direction *= -1
        rail += direction
    for r in rails:
        ciphertext += r
    print(ciphertext)

def railfence_d(ciphertext,key):
    plaintext = ""
def main():
    plaintext = "NAPADAMOUPODNEAKONEBUDEVETRA"
    key = 3
    railfence_e(plaintext,key)
    ciphertext = ""
    railfence_d(ciphertext,key)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
