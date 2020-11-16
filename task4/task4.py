import sys


def compare(first_string, second_string):
    """
    Функция, проверяющая на идентичность две строки с учётом
    символа '*', который может заменять собой любое колчиство символов.
    """
    second_string_list = second_string.split("*")
    if second_string_list[0] != "":
        if not (first_string.startswith(second_string_list[0])):
            return False

    start = 0
    end = len(second_string_list) - 1
    for i in second_string_list:
        if i != '':
            start = first_string.find(i, start)
            if start == -1:
                return False
            else:
                start += len(i)

    if second_string_list[end] != "":
        if not (first_string.startswith(second_string_list[end])):
            return False

    if '*' not in second_string:
        if len(second_string) != len(first_string):
            return False

    return True

def main():
    if len(sys.argv[1:]) < 2:
        print("Not enough arguments, expected at least 2")
        return

    list_data = sys.argv[1:]
    first_string = list_data[0]
    second_string = list_data[1]


    is_the_same = compare(first_string, second_string)
    if is_the_same:
        print("OK")
    else:
        print("KO")

main()

