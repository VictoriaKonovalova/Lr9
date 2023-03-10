#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Создайте словарь, связав его с переменной school , и наполните данными,
которые бы отражали количество учащихся в разных классах (1а, 1б, 2б, 6а, 7в и т. п.).
Внесите изменения в словарь согласно следующему: а) в одном из классов изменилось
количество учащихся, б) в школе появился новый класс, с) в школе был расформирован
(удален) другой класс. Вычислите общее количество учащихся в школе.
"""

if __name__ == '__main__':
    school = {'1a': 24, "1б": 29, '2б': 28, '6а': 19, '7в': 30}

    school['1a'] = 21
    school['6а'] = 23
    del school['7в']
    print(school)

    summ = sum(klass for klass in school.values())
    print(f"Общее количество учащихся в школе: {summ}")
