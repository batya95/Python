def arithmetic_series(first_item, diff, num_items):
    if diff < 0:
        raise ValueError('diff must be positive number')
    yield (first_item)
    for _ in range(num_items-1):
        first_item += diff
        yield (first_item)


for item in arithmetic_series(3, 5, 4):
    print(item)

series = arithmetic_series(7, 2, 8)
item1 = next(series)
item2 = next(series)

print(item1, item2)

for item in arithmetic_series(10, -2, 5):
    print(item)
