import random

def guess_number():
    print("Игра 'Угадай число'!")
    secret_number = random.randint(0, 100)
    while True:
        guess = int(input("Введите число от 0 до 100: "))
        if guess == secret_number:
            print("Поздравляю, вы угадали число!")
            return
        elif guess < secret_number:
            print("Загаданное число больше")
        else:
            print("Загаданное число меньше")

def multiplication_table():
    print("Таблица умножения:")
    table = [[0 for x in range(10)] for y in range(10)]
    for i in range(10):
        for j in range(10):
            table[i][j] = (i+1)*(j+1)
    for row in table:
        print(row)

def find_divisors():
    print("Вывод делителей числа:")
    while True:
        num = int(input("Введите число (для выхода введите 0): "))
        if num == 0:
            return
        divisors = []
        for i in range(1, num+1):
            if num % i == 0:
                divisors.append(i)
        print("Делители числа {}: {}".format(num, divisors))

def main():
    while True:
        print("\nВыберите программу:")
        print("1. Игра 'Угадай число'")
        print("2. Таблица умножения")
        print("3. Вывод делителей числа")
        print("0. Выход")
        choice = int(input())
        if choice == 0:
            break
        elif choice == 1:
            guess_number()
        elif choice == 2:
            multiplication_table()
        elif choice == 3:
            find_divisors()
        else:
            print("Неверный выбор")

if __name__ == '__main__':
    main()