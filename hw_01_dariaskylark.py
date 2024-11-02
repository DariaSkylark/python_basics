# Задача: Переопределение переменных
# Создайте переменную `x`, присвойте ей значение 10. Затем измените значение переменной `x` на 20.
# Выведите значение `x` на экран после каждого изменения.

# Решение: Переопределение переменных

x = 10
print(x)

x = 20
print(x)


# Задача: Обмен значениями
# Создайте две переменные `a` и `b`, присвойте им любые числовые значения. Затем поменяйте их местами
# (значение `a` должно стать значением `b`, а значение `b` — значением `a`). Выведите значения `a` и `b` после обмена.
# **Примечание**: Явное присвоение значения (такое как `a = 10`) в переменные `a` и `b` можно только по одному разу в начале.
# Все последующие присвоения в эти переменные допускается только с использованием значений других переменных
# (в таком виде `a = c`). Можно использовать больше переменных.

# Решение: Обмен значениями

a = c = 1
b = d = 0

a = d
b = c

print(a)
print(b)


# Задача: Арифметические операции
# Создайте переменную `num`, присвойте ей значение 5. Затем выполните следующие операции и переопределите `num` после каждой:
# 1. Увеличьте `num` на 10.
# 2. Уменьшите `num` на 3.
# 3. Умножьте `num` на 2.
# 4. Разделите `num` на 4.
# Выведите значение `num` после каждой операции.
# **Примечание**: Помните что вы можете использовать короткую форму записи данных операций (`x += 1`)
# и длинную форму записи (`x = x + 1`).

# Решение: Арифметические операции

num = 5

num += 10
print(num)

num -= 3
print(num)

num *= 2
print(num)

num /= 4
print(num)


# Задача: Объединение строк
# Создайте переменную `greeting`, присвойте ей значение "Привет". Затем переопределите `greeting`, добавив к ней ваше имя.
# В конце выведите полное приветствие.

# Решение: Объединение строк

a = "Привет"
b = "Дарья"

greeting = a
greeting = a + ", " + b
print(greeting)


# Задача: Форматирование строк
# Напишите программу, которая запрашивает у пользователя его имя, возраст и любимое число используя функцию `input()`.
# Затем выведите сообщение, которое включает все эти данные. Например: `"Привет, {имя}! Тебе {возраст} лет, и твое любимое число - {число}"`.

# Решение: Форматирование строк
name = input("Enter your name: ")
age = input("Enter your age: ")
fav_num = input("Enter your favourite number: ")

print(f"Hello, {name}! Your age is {age}, and your favourite number is {fav_num}. \nYou are awesome!")


# Задача: Счетчик
# Создайте переменную `counter` и присвойте ей значение 0. Также создайте переменную `x` со значением типа `float`.
# Произведите несколько арифметических операций с `x` (по одной операции за раз) и после выполнения каждой операции
# увеличьте значение счетчика на 1. В результате выведите строку "Переменная Х была изменена {} раз".

# Решение: Счетчик
counter = 0
x = float(10)

x += 10
counter += 1

x *= 5
counter += 1

x /= 10
counter += 1

print(f"Переменная была изменена {counter} раз.")


# Задача: Преобразование типов
# Создайте программу, которая запрашивает у пользователя два числа. Проверьте какой тип данных вы получаете
# в результате выполнения функции `input()`. Преобразуйте их в целые числа и выведите их сумму, разность,
# произведение и частное.

# Решение: Преобразование типов

print("This is a program that performs addition, subtraction, multiplication and division with the two numbers you enter.")

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

print(type(num1))
print(type(num2))

num1 = int(num1)
num2 = int(num2)

print(f"The sum of the first and second number is: {num1 + num2}.")
print(f"The difference between the first and second number is: {num1 - num2}.")
print(f"The product of the first and second number is: {num1 * num2}")
print(f"The quotient of the first and second number is: {num1 / num2}")


# Задача: Периметр и площадь прямоугольника
# Напишите программу, которая запрашивает у пользователя длину и ширину прямоугольника, а затем вычисляет и выводит его
# периметр и площадь.

# Решение: Периметр и площадь прямоугольника

print("This is a program that counts the perimeter and area of a rectangle based on the length and width that you enter.")

length = input("Please enter the length of the rectangle: ")
width = input("Please enter the width of the rectangle: ")

perimeter = 2 * (int(length) + int(width))
area = int(length) * int(width)

print(f"The perimeter of the rectangle is {perimeter} and the area of the rectangle is {area}.")


# Задача: Работа со строками
# Создайте программу, которая принимает строку от пользователя и выводит нексколько ее вариаций:
# в верхнем регистре, в нижнем регистре и без пробелов. Также выведите количество символов в изначальной строке.

# Решение: Работа со строками

print("This is a program that alters your string and counts the number of symbols in it.")

user_string = input("Please enter your string: ")

print(f"Here is your string in uppercase: {user_string.upper()}")
print(f"Here is your string in lowercase: {user_string.lower()}")
print(f"Here is your string without whitespaces: {user_string.replace(" ", "")}")
print(f"Here is the number of symbols in your initial string: {len(user_string)}")


# Задача: Работа со строками и списками
# Напишите программу, которая запрашивает у пользователя предложение и разбивает его на слова.
# Затем выведите количество слов в предложении.

# Решение: Работа со строками и списками

print("This is a program that counts the number of words in your sentence.")

sentence = input("Please enter your sentence: ")
new_list = sentence.split()
el_num = len(new_list)

print(f"The number of words in your sentence is {el_num}")


# Задача: Создание и работа со списками
# Напишите программу, которая запрашивает у пользователя 5 чисел, сохраняет их в списке. Выведите список.

# Решение: Создание и работа со списками

print("This is a program that makes a list of the five numbers you enter.")

num1 = int(input("Please enter your first number: "))
num2 = int(input("Please enter your second number: "))
num3 = int(input("Please enter your third number: "))
num4 = int(input("Please enter your forth number: "))
num5 = int(input("Please enter your fifth number: "))

your_list = [num1, num2, num3, num4, num5]

print(f"Here is your list of numbers: {your_list}.")