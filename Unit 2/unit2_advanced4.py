# input: string of lower case letters
# output: true/false

# Return true if already balanced or if there is one duplicate letter

# Return false if:
#    a frequency is 2 or more than the minimum frequency
#    there is more than 1 frequency above the minimum frequency


def is_balanced(code):
    my_dict = {}
    above = False

    for char in code:
        if char not in my_dict:
            my_dict[char] = 0
        else:
            my_dict[char] += 1

    max_num = max(my_dict.values())
    min_num = min(my_dict.values())

    if max_num - min_num > 1:
        return False

    for value in my_dict.values():
        if value > min_num and above is False:
            above = True
        elif value > min_num and above is True:
            return False

    if above is True:
        return True
    else:
        return False


code1 = "aarrgghgh"
code2 = "haha"

print(is_balanced(code1))
print(is_balanced(code2))
