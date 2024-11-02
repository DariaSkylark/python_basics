# Решение: Переопределение переменных
x = 10
print(x)

x = 20
print(x)

# Решение: Обмен значениями
a = c = 1
b = d = 0

a = d
b = c

print(a)
print(b)

# Решение: Арифметические операции
num = 5

num += 10
print(num)

num -= 3
print(num)

num *= 2
print(num)

num /=4
print(num)

# Решение: Объединение строк
a = "Привет"
b = "Дарья"

greeting = a
greeting = a + ", " + b
print(greeting)

#Решение: Форматирование строк
name = input("Enter your name: ")
age = input("Enter your age: ")
fav_num = input("Enter your favourite number: ")

print(f"Hello, {name}! Your age is {age}, and your favourite number is {fav_num}. \nYou are awesome!")

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

# Решение: Периметр и площадь прямоугольника
print("This is a program that counts the perimeter and area of a rectangle based on the length and width that you enter.")

length = input("Please enter the length of the rectangle: ")
width = input("Please enter the width of the rectangle: ")

perimeter = 2 * (int(length) + int(width))
area = int(length) * int(width)

print(f"The perimeter of the rectangle is {perimeter} and the area of the rectangle is {area}.")

# Решение: Работа со строками
print("This is a program that alters your string and counts the number of symbols in it.")

user_string = input("Please enter your string: ")

print(f"Here is your string in uppercase: {user_string.upper()}")
print(f"Here is your string in lowercase: {user_string.lower()}")
print(f"Here is your string without whitespaces: {user_string.replace(" ", "")}")
print(f"Here is the number of symbols in your initial string: {len(user_string)}")

# Решение: Работа со строками и списками
print("This is a program that counts the number of words in your sentence.")

sentence = input("Please enter your sentence: ")
new_list = sentence.split()
el_num = len(new_list)

print(f"The number of words in your sentence is {el_num}")

# Решение: Создание и работа со списками
print("This is a program that makes a list of the five numbers you enter.")

num1 = int(input("Please enter your first number: "))
num2 = int(input("Please enter your second number: "))
num3 = int(input("Please enter your third number: "))
num4 = int(input("Please enter your forth number: "))
num5 = int(input("Please enter your fifth number: "))

your_list = [num1, num2, num3, num4, num5]

print(f"Here is your list of numbers: {your_list}.")