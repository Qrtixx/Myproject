import sys
import time
import threading
import queue

try:
    import msvcrt
except ImportError:
    msvcrt = None

# образовательное приложение с заметками, карточками и викторинами

users = {}
notes_data = []
flashcards_data = []
quizzes_data = []

QUIZ_TIME_LIMIT = 10


def timed_input(prompt, timeout):
    if msvcrt:
        print(prompt, end='', flush=True)
        start_time = time.time()
        line = ''
        while True:
            if msvcrt.kbhit():
                ch = msvcrt.getwch()
                if ch in ('\r', '\n'):
                    print()
                    return line
                if ch == '\b':
                    if line:
                        line = line[:-1]
                        print('\b \b', end='', flush=True)
                else:
                    print(ch, end='', flush=True)
                    line += ch
            if time.time() - start_time >= timeout:
                print()
                return None
            time.sleep(0.01)
    else:
        print(prompt, end='', flush=True)
        q = queue.Queue()

        def read_input():
            try:
                q.put(sys.stdin.readline())
            except Exception:
                q.put('')

        thread = threading.Thread(target=read_input, daemon=True)
        thread.start()
        try:
            line = q.get(timeout=timeout)
            return line.rstrip('\n')
        except queue.Empty:
            print()
            return None


def reg():
    print("Регистрация")
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    users[username] = password
    print("Регистрация успешна! Данные не сохраняются после выхода.")


def login():
    print("Вход")
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    if users.get(username) == password:
        print("Вход успешен!")
        return True
    print("Неверное имя пользователя или пароль.")
    return False


def main_menu():
    while True:
        print("\nГлавное меню:")
        print("1. Заметки")
        print("2. Карточки")
        print("3. Викторины")
        print("4. Выход")   
        choice = input("Выберите опцию: ")
        if choice == "1":
            notes_menu()
        elif choice == "2":
            flashcards_menu()
        elif choice == "3":
            quizzes_menu()
        elif choice == "4":
            print("Выход из приложения. Все данные будут забыты.")
            sys.exit()
        else:
            print("Неверный выбор. Попробуйте снова.")


def notes_menu():
    while True:
        print("\nЗаметки:")
        print("1. Добавить заметку")
        print("2. Показать заметки")
        print("3. Назад")
        choice = input("Выберите опцию: ")
        if choice == "1":
            add_note()
        elif choice == "2":
            show_notes()
        elif choice == "3":
            return
        else:
            print("Неверный выбор. Попробуйте снова.")


def add_note():
    print("\nДобавление заметки")
    note = input("Введите заметку: ")
    notes_data.append(note)
    print("Заметка добавлена.")


def show_notes():
    print("\nСохранённые заметки:")
    if not notes_data:
        print("Заметок ещё нет.")
        return
    for index, note in enumerate(notes_data, start=1):
        print(f"{index}. {note}")


def flashcards_menu():
    while True:
        print("\nКарточки:")
        print("1. Добавить карточку")
        print("2. Учиться по карточкам")
        print("3. Показать все карточки")
        print("4. Назад")
        choice = input("Выберите опцию: ")
        if choice == "1":
            add_flashcard()
        elif choice == "2":
            study_flashcards()
        elif choice == "3":
            show_flashcards()
        elif choice == "4":
            return
        else:
            print("Неверный выбор. Попробуйте снова.")


def add_flashcard():
    print("\nДобавление карточки")
    question = input("Введите вопрос: ")
    answer = input("Введите ответ: ")
    flashcards_data.append((question, answer))
    print("Карточка добавлена.")


def show_flashcards():
    print("\nСписок карточек:")
    if not flashcards_data:
        print("Карточек ещё нет.")
        return
    for index, (question, answer) in enumerate(flashcards_data, start=1):
        print(f"{index}. Вопрос: {question} | Ответ: {answer}")


def study_flashcards():
    print("\nУчебный режим карточек")
    if not flashcards_data:
        print("Карточек ещё нет. Сначала добавьте хотя бы одну.")
        return
    for index, (question, answer) in enumerate(flashcards_data, start=1):
        print(f"\nКарточка {index}")
        print(f"Вопрос: {question}")
        input("Нажмите Enter, чтобы увидеть ответ...")
        print(f"Ответ: {answer}")
    print("Вы просмотрели все карточки.")


def quizzes_menu():
    while True:
        print("\nВикторины:")
        print("1. Добавить викторину")
        print("2. Пройти викторину")
        print("3. Показать все викторины")
        print("4. Назад")
        choice = input("Выберите опцию: ")
        if choice == "1":
            add_quiz()
        elif choice == "2":
            take_quiz()
        elif choice == "3":
            show_quizzes()
        elif choice == "4":
            return
        else:
            print("Неверный выбор. Попробуйте снова.")


def add_quiz():
    print("\nДобавление викторины")
    question = input("Введите вопрос викторины: ")
    answer = input("Введите ответ викторины: ")
    quizzes_data.append((question, answer))
    print("Викторина добавлена.")


def show_quizzes():
    print("\nСписок викторин:")
    if not quizzes_data:
        print("Викторин ещё нет.")
        return
    for index, (question, answer) in enumerate(quizzes_data, start=1):
        print(f"{index}. Вопрос: {question} | Ответ: {answer}")


def take_quiz():
    print("\nРежим викторины")
    if not quizzes_data:
        print("Викторин ещё нет. Сначала добавьте хотя бы одну.")
        return
    correct = 0
    for index, (question, answer) in enumerate(quizzes_data, start=1):
        print(f"\nВопрос {index}: {question}")
        user_answer = timed_input(f"Ваш ответ (есть {QUIZ_TIME_LIMIT} секунд): ", QUIZ_TIME_LIMIT)
        if user_answer is None:
            print(f"Время вышло! Правильный ответ: {answer}")
            continue
        if user_answer.strip().lower() == answer.strip().lower():
            print("Правильно!")
            correct += 1
        else:
            print(f"Неправильно. Правильный ответ: {answer}")
    print(f"\nВикторина завершена. Правильных ответов: {correct}/{len(quizzes_data)}")


if __name__ == "__main__":
    reg()
    if login():
        print("Добро пожаловать в образовательное приложение!")
        main_menu()
    else:
        print("Попробуйте снова.")


