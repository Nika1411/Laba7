#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант17
# Ввести список А из 10 элементов, найти квадраты элементов кратных 4 и их количество.Преобразованный массив вывести
import sys

if __name__ == '__main__':
    A = tuple(map(int, input().split()))
    if len(A) != 10:
        print("Неверный размер кортежа", file=sys.stderr)
        exit(1)
    i = 1
    L = [i * i for i in A if i % 4 == 0]
    print(tuple(L))
