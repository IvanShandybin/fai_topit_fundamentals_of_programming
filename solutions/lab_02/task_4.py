import gc

"""print("Сборщик мусора включен:", gc.isenabled())
print("Пороги поколений:", gc.get_threshold())
print("Статистика поколений (counts):", gc.get_count())
first = []
second = []

first.append(second)
second.append(first)

id_first = id(first)
id_second = id(second)
print(f"ID первого списка: {id_first}")
print(f"ID второго списка: {id_second}")

print("first ссылается на second:", first[0] is second)
print("second ссылается на first:", second[0] is first)

del first
del second

collected_count = gc.collect()
print(f"Количество собранных цикклических объектов: {collected_count}")"""

"""print("Автоматический сборщик включен до отключения:", gc.isenabled())
gc.disable()
print("Автоматический сборщик включен после отключения:", gc.isenabled())

def create_isolated_cycles():
    loop_a = []
    loop_b = [loop_a]
    loop_a.append(loop_b)

    loop_dict1 = {}
    loop_dict2 = {"ref": loop_dict1}
    loop_dict1["ref"] = loop_dict2

create_isolated_cycles()
collected_objects = gc.collect()
print(f"Количество объектов, собранных вручную при отключенном автосборщике: {collected_objects}")

gc.enable()
print("Автоматический сборщик успешно восстановлен:", gc.isenabled())"""

gc.collect()

node_a = {"id": "A", "next": None}
node_b = {"id": "B", "next": None}
node_c = {"id": "C", "next": None}

node_a["next"] = node_b
node_b["next"] = node_c
node_c["next"] = node_a  

independent_node = {"id": "Independent", "next": None}

print(f"{node_a['id']} -> {node_a['next']['id']} -> {node_a['next']['next']['id']} -> цикл замкнут")
print(f"Независимый узел: {independent_node['id']}")

del node_a
del node_b
del node_c

collected_count = gc.collect()
print(f"Удалено объектов циклического графа: {collected_count}")

print("Независимый узел по-прежнему доступен:", independent_node["id"])