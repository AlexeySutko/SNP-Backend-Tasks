import re

def count_words(string):
    word_list = re.findall(r'\w+', string.lower())
    wordcount = {}
    for word in word_list:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1

    return wordcount


print(count_words("A man, a plan, a canal -- Panama"))
print(count_words("Doo bee doo bee doo"))