'''Задание 1:
Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
В результирующем списке не должно быть дубликатов.
[1, 2, 3, 1, 2] -> [1, 2]'''

MY_LIST = [1, 2, 3, 1, 2, 1, 4, 5, 3, 3, 5, 6, 3]
counter_dict = {}
duplicate_list = []
for i in MY_LIST:
    counter_dict[i] = counter_dict.get(i, 0) + 1
for key, value in counter_dict.items():
    if value > 1:
        duplicate_list.append(key)
print(f'Список с дублирующими элементами - {duplicate_list}')
print()

counter_list = [MY_LIST[0]]
duplicate = []
for i in range(1, len(MY_LIST)):
    if MY_LIST[i] in counter_list and MY_LIST[i] not in duplicate:
        duplicate.append(MY_LIST[i])
    counter_list.append(MY_LIST[i])
print(f'Список с дублирующими элементами - {duplicate}')
