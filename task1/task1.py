import sys


def itoBase(nb, baseSrc: int, baseDist: int=10):
    """Конвертация числа nb из baseDist в baseSrc систему исчисления"""
    # Конвертируем полученное число в 10-чную систему
    if isinstance(nb, str):
        n = int(nb, baseDist)
    else:
        n = int(nb)
    # Конвертируем из полученного 10-чного числа в baseSrc систему
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < baseSrc:
        return alphabet[n]
    else:
        return itoBase(n // baseSrc, baseSrc) + alphabet[n % baseSrc]


def main():
    if len(sys.argv) > 2:
        a = sys.argv
        num = a[1]
        newBase = int(a[2])
        if len(a) > 3:
            oldBase = int(a[3])
        else:
            oldBase = 10
        print(itoBase(num, newBase, oldBase))
    else:
        print("Not enough arguments.")

main()
