stroka = input('Введите предложение:\n')
if stroka[-1] == '.':
    stroka = stroka[0:-1]
    stroka_set = set(stroka.split(' '))
    print(stroka_set)
else:
    stroka_set = set(stroka.split(' '))
    print(stroka_set)
