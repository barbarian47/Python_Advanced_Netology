class FlatIterator:
    def __init__(self, input_list):
        self.counter = 0
        self.input_list = input_list
        self.unpacked_list = list()
        self.unpack()


    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter - 1 >= len(self.unpacked_list):
            raise StopIteration
        return self.unpacked_list[self.counter - 1]

    def unpack(self):
        def merge(current_list):
            for element in current_list:
                if isinstance(element, list):
                    merge(element)
                else:
                    self.unpacked_list.append(element)

        merge(self.input_list)


if __name__ == "__main__":
    nested_list = [
        ['a', 'b', 'c', [9, 10, [True, 11]]],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]

    print(flat_list)