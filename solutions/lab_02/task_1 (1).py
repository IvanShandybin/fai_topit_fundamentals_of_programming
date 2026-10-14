"""a = 10
b = a

print(a, b)
print(id(a), id(b))

a += 1

print(a, b)
print(id(a), id(b))"""

"""first = [10, 20]
second = first

print(first, second)
print(id(first), id(second))

second.append(30)

print(first, second)
print(id(first), id(second))

second = [10,20,30]
print(first==second, first is second)

second.append(40)
print(first,second)"""

import copy

config_1 = {
    "name": "Project Alpha",
    "participants": ["Иван", "Пётр"],
    "parameters": ["--debug", "--port=8080"]
}
config_2=config_1
config_2["participants"].append("Анна")
print("config_1:",config_1)
print("config_2:",config_2)
print(config_1["participants"] is config_2["participants"])
print()

config_3 = {
    "name": "Project Beta",
    "participants": ["Иван", "Пётр"],
    "parameters": ["--release", "--port=9000"]
}
config_4 = copy.deepcopy(config_3)
config_4["participants"].append("Мария")
config_4["parameters"].append("--verbose")
print("config_3:", config_3)
print("config_4:", config_4)
assert config_3 is not config_4
assert config_3["participants"] is not config_4["participants"]
assert config_3["parameters"] is not config_4["parameters"]
print("норм")