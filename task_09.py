

def connect_dicts(dict1: dict, dict2: dict):
    sum_dict1 = 0
    sum_dict2 = 0
    sorted_dict = {}

    def clean_dicts(d1: dict, d2: dict):
        for i in d1.keys():
            val1 = d1.get(i)
            if val1 < 10:
                del d1[i]
                return clean_dicts(d1, d2)
        for i in d2.keys():
            val1 = d2.get(i)
            if val1 < 10:
                del d2[i]
                return clean_dicts(d1, d2)

    for x in dict1.values():
        sum_dict1 += x
    for x in dict2.values():
        sum_dict2 += x

    if sum_dict1 > sum_dict2:
        clean_dicts(dict1, dict2)
        for x in dict2.keys():
            if x not in dict1.keys():
                dict1[x] = dict2.get(x)

        sorted_values = sorted(dict1.values())
        for x in sorted_values:
            for j in dict1.keys():
                if dict1[j] == x:
                    sorted_dict[j] = dict1[j]
        return sorted_dict

    else:
        clean_dicts(dict1, dict2)
        for x in dict1.keys():
            if x not in dict2.keys():
                dict2[x] = dict1.get(x)

        sorted_values = sorted(dict2.values())
        for x in sorted_values:
            for j in dict2.keys():
                if dict2[j] == x:
                    sorted_dict[j] = dict2[j]
        return sorted_dict



print(connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5}))
print(connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15}))
print(connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15}))