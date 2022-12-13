#!/usr/bin/env python3
# -- coding: utf-8 --

if __name__ == '__main__':
    s = input()
    a = list(s)
    if len(a) % 2 == 0:
        a[0], a[1] = s[1], s[0]
        a[2], a[3] = s[3], s[2]
        print(''.join(a))
    else:
        print("число нечетное")