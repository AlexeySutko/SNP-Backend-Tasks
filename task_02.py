
def coincidence(arr:list=[], rng:range=[]):
    if arr == [] or rng == []:
        return []
    else:
        def inRange(val, rng:range):
            min,max = rng[0],rng[-1]
            if type(val) is int or type(val) is float:
                return True if val >= min and val <= max else False
            else:
                return False
        result = []
        for x in arr:
            if inRange(x, rng):
                result.append(x)
        return result


print(coincidence([1, 2, 3, 4, 5], range(3, 6)))
print(coincidence())
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))
