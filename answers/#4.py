def four(string1, string2):
    str = "".join(''.join(i) for i in zip(string1, string2))
    return str