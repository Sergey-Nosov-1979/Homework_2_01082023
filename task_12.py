"""Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает два натуральных числа 
X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две
подсказки. Он называет сумму этих чисел S и их произведение P. Помогите
Кате отгадать задуманные Петей числа."""


x = abs(int(input('Введите первое натуральное число X от 1 до 1000 ')))
y = abs(int(input('Введите второе натуральное число Y от 1 до 1000 ')))
if x < 1 or x > 10 or y < 1 or y > 10:
    print('Вы ввели числа не из заданного диапазона - начните сначало!')
else:
    Addition = x + y
    Multiplication = x * y
    stop = 0
    for i in range(1001):
        if stop != 1 and i > 0:
            for j in range(1001):
                if stop != 1 and  j > 0:
                    if i * j == Multiplication and i + j == Addition:
                        print((f'Одно из загаданных чисел - {i}'))
                        print((f'Второе из загаданных чисел - {j}'))
                        stop = 1
                else:
                    j = 1001
        else:
            i = 1001