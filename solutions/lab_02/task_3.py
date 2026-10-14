"""import sys

data = [1, 2, 3]
print("После создания:", sys.getrefcount(data))

alias = data
print("После создания alias:", sys.getrefcount(data))

container = [data]
print("После помещения в контейнер:", sys.getrefcount(data))

del alias
print("После del alias:", sys.getrefcount(data))

container.clear()
print("После очистки контейнера:", sys.getrefcount(data))"""


"""import weakref


class Record:
    pass


record = Record()
weak_record = weakref.ref(record)

print(weak_record())
del record
print(weak_record())"""

import weakref

class Record:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Record({self.name})"

registry = weakref.WeakValueDictionary()

rec1 = Record("Alpha")
rec2 = Record("Beta")
rec3 = Record("Gamma")

registry["a"] = rec1
registry["b"] = rec2
registry["c"] = rec3

print("1. Исходное состояние реестра (все 3 объекта имеют сильные ссылки):")
print(list(registry.items()))

del rec3

print("\n2. После удаления сильной ссылки на 'Gamma' (rec3):")
print(list(registry.items()))

del rec2

print("\n3. После удаления сильной ссылки на 'Beta' (rec2):")
print(list(registry.items()))

print("\nСодержимое реестра на данный момент:")
for key, value in registry.items():
    print(key, ":", value)