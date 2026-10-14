student = "Анна Смирнова"
course = "Основы программирования на Python"
completed = 7
total = 10

print(student[0],student[-1])
print(student[0:4],student[5:13])
print(student.upper(), student.lower())
print(student[0]+'.'+student[5]+'.')
print(course[::-1])
print("%s — %s: %d/%d (%.1f%%)" % (student, course, completed, total, (completed / total) * 100))
print("{} — {}: {}/{} ({}%)".format(student, course, completed, total, (completed / total) * 100))
print(f"{student} — {course}: {completed}/{total} ({(completed / total) * 100}%)")

symbol = "Я"
code_point = ord(symbol)
"""symbol[0]="Э" """

restored_symbol = chr(code_point)
encoded_bytes = symbol.encode("utf-8")
bytes_length = len(encoded_bytes)

print(f"Символ: {symbol}")
print(f"Кодовая позиция (ord): {code_point} (в шестнадцатеричной системе: U+{code_point:04X})")
print(f"Восстановленный символ (chr): {restored_symbol}")
print(f"Результат encode('utf-8'): {encoded_bytes}")
print(f"Длина байтовой строки: {bytes_length} байта(ов)")