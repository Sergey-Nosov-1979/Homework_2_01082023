"""Уставшие от необычно теплой зимы, жители решили узнать, 
действительно ли это самая длинная оттепель за всю историю 
наблюдений за погодой. Они обратились к синоптикам, а те, в 
свою очередь, занялись исследованиями статистики за 
прошлые годы. Их интересует, сколько дней длилась самая 
длинная оттепель. Оттепелью они называют период, в 
который среднесуточная температура ежедневно превышала 
0 градусов Цельсия. Напишите программу, помогающую 
синоптикам в работе.
Пользователь вводит число N – общее количество
рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
располагается N целых чисел.
Каждое число – среднесуточная температура в
соответствующий день. Температуры – целые числа и лежат в
диапазоне от –50 до 5"""


N = int(input('Ко-во дней: '))
local_max = 0
global_max = 0

# ГДЕ ОШИБКА?
for _ in range(N): # Знак "_" мне не знаком, заменить "i"
    x = int(input('Темпрература: '))
    print(x)
    if x > 0:
        local_max += 1
    else:
        if local_max > global_max:
            global_max = local_max
            local_max = 0   # Необходимо обнулить счетчик, так как оттепель прирвалась
        else:
            local_max = 0
print(f'Ко-во дней = {global_max}')