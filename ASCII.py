#рисуем Ёлочку в текстовом режиме ASCII

from colorama import init
from colorama import Fore, Back, Style

init()
y1 = 1
x1 = 1

DELTA_Y = 20
DELTA_X = 40
YOLKA_LEN = 10

#print(Fore.RED + 'some red text')
#print(Back.GREEN + 'and with a green background')
#print(Style.DIM + 'and in dim text')
#print(Style.RESET_ALL)
#print('back to normal now')

#print(Back.YELLOW + 'на желтом фоне')
#print(Style.BRIGHT + 'стал ярче' + Style.RESET_ALL)
#print('обычный текст')

#print('\033[31m' + 'some red text')
#print('\033[39m') # and reset to default color


#print(f'\033[{DELTA_Y};{DELTA_X}H' + '--------')

#ставим красный цвет
print('\033[31m')

#for i  in (range (10)):
#           print(f'\033[{i};{i}H' + 'X')

#левая сторона ёлки
for i in range (YOLKA_LEN-2):
    for j in range (YOLKA_LEN-2-i):
        print(f'\033[{DELTA_Y - i};{DELTA_X - j}H' + 'X')

#правая сторона 
print('\033[31m')
for i in range (YOLKA_LEN-2):
    for j in range (YOLKA_LEN-2-i):
        print(f'\033[{DELTA_Y - i};{DELTA_X + j}H' + 'X')

#а теперь ствол

print('\033[31m')
for j in range (YOLKA_LEN):
        print(f'\033[{DELTA_Y + j};{DELTA_X}H' + '0')




           

