import re


def multiply_numbers(*inputs):
    digit_list = re.findall(r"\d", str(inputs))
    if digit_list:
        result = 1
        for x in digit_list:
            result = result * int(x)
        return result


print(multiply_numbers())
print(multiply_numbers('ss'))
print(multiply_numbers('1234'))
print(multiply_numbers('sssdd34'))
print(multiply_numbers(2.3))
print(multiply_numbers([5, 6, 4]))