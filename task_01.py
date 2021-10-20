import re

def is_palindrome(string):
    string = str(string)
    cleanString = re.findall(r'\w', string.lower())
    if cleanString == cleanString[::-1]:
        return True
    else:
        return False


print(is_palindrome("A man, a plan, a canal -- Panama"))
print(is_palindrome("Madam, I'm Adam!"))
print(is_palindrome(333))
print(is_palindrome(None))
print(is_palindrome("Abracadabra"))


