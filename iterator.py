class FlatIterator:

    def __init__(self, nested_list):
        self.list = sum(nested_list, [])
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.list):
            raise StopIteration
        items = self.list[self.index]
        self.index += 1
        return items

def test():
    nested_list = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f', 'h', False],
            [1, 2, None],
            ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(nested_list),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(nested_list)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    print(list(FlatIterator(nested_list)))

if __name__ == '__main__':
    test()