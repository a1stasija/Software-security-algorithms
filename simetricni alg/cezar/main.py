# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def de_cezar(a,k):
   for c in a:
       if c.isalpha():
           p = chr(65 + (ord(c) - 65 - k)%26)

       else:
           p = c
       print(p, end='')
   print('\n')



def sif_cezar(a,k):
    for p in a:
        if p.isalpha():
            c = chr(65+(ord(p) - 65 + k)%26)
        else:
            c = p
        print(c, end='')

    print('\n')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #b = "NAPADAMO U PODNE AKO NE BUDE VETRA" #radi samo za all caps jer ascii mala pocinju negde drugde
    #sif_cezar(b,3)
    a = "IXFN QLJJHUV"
    de_cezar(a,3)

    #65 je za velika slova
    #97 je za mala slova

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
