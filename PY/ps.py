#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
stroka = input('Введите предложение:\n')
if stroka[-1] == '.':
    stroka = stroka[0:-1]
    stroka_set = set(stroka.split(' '))
    print(stroka_set)
else:
    stroka_set = set(stroka.split(' '))
    print(stroka_set)
