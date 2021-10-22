
def combine_anagrams(words_arr: list):
    grouped_arr = {}
    grouped_list = []
    for x in words_arr:
        sorted_word = "".join(sorted(x))
        if sorted_word in grouped_arr:
            grouped_arr[sorted_word].append(x)
        else:
            grouped_arr[sorted_word] = [x]
    for j in grouped_arr.values():
        grouped_list.append(j)
    return grouped_list


print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar",
                        "creams", "scream"]))