'''Задание 3:
Создайте словарь со списком вещей для похода в качестве ключа 
и их массой в качестве значения. Определите какие вещи влезут в 
рюкзак передав его максимальную грузоподъёмность. Достаточно 
вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.'''

BACKPACK = {'спальник': 320, 'коврик': 200, 'фонарик': 80, 'котелок': 200,
            'термос': 250, 'тарелка': 50, 'кружка': 30, 'ложка': 10,
            'куртка': 300, 'брюки': 150, 'ботинки': 500, 'шапка': 30,
            'носки': 10}
things_in_backpack = {}
things_not_in_backpack = {}
list_possible_options = []
backpack_weight = int(input('Введите допустимый вес рюкзака: '))
for i in range(1, 2**len(BACKPACK)):
    possible_options = list(bin(i)[2:].zfill(len(BACKPACK)))
    COUNTER = 0
    TOTAL_WEIGHT = 0
    for key, value in BACKPACK.items():
        if possible_options[COUNTER] == '1':
            things_in_backpack[key] = value
            TOTAL_WEIGHT += value
        else:
            things_not_in_backpack[key] = value
        COUNTER += 1
    if TOTAL_WEIGHT == backpack_weight:
        list_possible_options.append(things_in_backpack)
    if TOTAL_WEIGHT < backpack_weight and len(things_not_in_backpack) == 0:
        list_possible_options.append(things_in_backpack)
    if TOTAL_WEIGHT < backpack_weight and len(things_not_in_backpack) != 0:
        difference_weight = backpack_weight - TOTAL_WEIGHT
        min_weight_things_not_in_backpack = min(things_not_in_backpack.values())
        if difference_weight < min_weight_things_not_in_backpack:
            list_possible_options.append(things_in_backpack)
    things_in_backpack = {}
    things_not_in_backpack = {}
if len(list_possible_options) != 0:
    for item in list_possible_options:
        print('В рюкзак поместятся:', end=' ')
        print(*item.keys())
else:
    print('В рюкзак ничего не поместиться')
        