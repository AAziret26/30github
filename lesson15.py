try:
    num = int(input("Введите число: "))
    print("Результат:", 10 / num)
except ZeroDivisionError:
    print("Ошибка: деление на ноль!")
except ValueError:
    print("Ошибка: введите число!")
