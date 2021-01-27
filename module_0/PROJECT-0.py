#!/usr/bin/env python
# coding: utf-8

# In[27]:


import numpy as np    
range_min = 1                                             # начальный диапазон поиска числа от 1 до 100
range_max = 100
some_number = np.random.randint(range_min, range_max+1)   # загадали число
print(f"Загадано число от {range_min} до {range_max}\n")
attempts = 0                                              # счетчик попыток
success = False                                           # число не угадано

while not(success):
    number = guess(range_min, range_max)
    [success, compare_result] = test(number)
    attempts += 1                        # одна попытка использована
    [range_min, range_max] = range_shortening(number, compare_result, range_min, range_max)
    
print (f"\nВы угадали число {some_number} за {attempts} попыток.")


# Проверка числа
def test(guessed_number):
    if some_number == guessed_number:   # число угадано!
        success = True                
        compare_result = True           # фиктивное значение, при success=True не обрабатывается в дальнейшем
    elif some_number > guessed_number:
        print (f"Угадываемое число больше {guessed_number}")
        success = False 
        compare_result = True 
    else:
        print (f"Угадываемое число меньше {guessed_number}")
        success = False 
        compare_result = False
    return [success,         # True - число угадано, False - число не угадано
            compare_result]  # True - угадываемое число больше или равно, False - угадываемое число меньше                


# Угадывание числа
def guess(range_min, range_max):
    number = int(range_min + (range_max-range_min)/2)  # предполагаемое число выгоднее всего спрашивать в середине диапазона
    print(f"Это число - {number}?")
    return number


# Сужение диапазона поиска
def range_shortening(number, compare_result, range_min, range_max):
    if compare_result:
        range_min = number + 1    # число не меньше указанного
    else:
        range_max = number - 1    # число не больше указанного
    return [range_min, range_max]

