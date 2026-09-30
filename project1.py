#игра камень онжницы бумага
import random
import time
import webbrowser as web

def win():
    print('ты победиль!')
def los():
    print('ты пройграл')
def draw():
    print('ничия')

game = False
game2 = False

p_scr = 0
b_scr = 0
print("1.Камень ножницы бумага✌️🗿🧻")
print("2. угадай кейс💵")
print("")
games = input("Во что хотите играть:")



if games == "1":
    game_menu = input("хотите сыграть в камень ножницы бумага? (да/нет): " )
    if game_menu == "да":
        game = True
        print("чтобы выйтий из игры напишите 'стоп'")
        print('чтобы сбросить счет напишите "сброс"')
    else:
        game = False
elif games == "2":
    game2 = True



options = ['камень', 'ножницы', 'бумага']

time.sleep(1)
while game:
    player_choice = input("Выберите камень, ножницы или бумагу: ")
    if player_choice == "стоп":
        print("Спасибо за игру!")
        game = False
    if player_choice == 'сброс':
        print('счет сброшен!')
        p_scr = 0
        b_scr = 0


    computer_choice = random.choice(options)
    if player_choice == computer_choice:
        draw()
    elif player_choice == "камень":
        if computer_choice == 'бумага':
            print('компютер:' + computer_choice)
            los()
            b_scr += 1

        elif computer_choice == 'ножницы':
            print(computer_choice)
            win()
            p_scr += 1

    if player_choice == "бумага":
        if computer_choice == 'ножницы':
            print('компютер:' + computer_choice)
            los()
            b_scr += 1

        elif computer_choice == 'камень':
            print(computer_choice)
            win()
            p_scr += 1

    if player_choice == "ножницы":
        draw()

        if computer_choice == 'камень':
            print('компютер:' + computer_choice)
            los()
            b_scr += 1

        elif computer_choice == 'бумага':
            print(computer_choice)
            win()
            p_scr += 1
    time.sleep(0.3)
    print("Твой шет:" + str(p_scr), " бот:" + str(b_scr))



#2 game
balance = 100000000000
game2_menu = 0
time.sleep(0.3)
while game2:


    time.sleep(0.5)

    print("баланс:"+ str(balance))
    print("1.угадать число")
    print("2.магазин ")
    game2_menu = input("выберите(число):")

    if game2_menu == "1":
        time.sleep(0.2)
        print("(В одном кейсе миллион а в других ничева!задача угадать кейс! всего кейсов 5 в 2 кейсах есть пройгрыш)")
        print("")
        time.sleep(3)
        cases = [1, 2, 3, 4, 5]
        win_case = random.choice(cases)
        choice_plr = int(input("напшите цисло от 1 до 5"))
        if choice_plr == win_case:
                win()
                balance += 1000000
        else:
            los()
            balance -= 100000
            print("ты потерял 100к!")
    elif game2_menu == "2":
        time.sleep(0.2)
        print("1.чат гпт-100кк")
        print("2.Gemini-50kk")
        print("3.Grok-30kk")
        print("4.Youtube-1kk")
        magaz = input("ваш выбор:")
        if magaz == "1":
            if balance >= 100000000:
                print("успешно куплено!")
                time.sleep(0.2)
                web.open("https://chatgpt.com")
            else:
                print("Не получилось!")
        elif magaz == "2":
            if balance >= 50000000:
                print("успешно куплено!")
                time.sleep(0.2)
                web.open("https://gemini.google.com/app?hl=ru")
            else:
                print("Не получилось!")
        elif magaz == "3":
            if balance >= 30000000:
                print("успешно!")
                time.sleep(0.2)
                web.open("https://grok.com/")
            else:
                print("Не получилось!")
        elif magaz == "4":
            if balance >= 1000000:
                print("успешно!")
                time.sleep(0.2)
                web.open("https://www.youtube.com/?app=desktop&hl=ru")
            else:
                print("Не получилось!")



print("Спасибо за игру!")
