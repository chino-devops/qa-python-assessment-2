def one(n,string):
    word = ''
    for char in string:
        word += char * n 
    return word
one(3, 'ape')