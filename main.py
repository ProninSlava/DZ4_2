nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

#1_______________________________
def FlatIterator(nested_list):
    nested_list_new = []
    for item in nested_list:
        nested_list_new += item
    return nested_list_new

for item in FlatIterator(nested_list):
    print(item)

#2_______________________________
print([item for item in FlatIterator(nested_list)])

#3_______________________________
print(sum(nested_list,[]))

#4_______________________________
def FlatIterator_(nested_list):
    for list_g in nested_list:
        for list_vl in list_g:
            yield list_vl

for item in FlatIterator_(nested_list):
    print(item)

print('__________________________')
#5_______________________________
class NestedIterator:
    def __init__(self, list_):
        self._stopped = False
        self._list = list_
        self._i = 0
        self._j = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self._stopped:
            while self._i < len(self._list):
                if self._j < len(self._list[self._i]):
                    v = self._list[self._i][self._j]
                    self._j += 1
                    return v

                self._i += 1
                self._j = 0
            self._stopped = True
        raise StopIteration


def main(nested_list):
    flat_list = list(NestedIterator(nested_list))
    print(flat_list)

main(nested_list)