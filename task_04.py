
def sort_list(list):
    if list:
        xMin = list[0]
        xMax = list[0]
        for x in list:
            if xMax < x:
                xMax = x
            elif xMin > x:
                xMin = x

        for x in range(len(list)):
            if list[x] == xMax:
                list[x] = xMin
            elif list[x] == xMin:
                list[x] = xMax

        list.append(xMin)
    return list


print(sort_list([]))
print(sort_list([2, 4, 6, 8]))
print(sort_list([1]))
print(sort_list([1, 2, 1, 3]))
