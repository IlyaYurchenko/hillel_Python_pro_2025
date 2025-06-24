def string_len(string: str):
    return f'srtring lenght: {len(string)}'

def string_concat(string1: str, string2:str):
    return f'concatenated string: {string1 + string2}'

def square(num: int | float):
    return f'number square = {num ** 2}'

def num_sum(num1: int | float, num2: int | float):
    return f'numbers sum = {num1 + num2}' 

def num_subdiv(num1: int, num2: int):
    whole_part = num1 // num2
    fractional_part = num1 % num2
    return f'whole_part: {whole_part}\n fractional_part: {fractional_part}'

def list_avg(numbers: list[int | float]):
    avg = sum(numbers) / len(numbers)
    return f'avg: {avg}'

def list_common_elements(list1: list[int | float], list2: list[int | float]):
    common = sorted(set(list1) & set(list2))
    return f'common elements: {common}'

def dict_keys_values(d: dict):
    keys = list(d.keys())
    return f'keys: {keys}'

def dicts_merge(dict1: dict, dict2: dict):
    merged_dict = {**dict1, **dict2}
    return f'merged_dict: {merged_dict}'

def union_sets(set1: set, set2: set):
    return f'union: {set1.union(set2)}'

def is_subset(set1: set, set2: set):
    return f'set1 is subset of set2: {set1.issubset(set2)}'

def if_odd(num: int | float):
    if num % 2 == 0:
        return f'{num} is even'
    else:
        return f'{num} is odd'
    
def odd_list(numbers: list[int | float]):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return f'odd numbers: {odd_numbers}'


# 1. string_len
assert string_len("hello") == "srtring lenght: 5"

# 2. string_concat
assert string_concat("hello", "world") == "concatenated string: helloworld"

# 3. square
assert square(3) == "number square = 9"

# 4. num_sum
assert num_sum(3, 5.5) == "numbers sum = 8.5"

# 5. num_subdiv
assert num_subdiv(10, 3) == "whole_part: 3\n fractional_part: 1"

# 6. list_avg
assert list_avg([1, 2, 3, 4]) == "avg: 2.5"

# 7. list_common_elements
assert list_common_elements([1, 2, 3], [2, 3, 4]) == "common elements: [2, 3]"

# 8. dict_keys_values
assert dict_keys_values({'a': 1, 'b': 2}) == "keys: ['a', 'b']"

# 9. dicts_merge
assert dicts_merge({'a': 1}, {'b': 2}) == "merged_dict: {'a': 1, 'b': 2}"

# 10. union_sets
assert union_sets({1, 2}, {2, 3}) == "union: {1, 2, 3}"

# 11. is_subset
assert is_subset({1, 2}, {1, 2, 3}) == "set1 is subset of set2: True"

# 12. if_odd
assert if_odd(3) == "3 is odd"
assert if_odd(4) == "4 is even"

# 13. odd_list
assert odd_list([1, 2, 3, 4, 5]) == "odd numbers: [1, 3, 5]"


print("OKEY")