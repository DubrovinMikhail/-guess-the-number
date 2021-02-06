def is_valid(s):
    return (s.isdigit() and 1<=int(s)<=100)

from random import randint
a = randint(1,100)
print('Добро пожаловать в числовую угадайку')

while True:
    n=(input('Введите число от1 до 100 '))
    if is_valid(n)==True:
        n=int(n)
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    if n < a:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    elif n > a:
        print('Ваше число больше загаданного, попробуйте еще разок')
    elif n == a:
        print('Вы угадали, поздравляем!')
        break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')



