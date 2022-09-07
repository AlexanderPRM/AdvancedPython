# Задание 1. Работает только с первым уровнем вложенности.
class FlatIterator:
    def __init__(self, data_list):
        self.data_list = data_list

    def __iter__(self):
        self.counter = 0
        self.nested_counter = 0
        return self

    def __next__(self):
        if self.counter == len(self.data_list):
            raise StopIteration
        else:
            self.results = self.data_list[self.counter][self.nested_counter]
            self.nested_counter += 1
            if self.nested_counter == len(self.data_list[self.counter]):
                self.counter += 1
                self.nested_counter = 0
        return self.results


# Задание 2. Генератор, который также обрабатывает только один уровень вложенности

def flat_generator(data_list):
    counter = 0
    nested_counter = 0
    while counter < len(data_list):
        yield data_list[counter][nested_counter]
        nested_counter += 1
        if nested_counter == len(data_list[counter]):
            nested_counter = 0
            counter += 1

# Задание 3.

# class AdvancedFlatIterator:
#     def __init__(self, data_list):
#         self.data_list = data_list
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while True:
#             current_el = next()


# Задание 4. Генератор, который обрабатывает любые уровни вложенности.
def advanced_flat_generator(data_list):
    for el in data_list:
        if isinstance(el, list):
            for element in advanced_flat_generator(el):
                yield element
        else:
            yield el
