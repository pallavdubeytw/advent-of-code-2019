def has_two_adj_numbers(number):
    string = str(number)

    i = 0
    while i < len(string) - 1:
        if string[i] == string[i + 1]:
            return True
        i += 1

    return False
