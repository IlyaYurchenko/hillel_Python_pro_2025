set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Додавання та видалення елементів
set_a.add(4)
set_b.remove(5)

# Операції над множинами
union_result = set_a.union(set_b)
intersection_result = set_a.intersection(set_b)

print(f'Об\'єднання множин: {union_result}')
print(f'Перетин множин: {intersection_result}')
