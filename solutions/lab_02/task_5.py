import sys

"""print("Пустой список:", sys.getsizeof([]))
print("Список из 10 целых чисел:", sys.getsizeof(list(range(10))))
print("Кортеж с теми же значениями:", sys.getsizeof(tuple(range(10))))
print("Строка из 10 символов:", sys.getsizeof("1234567890"))
print("Целое число:", sys.getsizeof(42))
print("Объект None:", sys.getsizeof(None))"""

"""dynamic_list = []
prev_size = sys.getsizeof(dynamic_list)

print(f"Начальное состояние: длина = {len(dynamic_list)}, размер = {prev_size} байт")

for i in range(100):
    dynamic_list.append(i)
    current_size = sys.getsizeof(dynamic_list)
    if current_size != prev_size:
        print(f"Изменение размера! Длина: {len(dynamic_list)}, Размер в памяти: {current_size} байт")
        prev_size = current_size"""
        
import tracemalloc

tracemalloc.start()
numbers_list = list(range(100_000))
current_list, peak_list = tracemalloc.get_traced_memory()
tracemalloc.stop()

tracemalloc.start()
numbers_range = range(100_000)
current_range, peak_range = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"list(range(100_000)): текущая память = {current_list / 1024:.2f} КБ, пиковая = {peak_list / 1024:.2f} КБ")
print(f"range(100_000): текущая память = {current_range / 1024:.2f} КБ, пиковая = {peak_range / 1024:.2f} КБ" if False else f"range(100_000): текущая память = {current_range / 1024:.2f} КБ, пиковая = {peak_range / 1024:.2f} КБ")