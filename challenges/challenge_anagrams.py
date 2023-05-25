def merge_sort(string: str):
    if len(string) <= 1:
        return string

    middle = len(string) // 2
    left = string[:middle]
    right = string[middle:]

    left_orders = merge_sort(left)
    right_orders = merge_sort(right)

    return "".join(merge(left_orders, right_orders))


def merge(left: list[str], right: list[str]):
    result = []
    esq = 0
    dir = 0

    while esq < len(left) and dir < len(right):
        if left[esq] < right[dir]:
            result.append(left[esq])
            esq += 1
        else:
            result.append(right[dir])
            dir += 1

    result += left[esq:]
    result += right[dir:]

    return result


def is_anagram(first_string: str, second_string: str):
    first_lower = first_string.lower() if first_string else ""
    second_lower = second_string.lower() if second_string else ""

    first_orders = merge_sort(first_lower)
    second_orders = merge_sort(second_lower)

    if not first_string or not second_string:
        return (first_orders, second_orders, False)

    result_anagrams = first_orders == second_orders

    return (first_orders, second_orders, result_anagrams)
