import random
import time

red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
green = [0]

def roulette():
    
    """ Таймер задержки. Генерация случайного числа и
    сравнение его со списками (массивами). Полученый
    результат выводится на экран и возвращается для
    дальнейшего сравнения в функции result().

    """
    
    print('Рулетка вращается. Ожидайте')
    wait_time = random.randint(5,15)
    time.sleep(wait_time)
    num_roulette = random.randint(0, 36)  # В какую ячейку попал шарик
    if choice == "number":                # Какому цвету пренадлежит число (число + цвет)
        if num_roulette in red:
            print(num_roulette, "red")
            return num_roulette
        elif num_roulette in black:
            print(num_roulette, "black")
            return num_roulette
        elif num_roulette in green:
            print(num_roulette, "ZERO")
            return num_roulette
    elif choice_color == "black" or choice_color == "red":
        if num_roulette in red:            # Какому цвету пренадлежит число (только цвет)
            print("red")
            return "red"
        elif num_roulette in black:
            print("black")
            return "black"
        elif num_roulette in green:
            print("ZERO")
    
def result():
    
    """ Сравнивание результата функции roulette()
    со значениями введёнными с клавиатуры.
    Результат выводится на экран.

    """
    
    if choice == "color":
        if result_roulette == choice_color:
            print('\aПоздравляем! Вы выйграли')
        else:
            print('К сожалению Вы проиграли')
    elif choice == "number":
        if result_roulette == num:
            print('\aПоздравляем! Вы выйграли')
        else:
            print('К сожалению Вы проиграли')

def errore():
    print('Не верный выбор! Вы упустили свой шанс...')
    if i == 2:
        print('СОБЕРИТЕСЬ, победа любит внимательных!')     

print('Здравствуйте! Сколько раз вы хотите сыграть?')
i = int(input())  # Количество игр (1 игра = 1 цикл кода)
while i != 0:
    print('Сделайте вашу ставку!', '\nВыберите: "number" или "color"')
    choice = str(input())
    if choice == "color":
        print('black или red?')
        choice_color = str(input())
        if choice_color == "black" or choice_color == "red":
            result_roulette = roulette()
            result()
            i -= 1  # Уменьшаем количество игр на 1
        else:
            errore()
            i -= 1
    elif choice == "number":
        print('На какое число вы хотите поставить от 0 до 36?')
        num = int(input())
        if 0 <= num <= 36: 
            result_roulette = roulette()
            result()
            i -= 1  
        else:
            errore()
            i -= 1
    else:
        errore()
        i -= 1
        
print('На этом всё. Спасибо за игру')
exit_time = int(5)
time.sleep(exit_time)



