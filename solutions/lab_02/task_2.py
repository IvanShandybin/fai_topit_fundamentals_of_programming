"""import copy

original = [
    ["Python", 5],
    ["Algorithms", 4],
]

alias = original
shallow = original.copy()
deep = copy.deepcopy(original)

original.append(["Databases", 5])
print(original)
print(alias)
print(shallow)
print(deep)
original[0][1]=3
print(original)
print(alias)
print(shallow)
print(deep)"""

wrong_matrix = [[0] * 3] * 3
print(wrong_matrix[0] is wrong_matrix[1])
wrong_matrix[0][0] = 1
print(wrong_matrix)

correct_matrix = [[0] * 3 for _ in range(3)]
print(correct_matrix[0] is correct_matrix[1])
correct_matrix[0][0] = 1
print(correct_matrix)