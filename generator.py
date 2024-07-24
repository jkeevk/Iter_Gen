def flat_generator(nested_list):
    for some_list in nested_list:
        for item in some_list:
            yield item

def test():
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(nested_list),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(nested_list)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    print(list(flat_generator(nested_list)))

if __name__ == '__main__':
    test()

