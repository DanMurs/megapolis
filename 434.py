import csv
#“У персонажа\t<characters>\tв игре\t<GameName>\tнашлась ошибка с кодом:\t <nameError>.\tДата фиксации:\t <date>”
header = 'GameName$characters$nameError$date'
with open('game.txt', encoding='utf8') as fd:
    data = fd.readlines()

data = [i.strip().split('$') for i in data]

with open('game_new.csv', 'w', encoding='utf-8') as fd:
    for row in data:
        if '55' in row[2]:
            row[2] = 'Done'
            row[3] = '0000-00-00'
        print(row, file=fd)









