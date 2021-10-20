
def max_odd(array):
    x1 = 0

    for x in array:

        if isinstance(x, int) or isinstance(x, float):
            if int(x) > int(x1) and (int(x) % 2) != 0:
                x1 = int(x)
        elif isinstance(x, list):
            for y in x:
                if int(y) > int(x1) and (int(y) % 2) != 0:
                    x1 = int(y)

    if (x1 % 2) != 0:
        return x1
    else:
        return None


print(max_odd([1, 2, 3, 4, 4]))
print(max_odd([21.0, 2, 3, 4, 4]))
print(max_odd(['ololo', 2, 3, 4, [1, 11], None]))
print(max_odd(['ololo', 'fufufu']))
print(max_odd([2, 2, 4]))