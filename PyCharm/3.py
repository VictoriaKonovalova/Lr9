#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Создайте словарь, где ключами являются числа, а значениями – строки.
Примените к нему метод items(), c с помощью полученного объекта dict_items создайте
новый словарь, "обратный" исходному, т. е. ключами являются строки, а значениями –
числа.
"""
if __name__ == '__main__':
    my_dict = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five'
    }
    new_dict = {}
    for key, value in my_dict.items():
        new_dict[value] = key
    print(f"Исходный словарь\n {my_dict}")
    print(f"Обратный словарь\n {new_dict}")
