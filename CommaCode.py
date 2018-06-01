
def CommaCode(lst):
    res = ''
    for i in lst[:-1]:
        res = res + i + ', '
    res = res + 'and ' + lst[-1]
    return res

spam = ['apples', 'bananas', 'tofu', 'cats']
print(CommaCode(spam))