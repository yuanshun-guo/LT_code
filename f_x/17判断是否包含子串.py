def to_judge1(a, b):
    if b.find(a) != -1:
        return True
    else:
        return False


a = 'big'
b = 'bigbang'
print(to_judge1(a, b))


def to_judge2(a, b):
    try:
        b.index(a)
        return True
    except ValueError:
        return False


a = 'big'
b = 'bigbang'
print(to_judge2(a, b))
