def merge_sort(string: str):
    if len(string) <= 1:
        return string

    middle = len(string)
    left = string[:middle]
    right = string[middle:]

    left_orders = merge_sort(left)
    right_orders = merge_sort(right)

    return "".join(merge(left_orders, right_orders))


def merge(first_part, second_part):

    if not first_part:
        return second_part

    if not second_part:
        return first_part

    if first_part[0] > second_part[0]:
        return [second_part[0]] + merge(first_part, second_part[1:])
    else:
        return [first_part[0]] + merge(first_part[1:], second_part)


def is_anagram(first_string, second_string):

    first_lower = first_string.lower() if first_string else ""
    second_lower = second_string.lower() if second_string else ""

    first_orders = merge_sort(first_lower)
    second_orders = merge_sort(second_lower)

    if not first_string or not second_string:
        return (first_orders, second_orders, False)

    anagram = first_orders == second_orders

    return (first_orders, second_orders, anagram)
