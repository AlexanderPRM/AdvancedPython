from config import FlatIterator, flat_generator, advanced_flat_generator

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

# for item in FlatIterator(nested_list):
#     print(item)


# for item in flat_generator(nested_list):
#     print(item)

# nested_list = [
#     ['a', 'b', 'c'],
#     ['d', 'e', [1111, '2131', True], 'f', 'h', False],
#     [1, 2, None, [14, False, 124.2]],
# ]
# for item in advanced_flat_generator(nested_list):
#     print(item)

