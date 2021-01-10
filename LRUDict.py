from collections import OrderedDict


class LRUDict(OrderedDict):
    def __init__(self, capacity):
        super().__init__()
        self.capacity = capacity
        self.items = OrderedDict()

    def __setitem__(self, key, value):
        old = self.items.get(key)
        if old is not None:
            self.items.pop(key)
            self.items[key] = value
        elif len(self.items) < self.capacity:
            self.items[key] = value
        else:
            self.items.popitem(last=False)
            self.items[key] = value

    def __getitem__(self, item):
        value = self.items.get(item)
        if value is not None:
            self.items.pop(item)
            self.items[item] = value
        return value

    def __repr__(self):
        return repr(self.items)


d = LRUDict(20)

for i in range(40):
    d[i] = i

print(d)
