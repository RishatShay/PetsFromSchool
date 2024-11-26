from random import *

to_incorrect = ['Нет, в этот раз правда не на твоей стороне', 'Не правда, не правда, не правда!', 'Ты шутишь?',
                'Это самое неподходящее число из всех, что я видел', 'Нет, нет, нет. И еще раз - нет', 'Не угадал',
                'Вовсе не так!', 'Попробуй еще, ты ведь не компьютер, а я, к слову, ДА! xd)',
                'Хмм... Подумай еще, хорошо?',
                'Не хочу показаться грубым, но я всего лишь компьютер. Так что, давай по новой!']

to_congratulate = ['Угадал наконец, поздравляю!', 'Ура победителю!!!', 'Награда самый умный присуждается игроку!',
                   'Ты молодец! Это оно', 'Ты что жулик? Так быстро угадать надо еще умудриться!',
                   'Рускоплескания и авации, поздравляю!', 'Как круто, ты уже угадал!',
                   'Был у меня знакомый компьютер, так же быстро отгадывал, ты почти как он!',
                   'Умница, отгадал таки', 'Число было успешно отгадано...Бип-бип...']

to_replay = ['Может быть еще разок', 'Не время останавливаться, давай еще', 'Не хочешь ещё?',
             'Ты так хорошо отгадываешь, не хочешь остаться', 'Ну что? Может еще разок сыграем',
             'Я ни на что не намекаю, но давай еще', 'Я не прочь сыграть с тобой еще раз',
             'Ну что чемпион по отгадыванию, еще разок?', 'Слушай, а давай ещё', 'С тобой так интресно, может еще?']

to_more = ['Это слишком много для моего числа', 'Может введешь поменьше чего-нибудь', 'А моё число определенно меньше',
           'Я меньше загадывал', 'Еще чуток убрать и угадаешь(или не чуток:)', 'Большевато твоё число',
           'Ух-ты, какое здоровое число. Моё меньше было', 'Уменьши число и никто не пострадает',
           'У моего создателя устали пальцы печатать, так что: МЕНЬШЕ!', 'Ох-ох-ох. Слишком большое число']

to_less = ['Маловато, но вкусновато. Ой о чём это я? Просто маловато', 'Всегда нужно куда-то РАСТИ',
           'Больше, конечно больше', 'Ты не мог бы чутка увеличить', 'Я уверен, что оно было больше',
           'С  таким маленьким числом далеко не уйдешь', 'Число маловато (с)Конфуций', 'Мне нужно больше',
           'Число как дом, чем БОЛЬШЕ, тем лучше', 'С такими маленькими числами не работаю!']


def valid_input():
    value = input()
    if not value.isdigit():
        print('Что это за белеберда? Давай снова')
        return valid_input()
    elif left_board <= int(value) <= right_board:
        return int(value)
    else:
        print('Слушай, число из диапазона выходит. Сам же обозначал. Не помнишь?')
        print(f'Давай напомню, мне не сложно. Угадывай от {left_board} до {right_board} (включительно)')
        return valid_input()


def play():
    secret = randint(left_board, right_board)

    while True:
        user = valid_input()
        if user < secret:
            print(to_incorrect[randint(0, 9)])
            print(to_less[randint(0, 9)])
        elif user > secret:
            print(to_incorrect[randint(0, 9)])
            print(to_more[randint(0, 9)])
        else:
            print(to_congratulate[randint(0, 9)])
            print(to_replay[randint(0, 9)])
            break


def valid_border():
    border = input()
    if not border.isdigit():
        print('Введи уж целое число!')
        return valid_border()
    elif -10 ** 3 < int(border) < 10 ** 3:
        return int(border)
    else:
        print('Я не хочу ждать полдня пока ты угадаешь число в таких границах. Возьми от -1000 до 1000')
        return valid_border()


def get_boarders():
    print('Давай настроим границы. От какого и до какого числа ты будешь угадывать\n')
    print('\t\t\tСначала левая граница. Вводи не бойся')
    left_border = valid_border()
    print('Теперь правая. Вводи, будь так любезен')
    right_boarder = valid_border()
    if left_border < right_boarder:
        return left_border, right_boarder
    else:
        print('Неправильные у тебя какие-то границы. Давай так, чтобы правая была меньше левой')
        return get_boarders()


#  Угадайка
print('Добро пожаловать в цифровую угадайку!!!')
while True:
    print('Хочешь сыграть? ("да" - играть; "нет" или что угодно другое - оставить меня в одиночестве)')
    if input().lower() == 'да':
        left_board, right_board = get_boarders()
        print('Твои границы:', left_board, right_board)
        print('Я загадал. Вводи своё предположение')
        play()
    else:
        print('Пока!\nЗаходи ещё')
        break
