def flat_generator(input_list):
    for element in input_list:
        if isinstance(element, list):
            for item in flat_generator(element):
                yield item
        else:
            yield element

if __name__ == "__main__":
    nested_list = [
        ['a', 'b', 'c', [9, 10, [True, 11]]],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]


    for item in flat_generator(nested_list):
        print(item)