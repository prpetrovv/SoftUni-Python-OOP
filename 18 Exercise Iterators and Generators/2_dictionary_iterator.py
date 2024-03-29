class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary_tuple = tuple(dictionary.items())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.dictionary_tuple):
            index = self.index
            self.index += 1
            return self.dictionary_tuple[index]
        else:
            raise StopIteration()


# Test Code
result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
