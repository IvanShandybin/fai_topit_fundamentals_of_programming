import sys
import tracemalloc

report_data = []
tracemalloc.start()
numbers_list=list(range(100000))
obj_size_list=sys.getsizeof(numbers_list)
curr_list, peak_list=tracemalloc.get_traced_memory()
tracemalloc.stop()
report_data.append(
    {
        "scenario": "Материализованный список (list)",
        "elements": 100000,
        "obj_size_bytes": obj_size_list,
        "current_kb": curr_list/1024,
        "peak_kb": peak_list/1024,
    }
)
tracemalloc.start()
numbers_range=range(100000)
obj_size_range=sys.getsizeof(numbers_range)
curr_range, peak_range=tracemalloc.get_traced_memory()
tracemalloc.stop()
report_data.append(
    {
        "scenario": "Объект-интервал (range)",
        "elements": 100000,
        "obj_size_bytes": obj_size_range,
        "current_kb": curr_range/1024,
        "peak_kb": peak_range/1024,
    }
)

ratio = (
    report_data[0]["peak_kb"]/report_data[1]["peak_kb"]
    if report_data[1]["peak_kb"] > 0
    else 0
)

for i in report_data:
    print(f"Сценарий:              {i['scenario']}")
    print(f"Количество элементов:  {i['elements']:,}")
    print(f"Размер внешнего объекта: {i['obj_size_bytes']} байт")
    print(f"Текущая память кучи:   {i['current_kb']:.2f} КБ")
    print(f"Пиковая память кучи:   {i['peak_kb']:.2f} КБ")
    print("-" * 80)

print(f"Отношение пикового объема памяти (List / Range): {ratio:.2f} раз(а)")
print("=" * 80)

