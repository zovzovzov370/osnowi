# print('hello world')
# #функция print нужна для вывода данных в консоли
#
# name = input("скажи свое имя:")
# #переменная, которая хранит в себе строку
# age = int(input("введите свой возраст:"))
# #переменная, которая хранит в себе целочисленное число
#
# water = 4.5
# #переменная,которая хранит в себе дробь
# print(type(age), type(name))
# '''
# функция type - нужна для определения
# типа данных наших переменных
# '''
# print("привет," , name,'тебе',age,'лет')
# print("я пью", water, 'литра водки')
# makaka = int(input('5*8:10=?'))
# print(' правильный ответ 4, ваш ответ:', makaka)
#
#
# #задание 1
# #пользователь вводит с клавиатуры 3 числа необходимо найти сумму чисел
# #найти произведение чисел найти разность чисел найти деление
# #результат операции вывести на экран
# print('сегодня 5 сентября',
#       'я измученный пришел на первую пару','к 8:15',
#       sep='\t', end=' '
#       )
# #\t - текстовая табуляция(3 пробела)
# #\n - перенос на новую строку
# #sep - отступы между параметрами print
# #end - завершение строки
# print('желаю \'всем\' продуктивного дня')
# s_name = input('введите фамилию:')
# date = input('введите ваш год рождения')
# print(f'ваше имя: {name} \n'
#       f'ваша фамилия {s_name} \n'
#       f'ваш возрамт {age} \n'
#       f'ваша дата рождения {date} \n')

# обращение f'' f"" f`` нужно для форматирования
# текста и вставки переменных в строку

'''
арифметические операции в python
** - оператор возведения в степень
print(2**2) #4
// - целочисленное деление
print(6.31 // 3) # 2
% - деление по остатку
print(6 % 2) #
что делать нельзя:
1) делить на 0
2) делить целое на 0
3) находить остаток от делений на 0
функция суммы: sum(1,2,3)#6
функция минимума:min(1,2,3)#1
функция максимума:max(1,2,3) #3
'''


#практика
'''
задание 1 
пользователь вводит с клавиатуры три числа. Необходимо найти сумму чисел, 
произведение чисел. Результат вычислений вывести на экран.
задание 2
пользователь вводит с клавиатуры три числа.
первое число - зп за месяц,
второе число - сумма месячного платежа по кредиту в банке,
третье - задолженость за комунальные услуги.
необходимо вывести на экран сумму,
которая останется у пользователя после всех выплат.
задание 3
напишите программу, вычисляющую площадь ромба.
пользватель с клавиатуры вводит длину двух его диагоналей 
задание 4 
выведите на экране надпись to be or not to be на разных строках
пример вывода
to be 
or not
to be
задание 5
выведите на экран надпись <life is what happens when you're busy making other plans>
john Lennon на разных строках пример вывода:
life is what happens
                      
                      when 
                       
                           you're busy making other plans
                                 
                                                           john Lennon.             
'''
'''
#задание 1
one = int(input('введите число:'))
dva = int(input("введите число:"))
tri = int(input("введите число:"))
print(one + dva + tri)

#задание 2
dengi = int(input('введите три числа: зп за месяц:'))
babki = int(input("сумма месячного платежа по кредиту в банке:"))
rubl = int(input("задолженость за комунальные услуги:"))
print(dengi - babki - rubl)

#задание 3
xz1= int(input("Введите длину первой диагонали: "))
xz2 = int(input("Введите длину второй диагонали: "))
print(f"Площадь ромба: {(xz1 * xz2) / 2}")

#задание 4
print('to be \n'
      'or not \n'
      'to be\n')

#задание 5
print("'Life is what happens \n\n "
      "                       when \n\n "
      "                            you're busy making other plans' \n\n "
      "                                                           John Lennon.")

'''

'''
#условные конструкции
age = int(input("введите ваш возраст: "))
#if (условие) == true:
# функция действие
if age < 10:
      print("ты еще малыш")
elif age < 20 and age > 10:
      print("ты еще подросток")
elif 20 < age < 45:
      print("ты молодеж")
elif 45 < age < 100:
      print("ты уже пенсионер")
else:
      ("некорректный возраст")
'''

'''
#задание 1
пользователь вводит с клавиатуры три числа. В зависимости 
от выбора пользователя программа выводит на экран сумму трех
чисел или произведение трех чисел.
#задание 2
пользователь вводит с клавиатуры три числа. В зависимости 
от выбора пользователя программа выводит максимум из трех, 
минимум из трех или среднее арифметическое.
#задание 3
пользователь вводит с клавиатуры количество метров. в зависимотси 
от выбора пользователя программа переводит метры в мили, дюймы или ярды.
'''

'''
#задание 1
n = int(input("введите первое число"))
n1 = int(input("введите второе число"))
n2 = int(input("введите третье число"))
print("выберите операцию:")
print("1 - сумма трех чисел")
print("2 - произведение трех чисел")
xz = input("ваш выбор 1 или 2: ")
if xz == "1":
    result = n + n1 + n2
    print(f"сумма чисел: {result}")
elif xz == "2":
    result = n * n1 * n2
    print(f"произведение чисел: {result}")
else:
    print("ошибка выберите 1,2")

#задание 2
num1 = int(input("введите первое число"))
num2 = int(input('введите второе число'))
num3 = int(input('введите третье число'))
print("выберите операцию:")
print("1 - максимум из трех")
print("2 - минимум из трех")
print("3 - среднее арифметическое")
xz1 = input("ваш выбор 1, 2, 3: ")
if xz1 == "1":
    result = max(num1, num2, num3)
    print(f"максимальное число:{result}")
elif xz1 ==  "2":
    result = min(num1, num2, num3)
    print(f"минимальное число:{result}")
elif xz1 == "3":
    result = (num1 + num2 + num3) / 3
    print(f"среднее арифметическое:{result}")
else:
    print('ошибка, выбери 1,2,3')

#задание 3
mil = 0.000621371
duim = 39.3701
yard = 1.09361
n = int(input("введите количество метров: "))
print("выберите операцию: ")
print("1 - перевести в мили")
print("2 - перевести в дюймы")
print("3 - перевести в ярды")
n1 = input("ваш выбор: 1, 2, 3")
if n1 == "1":
    result = n * mil
    print(f"метры в милях:{result}")
elif n1 == "2":
    result = n * duim
    print(f"метры в дюймах:{result}")
elif n1 == "3":
    result = n * yard
    print(f"метры в ярдах:{result}")
else:
    print('ошибка, выбери 1,2,3')
 '''
'''
user_value = int(input("введите число "))
var_user = 1
while var_user > 10:
    print(f"{user_value} * {var_user} = {user_value*var_user}")
'''

'''
while True:
    print("ваша задача ввести значение в рублях. \n"
          "выберете пункт для перевода: \n"
          "1. перевод в доллары \n"
          "2. перевод в юани \n"
          "3. перевод в тенге \n"
          "4. перевод в бел. рубли \n"
          "0. выход из приложения")
    user_choice = int(input("ваш выбор: "))
    if user_choice == 0:
        print('до скорой встречи')
        break
    elif user_choice == 1:
         print(f'кол рублей, после операции: {user_ru * 0.011963}')
    elif user_choice == 2:
        print(f'кол рублей после операции: {user_ru * 0.085426}')
    elif user_choice == 3:
        print(f'кол рублей после операции: {user_ru * 6.48}')
    elif user_choice == 4:
        print(f'кол рублей после операции: {user_ru * 0.036396}')
'''

'''
user_min = int(input("введите левую границу диапазона: "))
user_max = int(input("введите правую границу диапазона: "))
user_value = int(input("введите число для поиска в диапазоне: "))
while user_min < user_max:
    if user_min == user_value:
        print(f"  !{user_min}!")
    else:
        print(user_value, end= '')
        user_min += 1
'''
'''
from random import randint
value_random = randint(1, 500)
print('добро пожаловать в игру <угадай число>')
print('ваша задача - угадать число в интервале от 1 до 500 \n'
      'если введен 0 это выход \n'
      'удачи')
user_choice = -50
while user_choice != 0:
    if user_choice < value_random:
        print('ваше число больше')
    elif user_choice > value_random:
        print('ваше число меньше')
    elif user_choice == value_random:
        print("победа")
        break
'''

'''
#задание 1
n = int(input("введите число от 1 до 100: "))
if n < 1 or n > 100:
    print('число должно быть в диапазоне от 1 до 100')
else:
    if n % 3 == 0 or n % 5 == 0:
        print('fizz buzz')
    elif n % 3 == 0:
        print('fizz')
    elif n % 5 == 0:
        print('buzz')
    else:
        print(n)

#задание 2
n = int(input('введите число: '))
n1 = int(input('выберете степень от 0 до 7: '))
if n1 == 0:
    print(n ** 0)
elif n1 == 1:
    print(n ** 1)
elif n1 == 2:
    print(n ** 2)
elif n1 == 3:
    print(n ** 3)
elif n1 == 4:
    print(n ** 4)
elif n1 == 5:
    print(n ** 5)
elif n1 == 6:
    print(n ** 6)
elif n1 == 7:
    print(n ** 7)
else:
    print('не та степень')

#задание 3
n = int(input('введите стоимость разговора: '))
n1 = int(input('выберете с какого оператора вы звоните с 1)МТС или 2)мегафона: '))
n2 = int(input('на какой оператор: 1)Билайн, 2)Теле 2: '))
if n1 == 1:
 if n2 == 1:
    print(n * 1.5)
if n1 == 2:
 if n2 == 1:
    print(n * 1.8)
if n1 == 1:
 if n2 == 2:
    print(n * 1.2)
if n1 == 2:
 if n2 == 2:
     print(n * 1.4)

#задание 4
n = int(input('введите уровень продаж для первого менеджера: '))
n1 = int(input('введите уровень продаж для второго: '))
n2 = int(input('введите уровень продаж для третьего: '))
zp = 200
if n <= 500:
    print(zp + (n * 0.3))
elif n >= 500 or n <= 1000:
    print(zp + (n * 0.5))
elif n >= 1000:
    print(zp + (n * 0.8))
if n1 <= 500:
    print(zp + (n * 0.3))
elif n1 >= 500 or n <= 1000:
    print(zp + (n * 0.5))
elif n1 >= 1000:
    print(zp + (n * 0.8))
if n2 <= 500:
    print(zp + (n * 0.3))
elif n2 >= 500 or n <= 1000:
    print(zp + (n * 0.5))
elif n2 >= 1000:
    print(zp + (n * 0.8))
else:
    print('ошибка')
print(f'самый лучший работник:{max(n,n1,n2)} премия 200$')
'''

'''
string = input()
string1 = 'hello'
print(len(string1))
print(string1 * 10)
print(string + string1)
print(string1[0])
print(string1[0:5])
print(string1[0:10:2])
print(string1.find("world"))
print(string1.find('l'))
#replace(old, new)
print('date_1'.replace("t","TT"))
#метод count - подсчет вхождений(элементов)
print(string1.count('l'))
#использование списков
primes = [2,3,5,7,11,13]
raindow = ['red', 'orange', 'yellow', 'green', 'blue', 'Ingigo', 'Violet']
print(type(primes))
print(primes[0])
print(primes)
for i in primes:
    print(i, end=' ')
print()
list_user = []
from random import randint
for i in range(10):
    list_user.append(randint(1, 10))
print(list_user)
list_user.pop()
print(list_user)
#split and join
# 1 2 3
str_val = input()
str_list = str_val.split()  # str_list = ['1','2','3']
#указание параметра для split - это разделитель строк,
#убирает элемент и формирует список
for i in str_val:
    if type(i) == int: #decimal(i)
        str_list.append(i) #int(i)
lisr_color = ['red', 'green', 'blue']
print("+".join(lisr_color))
#генераторы списков
#заполнить список случайным образом, только четные, 10
list_a = []
while len(list_a)<10:
    a = randint(0, 10)
    if a % 2 == 0:
        list_a.append(a)
print(list_a)
#способ 2
list_b = [i for i in range(10) if a % 2 == 0]
print(list_b)
#list_c = [randint(0,10) for i in range(10)
#практика

задание 1 
написать программу,
вычисляющую произведение элементов списка целых.

list_u = []
for i in range(10):
    list.append(randint(1, 10))
summ = 0
for i in list_u:
    summ += i
print(f"список:{list_u} \nсумма элементов: {summ}")
'''


'''
задание 2
напишите минимума для нахождения(самое маленькое), не используя спец.
функции, в списке целых. список передается в качестве параметра.
полученный результат + список возвращается на экран.
'''
'''
задание 1. Пользователь вводит с клавиатуры два числа (нача
ло и конец диапазона). Требуется проанализировать все 
числа в этом диапазоне по следующему правилу: если 
число кратно 7, его надо выводить на экран.
 Задание 2
 Пользователь вводит с клавиатуры два числа (нача
ло и конец диапазона). Требуется проанализировать все 
числа в этом диапазоне. Нужно вывести на экран:
 1. Все числа диапазона;
 2. Все числа диапазона в убывающем порядке;
 3. Все числа, кратные 7;
 4. Количество чисел, кратных 5.
 Задание 3
 Пользователь вводит с клавиатуры два числа (начало 
и конец диапазона). Требуется проанализировать все числа 
в этом диапазоне. Вывод на экран должен проходить по 
правилам, указанным ниже.
 Если число кратно 3 (делится на 3 без остатка) нужно 
вывести слово Fizz. Если число кратно 5 нужно вывести слово Buzz. Если число кратно 3 и 5 нужно вывести 
Fizz Buzz. Если число не кратно не 3 и 5 нужно вывести 
само число
'''


'''
#задание 1
n = int(input("введите начало диапазона: "))
n1 = int(input("введите конец диапазона: "))
print(f"числа кратные 7 в диапазоне от {n} до {n1}:")
for number in range(n, n1 + 1):
    if number % 7 == 0:
        print(number)

#задание 2
n = int(input("введите начало диапазона: "))
n1 = int(input("введите конец диапазона: "))
print("\n1. все числа диапазона:")
for num in range(n, n1 + 1):
    print(num, end=' ')
print()
print("\n2. числа в убывающем порядке:")
for num in range(n1, n - 1, -1):
    print(num, end=' ')
print()
print("\n3. числа, кратные 7:")
multiples_of_7 = [num for num in range(n, n1 + 1) if num % 7 == 0]
print(*multiples_of_7)
count_multiples_of_5 = sum(1 for num in range(n, n1 + 1) if num % 5 == 0)
print(f"\n4. количество чисел, кратных 5: {count_multiples_of_5}")

#задание 3
n = int(input("начало диапазона: "))
n1 = int(input("конец диапазона: "))
if n % 3 == 0 or n % 5 == 0:
    if n1 % 3 == 0 or n1 % 5 == 0:
        print('fizz buzz')
elif n % 3 == 0:
        print('fizz')
elif n % 5 == 0:
        print('buzz')
elif n1 % 3 == 0:
        print('fizz')
elif n1 % 5 == 0:
        print('buzz')
else:
        print(n)
'''

'''
Задание 1
 Показать таблицу умножения для числа, введенного 
пользователем. Например, если пользователь вводит 
число 7, нужно показать:
 7 * 1 = 7
 7 * 2 = 14
 7 * 3 = 21
 …
 Задание 2
 Написать программу – конвертер валют. Реализовать 
общение с пользователем через меню.
 Задание 3
 Пользователь вводит с клавиатуры две границы ди
апазона и число. Если число не попадает в диапазон, 
программа просит пользователя повторно ввести число, 
и так до тех пор, пока он не введет число правильно. Про
грамма отображает все числа диапазона, выделяя число 
восклицательными знаками. Например:
 1 2 3 !4! 5 6 7.
 Задание 4
 Написать игру «Угадай число». Программа загадывает 
число в диапазоне от 1 до 500. Пользователь пытается
'''

# #задание 1
# n = int(input("введите число: "))
# for i in range(1, 11):
#     result = n * i
#     print(f"{n} * {i} = {result}")
# #задание 2
# def main():
#     exchange_rates = {
#         'USD': 1.0,
#         'EUR': 0.85,
#         'GBP': 0.73,
#         'JPY': 110.0,
#         'RUB': 75.0
#     }
#     while True:
#         print("конвертер волют")
#         print("1) конвертировать валюту")
#         print("2) показать доступные валюты")
#         print("3) выйти из программы")
#         choice = input("выберите пункт меню 1-3: ")
#         if choice == '1':
#             convert_currency(exchange_rates)
#         elif choice == '2':
#             show_currencies(exchange_rates)
#         elif choice == '3':
#             print("до свидания")
#             break
#         else:
#             print("ошибка, выберете 1,2,3")
# def convert_currency(rates):
#     print("\nконвертация валюты")
#     print("доступные валюты:", ", ".join(rates.keys()))
#     from_currency = input("из какой валюты конвертировать например, USD: ").upper()
#     to_currency = input("в какую валюту конвертировать например, EUR: ").upper()
#     if from_currency not in rates or to_currency not in rates:
#         print("ошибка: неизвестная валюта")
#         return
#     try:
#         amount = float(input(f"сумма в {from_currency}: "))
#         if amount <= 0:
#             print("сумма должна быть положительной")
#             return
#     except ValueError:
#         print("ошибка: введите корректное число")
#         return
#     amount_in_usd = amount / rates[from_currency]
#     result = amount_in_usd * rates[to_currency]
#     print(f"\nрезультат конвертации:")
#     print(f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}")
# def show_currencies(rates):
#     print("\nдоступные валюты")
#     for currency, rate in rates.items():
#         print(f"{currency}: 1 USD = {rate} {currency}")
# if __name__ == "__main__":
#     main()
#
# #задание 3
# print("введите границы диапазона:")
# start = int(input("начало: "))
# end = int(input("конец: "))
# if start > end:
#     start, end = end, start
# while True:
#     number = int(input(f"введите число от {start} до {end}: "))
#     if start <= number <= end:
#         break
#     print("число вне диапазона! Попробуйте снова.")
# print(f"\nчисла диапазона {start}-{end}:")
# for i in range(start, end + 1):
#     if i == number:
#         print(f"!{i}!", end=" ")
#     else:
#         print(f"{i}", end=" ")
# print("\n")
#
# #задание 4
# import random
# print("угадай число от 1 до 500")
# secret = random.randint(1, 500)
# popitka = 0
# while True:
#     try:
#         user_guess = int(input("твое число: "))
#         popitka += 1
#         if user_guess < secret:
#             print("больше")
#         elif user_guess > secret:
#             print("меньше")
#         else:
#             print(f"правильно {secret}")
#             print(f"ты угадал за {popitka} попыток")
#             break
#     except:
#         print("вводи только числа")

# задание 1
'''
print('задание 1')
def list(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result
mylist = [2, 3, 4, 5]
print(f"список: {mylist}")
print(f"произведение элементов: {list(mylist)}")
# задание 2
print('задание 2')
def minimum(numbers):
    if not numbers:
        return None
    minvalue = numbers[0]
    for number in numbers:
        if number < minvalue:
            minvalue = number
    return minvalue
mylist = [5, 2, 8, 1, 9, 3]
print(f"список: {mylist}")
print(f"минимальный элемент: {minimum(mylist)}")
#задание 3
print('задание 3')
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
def count_primes(numbers):
    count = 0
    num = []
    for number in numbers:
        if is_prime(number):
            count += 1
            num.append(number)
    return count, num
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
count, primes = count_primes(mylist)
print(f"список: {mylist}")
print(f"простые числа: {primes}")
print(f"количество простых чисел: {count}")
# задание 4
print('задание 4')
def remove_number(numbers, target):
    original_length = len(numbers)
    while target in numbers:
        numbers.remove(target)
    deleted_count = original_length - len(numbers)
    return deleted_count
mylist = [1, 2, 3, 2, 4, 2, 5]
num = 2
print(f"исходный список: {mylist}")
deleted = remove_number(mylist, num)
print(f"число для удаления: {num}")
print(f"количество удаленных: {deleted}")
print(f"список после удаления: {mylist}")
# задание 5
print('задание 5')
def combine_lists(list1, list2):
    combined = list1 + list2
    return combined
n = [1, 2, 3]
n1 = [4, 5, 6]
result = combine_lists(n, n1)
print(f"Первый список: {n}")
print(f"Второй список: {n1}")
print(f"Объединенный список: {result}")
#задание 6
print('задание 6')
def list(numbers, power):
    result = []
    for number in numbers:
        result.append(number ** power)
    return result
my_list = [1, 2, 3, 4, 5]
exponent = 3
result = list(my_list, exponent)
print(f"исходный список: {my_list}")
print(f"степень: {exponent}")
print(f"результат: {result}")


import random
lst = [random.randint(-10, 10) for _ in range(20)]
print("исходный список:", lst)
mid = len(lst) // 2
left_sorted = sorted(lst[:mid])
right_sorted = sorted(lst[mid:], reverse = True)
result = left_sorted + right_sorted
print("результат: ", result)

#задание 2
import random
lst = [random.randint(-20, 20) for _ in range(45)]
print("сходный список:", lst)
size = len(lst) // 3
p1, p2, p3 = lst[:size], lst[size:2*size], lst[2*size:]
result = (
    [x for x in p1 if x % 2 == 0] +
    [max(p2) if i % 2 == 0 else min(p2) for i in range(len(p2))] +
    [x for x in p3 if x % 2 != 0]
)
print("результат: ", result)
'''

# #задание 3
# print('задание 3')
# import random
# def insertion_sort_simple(arr):
#     iterations = 0
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] < key:
#             arr[j + 1] = arr[j]
#             j -= 1
#             iterations += 1
#         arr[j + 1] = key
#         iterations += 1
#     return iterations
# numbers = [random.randint(1, 100) for _ in range(15)]
# print("исходный: ", numbers)
# iterations = insertion_sort_simple(numbers)
# print("результат:", numbers)
# print("итераций: ", iterations)
#
# #задание 4
# print('задание 4')
# list = ["apple", "banana", "cherry", "date", "apricot"]
# print('исходной список:', list)
# sorted_list = sorted(list)
# print("отсортированный", sorted_list)
#
# #задание 5
# print('задание 5')
# def sort_fixed_compact(arr, k):
#     if k < 0 or k >= len(arr):
#         return arr
#     fixed = arr[k]
#     sorted_others = sorted(arr[:k] + arr[k + 1:])
#     return sorted_others[:k] + [fixed] + sorted_others[k:]
# test_cases = [
#     ([7, 2, 9, 1, 5, 3, 8], 2),
#     ([5, 3, 8, 1, 9], 1),
#     ([10, 20, 30, 40], 0),
#     ([1, 2, 3, 4, 5], 4)
# ]
# for arr, k in test_cases:
#     result = sort_fixed_compact(arr, k)
#     print(f"массив: {arr}, k={k}")
#     print(f"результат: {result}")
#     print(f"фиксированный элемент: {arr[k]} остался на позиции {k}")

#points_to_letters = {
#     1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'С', 'Т'],
#     2: ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'],
#     3: ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'],
#     4: ['F', 'H', 'V', 'W', 'Y', 'Р', 'Й', 'Р' 'Ы'],
#     5: ['K', 'Ж', 'З', 'Ч', 'Ц'],
#     8: ['J', 'X', 'Ш', 'Э', 'Ю', 'Х' 'Х'],
#     10: ['Q', 'Z', 'Ф', 'Щ', 'Ъ']
# }
# gamers = {} #словарь игрока
# count_user = int(input("сколько человек будет играть?/:"))
# for i in range(count_user):
#     name = input("введите имя игрока:")
#     gamers[name] = 0
# print(f"писок игроков: \n{gamers}")
# # result = 0
# # 10 раундов
# for raund in range(10):
#     for gamer in gamers.keys():
#         print("*"*11)
#         print(f"ходит игрок {gamer}")
#         answer = input("введите слово:")
#         for i in answer:
#             for key, value in dictionnary.items():
#                 if i in value:
#                     gamers[gamer] += key
# print("игра окончена! \n таблица игроков:")
# for key, value in dictionnary.items():
#     print(f"{key} -> {value} баллов")
# result_user = ' '
# result_user = ' '
# for key, value in gamers.items():
#     if result_value < value:
#         result_value = value
#         result_user = key
# print(f"победитель: {result_user}")
# from sys import intern
#
# backpack = {'зажигалка':20, 'компас':100, 'фрукты':500, 'рубашка':300,
#             'термос':1000, 'аптечка':200, 'куртка':600, 'бинокль':400,
#             'удочка':1300, 'салфетки':40, 'бутерброды':800, 'палатка':5500,
#             'спальный мешок':2500, 'изолента':250, 'котел':3000
# }
# max_mass = int(input("введитемаксимальный вес для похода:"))
# inter_mass = 0
# while iner_mass < max_mass:
#     print(backpack)
#     answer = input("что вы хотите взять с собой:")
#     for key, value in backpack.items():
#         if key == answer:
#             iner_mass += backpack[key]
# print(f"рюкзак заполнен, текущая масса:{iner_mass}")
#
# note_book = {
#     "Маша": {
#         'tel': '+7922123561',
#         'vk': 'vk.com/masha321',
#         'youtube': 'youtube.com/masha321',
#         'telegram': 't.me/masha321'
#     },
#     "Паша": {
#         'tel': '+7922123562',
#         'vk': 'vk.com/pasha123',
#         'youtube': 'youtube.com/pasha123',
#         'telegram': 't.me/pasha123'
#     },
#     "Саша": {
#         'tel': '+7922123563',
#         'vk': 'vk.com/sasha456',
#         'youtube': 'youtube.com/sasha456',
#         'telegram': 't.me/sasha456'
#     }
# }
# print("доступные контакты:", ", ".join(note_book.keys()))
#
# # Запрашиваем имя для поиска
# user_search = input("введите имя из списка контактов: ").capitalize()
#
# # Проверяем, есть ли контакт в книге и выводим информацию
# if user_search in note_book:
#     print(f"\nинформация о контакте {user_search}:")
#     for key, value in note_book[user_search].items():
#         print(f"{key}: {value}")
# else:
#     print(f"контакт '{user_search}' не найден в телефонной книге.")

# print('задание 1')
# print('"Don`t compare yourself with anyone in this world...if you do so, you are insulting\n'
#       'yourself."\n'
#       '\n'
#       'Bill Gates')
#
# print('задание 2')
#
# def get_even_numbers(num1, num2):
#     start = min(num1, num2)
#     end = max(num1, num2)
#     even_numbers = []
#     for number in range(start, end + 1):
#         if number % 2 == 0:
#             even_numbers.append(number)
#     return even_numbers
# result = get_even_numbers(3, 12)
# print(f"четные числа: {result}")
#
# print('задание 3')
#
# def xz(side_length, symbol, is_filled):
#     for row in range(side_length):
#         line = ""
#         for col in range(side_length):
#             if is_filled:
#                 line += symbol + " "
#             else:
#                 if row == 0 or row == side_length - 1 or col == 0 or col == side_length - 1:
#                     line += symbol + " "
#                 else:
#                     line += "  "
#         print(line)
# print("заполненный квадрат 6x6:")
# xz(6, '#', True)
#
# print("\nпустой квадрат 6x6:")
# xz(6, '#', False)

#ксперимент монте-карло
# import datetime
# from random import randint
# def getbirthday(number0fBirthdays):
#     birthdays = [] #писок дней рождений
#     for i in range(number0fBirthdays):
#                 # год в нашей имитации роли не играет,
#         # лишь бы в объектах дней рождения он был однаков
#         start0Year = datetime.date(2000, 1, 1)
#         # случайный день года
#         randomNumber0fDays = datetime.timedelta(randint(0, 364))
#         birthday = start0Year + randomNumber0fDays +randomNumber0fDays
#         birthdays.append(birthday) #добавляем в список
#     return birthdays
#
# '''
# принимает список дней рождений. обрабатывает его и возвращает совпадения в
# датах, которые встречаются несколько раз
# '''
# def getMatch(birtdays):
#     if len(birtdays) == len(set(birtdays)):
#         return None # даты не совпадают, выходим из программы
#     for a, birthdayA in enumerate(birtdays):
#         for b, birthdayB in enumerate(birtdays[a+1 : ]):
#             if birthdayA == birthdayB:
#                 return birthdayA # даты совпали
# # MAIN
# def main():
#     # кортедж месяцев в году
#     Months = ('Jan' , 'Feb' , 'Mar' , 'Apr' , 'May' , "Jun" ,
#               "Jul" , "Aug" , "Sep" , "Oct" , "Nov" , "Dec")
#     print("Добро пожаловать в приложение для симуляции совпадения "
#           "дат рождения")
#     while True: #апрашвает данные, пока пользователь
#         # не введет допустиые значения
#         print("сколько симуляций вы хотите сделать \n P.S. max = 100")
#         response = input("--->")
#         if response. isdecimal() and 0 < int(response) <= 100:
#             numBDdays = int(response)
#             break
#     print()
#     #генерируем и отображаем дни рождения
#     birthdays = getbirthday(numBDdays)
#     for i, birthday in enumerate(birthdays):
#         if i != 0:
#             print(", ", end="")
#         months = Months[birthday.month - 1]
#         dateText = "{} {}".format(months, birthday.day)
#         print(dateText, end="")
#     print()
#     print()
#     print(f"генерация {numBDdays} лучайных симуляций")
#     input("для продолжения введите Enter...")
#     print("запуск 100.000 симуляций")
#     simMatch = 0
#     for i in range(100_000):
#         if i % 100 == 0:
#             print(i, "запущена симуляция...")
#         birthdays = getMatch(birthdays)
#         if getMatch(birthdays) != None:
#             simMatch += 1
#     print("было выполнено 100.000 симуляций.")
#     probability = round (simMatch / 100 * 100, 2)
#     print("процент попадения",probability, "%")
#     print("количество дат для иследования:" ,numBDdays)
#     print("количество циклов симуляции:",simMatch)
#
# if name == '__main__':
#     main()


# import pygame
# import random
# from py2048_classes import Board
# # Создание списка клавиш для игр. прггресса
# from pygame.locals import(
#     K_UP,
#     K_DOWN,
#     K_LEFT,
#     K_RIGHT,
#     K_ESCAPE,
#     KEYDOWN,
#     QUIT,
# )

# # Задаем цвета для игровых полей
# TEXT_DARK = pygame.Color(119, 110, 100)
# TEXT_LIGHT = pygame.Color(255, 255, 255)
# BACKGROUND = pygame.Color(188, 173, 159)
# EMPTY = pygame.Color(206, 192, 179)
# TILE_MAX = pygame.Color(18, 91, 146)
#
# # Задаем цвета для текста
# CELL_STYLES = {
# 0: {"font": TEXT_DARK, "fill": EMPTY},
# 1: {"font": TEXT_DARK, "fill": pygame.Color(239, 229, 218)},
# 2: {"font": TEXT_DARK, "fill": pygame.Color (238, 225, 199)},
# 3: {"font": TEXT_LIGHT, "fill": pygame.Color(242, 177, 121)},
# 4: {"font": TEXT_LIGHT, "fill": pygame.Color(245, 149, 99)},
# 5: {"font": TEXT_LIGHT, "fill": pygame.Color(247, 127, 96)},
# 6: {"font": TEXT_LIGHT, "fill": pygame.Color(246, 94, 59)},
# 7: {"font": TEXT_LIGHT, "fill": pygame.Color(241, 219, 147)},
# 8: {"font": TEXT_LIGHT, "fill": pygame.Color(237, 204, 97)},
# 9: {"font": TEXT_LIGHT, "fill": pygame.Color(235, 193, 57)},
# 10: {"font": TEXT_LIGHT, "fill": pygame.Color(231, 181, 23)},
# 11: {"font": TEXT_DARK, "fill": pygame.Color(192, 154, 16)},
# 12: {"font": TEXT_LIGHT, "fill": pygame.Color(94, 218, 146)},
# 13: {"font": TEXT_LIGHT, "fill": pygame.Color(37, 187, 100)},
# 14: {"font": TEXT_LIGHT, "fil1": pygame.Color (55, 148, 81)},
# 15: {"font": TEXT_LIGHT, "fill": pygame.Color(113, 180, 213)},
# 16: {"font": TEXT_LIGHT, "fill": pygame.Color(25, 130, 205)},
# }
# BORDER_WIDTH = 10
# TILE_SIZE = 100
# NUMBER_OF_ROWS = NUMBER_OF_COLUMNS = 4
# SCREEN_WIDTH = SCREEN_HEIGHT = ((NUMBER_OF_ROWS+1)*BORDER_WIDTH) + (NUMBER_OF_COLUMNS*TILE_SIZE)
# FONT_SIZE = 24
# class Tile(pygame.sprite.Sprite):
#     def __init__(self, row, collumn, value=None):
#         super(Tile, self).__init__()
#         self.font =pygame.font.Font(pygame.font.get_default_font(), FONT_SIZE)
#         self.x_pos = BORDER_WIDTH + (row * (BORDER_WIDTH + TILE_SIZE))
#         self.y_pos = BORDER_WIDTH + (collumn * (BORDER_WIDTH + TILE_SIZE))
#         self.surface = pygame.Surface((TILE_SIZE, TILE_SIZE))
#         self.value = value
#         self.update(value)
#
#     def update(self, value):
#         self.change_fill(value)
#         self.change_text(value)
#         self.value = value
#
#     def change_fill(self, value):
#         if value:
#             if value in CELL_STYLES:
#                 fill_colour = CELL_STYLES[value]["fill"]
#             else:
#                 fill_colour = TILE_MAX
#         else:
#             fill_colour = EMPTY
#         self.surface.fill(fill_colour)
#
#     def change_text(self, value):
#         if value:
#             if value in CELL_STYLES:
#                 text_colour = CELL_STYLES[value]["font"]
#             else:
#                 text_colour = TEXT_LIGHT
#             text_surface = self.font.render(str(2**value), True, text_colour, None)
#             text_rectangle = text_surface.get_rect(center=(TILE_SIZE/2, TILE_SIZE/2))
#             self.surface.blit(text_surface, text_rectangle)
#
#
# class Game:
#     def __init__(self):
#         self.all_tiles = pygame.sprite.Group()
#         self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#         self.screen.fill(BACKGROUND)
#         self.tiles = self.initialise_tiles
#         self.draw_tiles()
#
#     def initialise_tiles(self):
#         tiles = []
#         for row in range(NUMBER_OF_ROWS):
#             row_of_tiles = []
#             for column in range(0, NUMBER_OF_COLUMNS):
#                 tile = Tile(row, column)
#                 row_of_tiles.append(tile)
#                 self.all_tiles.add(tile)
#             tiles.append(row_of_tiles)
#         return tiles
#
#     def draw_tiles(self):
#         for tile in self.all_tiles:
#             self.screen.blit(tile.surface, (tile.x_pos, tile.y_pos))
#
#             def update_tiles(self, tile_values):
#                 for row in range(0, NUMBER_OF_ROWS):
#                     for column in range(0, NUMBER_OF_COLUMNS):
#                         self.tiles[row][column].update(tile_values[row][column])
#
#             @staticmethod
#             def convert_grid(grid):
#                 tile_values = []
#                 for row in range(0, NUMBER_OF_ROWS):
#                     row_of_tiles = []
#                     for column in range(0, NUMBER_OF_COLUMNS):
#                         if grid[row][column]:
#                             row_of_tiles.append(grid[row][column].get_value())
#                         else:
#                             row_of_tiles.append(None)
#                     tile_values.append(row_of_tiles)
#                 return tile_values
#
#         def main():
#             pygame.init()
#             game = Game()
#             board = Board()
#             board.add_random_tiles(2)
#             game.update_tiles(Game.convert_grid(board.grid))
#             game.draw_tiles()
#             pygame.display.flip()
#
#             move_counter = 0
#             move = None
#             move_result = False
#             running = True
#             while running:
#                 for event in pygame.event.get():
#                     if event.type == pygame.KEYDOWN:
#                         if event.key == pygame.K_ESCAPE:
#                             running = False
#                         else:
#                             if event.type == K_UP:
#                                 move = "UP"
#                             elif event.type == K_DOWN:
#                                 move = "DOWN"
#                             elif event.type == K_LEFT:
#                                 move = "LEFT"
#                             elif event.type == K_RIGHT:
#                                 move = "RIGHT"
#                             else:
#                                 move = None
#                             if move is not None:
#                                 move_result = board.make_move(move)
#                                 if move_result:
#                                     add_tile_result = board.add_random_tiles(1)
#                                     move_counter += 1
#                                     game.update_tiles(Game.convert_grid(board.grid))
#                                     game.draw_tiles()
#                                     pygame.display.flip()
#                     elif event.type == pygame.QUIT:
#                         running = False
#
#         if __name__ == "__main__":
#             main()

# Выполнил: студент группы АГДСЭ-19 Иванов А.А.
# Лабораторная №4, вариант №31
#

# import math
# import os
#
# # процедура позволяет работать с вещественными числами
# def frange(start, stop, step):
#     i = start
#     while i < stop:
#         yield i
#         i += step

# 1. создаем значения аргумента x и функций y1 и y2 по формулам
# x = [i for i in frange(-6.0, 7.0, 1.0)]
# y1 = [(2 + math.sin(i)**2) / (1 + i * i) for i in x]
# y2 = [2 + (4 * math.cos(i)) / (1 + math.exp(i)) for i in x]
#
# # 2. корректный путь к файлу
# # вариант 1: относительный путь (файл будет рядом со скриптом)
# filename = 'data.txt'

# вариант 2: абсолютный путь под Windows (если у тебя реально есть такая папка)
# filename = r'C:\LR Python\data.txt'

# создаём папку, если используешь вариант с абсолютным путём
# os.makedirs(r'C:\LR Python', exist_ok=True)

# запись x, y1, y2
# with open(filename, 'w', encoding='utf-8') as outfile:
#     outfile.write('# значения x , y1  и y2\n')
#     for xi, y1i, y2i in zip(x, y1, y2):
#         outfile.write('%10.5f %10.5f %10.5f\n' % (xi, y1i, y2i))
#
# # 3. находим сумму функций s = y1 + y2
# result = map(lambda i1, i2: i1 + i2, y1, y2)
# y = list(result)
#
# # 4. добавление результата x и s в файл (две колонки)
# with open(filename, 'a', encoding='utf-8') as outfile:
#     outfile.write('# Результат задания x и s\n')
#     for xi, si in zip(x, y):
#         outfile.write('%10.5f %10.5f\n' % (xi, si))

# import random
# class Number:
#     def init(self, numbers=None, **kwargs):
#         if numbers is not None:
#             self.numbers = numbers
#         else:
#             size = kwargs.get('size', 10)  # По умолчанию размер 10
#             self.numbers = [random.randint(-50, 50) for _ in range(size)]
#     def process_list(self):
#         n = len(self.numbers)
#         avg = sum(self.numbers) / n
#         print(f"среднее арифметическое: {avg:.2f}")
#         if avg > 0:
#             sort_end = int(2 * n / 3)
#             print(f"среднее > 0 -> сортируем первые {sort_end} элементов")
#             self.numbers[:sort_end] = sorted(self.numbers[:sort_end])
#             self.numbers[sort_end:] = self.numbers[sort_end:][::-1]
#         else:
#             sort_end = int(n / 3)
#             print(f"среднее <= 0 -> сортируем первые {sort_end} элементов")
#             self.numbers[:sort_end] = sorted(self.numbers[:sort_end])
#             self.numbers[sort_end:] = self.numbers[sort_end:][::-1]
#         return self.numbers
#     def display(self):
#         print("список:", self.numbers)
#         print("длина списка:", len(self.numbers))
# print("задание 1")
# print("тест 1 случайные числа:")
# num_obj1 = Number(size=12)
# print("исходный список:")
# num_obj1.display()
# result1 = num_obj1.process_list()
# print("после обработки:")
# num_obj1.display()
#
#
# class Student:
#     def init(self):
#         self.grades = []
#     def menu(self):
#         while True:
#             print("\n=== ДНЕВНИК СТУДЕНТА ===")
#             print("1. Ввести 10 оценок")
#             print("2. Показать все оценки")
#             print("3. Изменить оценку")
#             print("4. Проверить стипендию")
#             print("5. Сортировать оценки")
#             print("0. Выход")
#             choice = input("Ваш выбор: ")
#             if choice == '1':
#                 self.input_grades()
#             elif choice == '2':
#                 self.show_grades()
#             elif choice == '3':
#                 self.change_grade()
#             elif choice == '4':
#                 self.check_scholarship()
#             elif choice == '5':
#                 self.sort_grades()
#             elif choice == '0':
#                 print("Выход!")
#                 break
#     def input_grades(self):
#         self.grades = []
#         for i in range(10):
#             grade = int(input(f"Оценка {i + 1}: "))
#             if 1 <= grade <= 12:
#                 self.grades.append(grade)
#             else:
#                 print("Ошибка! Оценка 1-12")
#                 return
#     def show_grades(self):
#         if self.grades:
#             for i, g in enumerate(self.grades, 1):
#                 print(f"{i}. {g}")
#         else:
#             print("Нет оценок!")
#     def change_grade(self):
#         if not self.grades:
#             print("Сначала введите оценки!")
#             return
#         self.show_grades()
#         num = int(input("Какую оценку изменить? ")) - 1
#         new_grade = int(input("Новая оценка: "))
#         if 0 <= num < len(self.grades) and 1 <= new_grade <= 12:
#             self.grades[num] = new_grade
#             print("Изменено!")
#     def check_scholarship(self):
#         if not self.grades:
#             print("Нет оценок!")
#             return
#         avg = sum(self.grades) / len(self.grades)
#         print(f"Средний балл: {avg:.2f}")
#         print("Стипендия: ДА" if avg >= 10.7 else "Стипендия: НЕТ")
#     def sort_grades(self):
#         if not self.grades:
#             print("Нет оценок!")
#             return
#         choice = input("Сортировать по возрастанию (1) или убыванию (2)? ")
#         if choice == '1':
#             print(sorted(self.grades))
#         elif choice == '2':
#             print(sorted(self.grades, reverse=True))
# student = Student()
# student.menu()
#
#
# numbers = [5, 2, 8, 1, 9, 3]
# print("Исходный список:", numbers)
# n = len(numbers)
# for i in range(n - 1):
#     swaps = 0
#     for j in range(n - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#             swaps += 1
#     print(f"Проход {i + 1}: {numbers}, перестановок: {swaps}")
#     if swaps == 0:
#         print("Сортировка завершена!")
#         break
# print("Результат:", numbers)


# def phone_directory():
#     codes = [111234,234567,456345,18769,141141]
#     phones = [791925334,78172833,74553732,79123433,7141141]
#     while True:
#         print("1 отсортировать по идентификационным кодам")
#         print("2 отсортировать по номерам телефона")
#         print("3 вывести список с кодами и телефонами")
#         print("4 выход")
#         choice = input("выберите пункт меню:")
#         if choice == '1':
#             if codes and phones:
#                 combined = sorted(zip(codes, phones), key=lambda x: x[0])
#                 codes[:], phones[:] = zip(*combined)
#                 print("список отсортирован по идентификационным кодам")
#             else:
#                 print("списки пусты")
#         elif choice == '2':
#             if codes and phones:
#                 combined = sorted(zip(codes, phones), key=lambda x: x[1])
#                 codes[:], phones[:] = zip(*combined)
#                 print("список отсортирован по номерам телефона")
#             else:
#                 print("списки пусты")
#         elif choice == '3':
#             if codes and phones:
#                 print("\nсписок пользователей:")
#                 print("код\tтелефон")
#                 for code, phone in zip(codes, phones):
#                     print(f"{code}\t{phone}")
#             else:
#                 print("списки пусты, добавьте данные")
#         elif choice == '4':
#             print("выход")
#             break
#         else:
#             print("ошибка")
#
# phone_directory()
# def books_catalog():
#     titles = []
#     years = []
#     while True:
#         print("1 отсортировать по названию книг")
#         print("2 отсортировать по годам выпуска")
#         print("3 вывести список книг с названиями и годами выпуска")
#         print("4 добавить книгу")
#         print("5 выход")
#         choice = input("выбери пункт меню:")
#         if choice == '1':
#             if titles and years:
#                 combined = sorted(zip(titles, years), key=lambda x: x[0])
#                 titles[:], years[:] = zip(*combined)
#                 print("список отсортирован по названиям книг")
#             else:
#                 print("каталог пуст")
#         elif choice == '2':
#             if titles and years:
#                 combined = sorted(zip(titles, years), key=lambda x: x[1])
#                 titles[:], years[:] = zip(*combined)
#                 print("список отсортирован по годам выпуска")
#             else:
#                 print("каталог пуст")
#         elif choice == '3':
#             if titles and years:
#                 print("\nкаталог книг:")
#                 print("название\tгод выпуска")
#                 for title, year in zip(titles, years):
#                     print(f"{title}\t{year}")
#             else:
#                 print("каталог пуст, добавь книги")
#         elif choice == '4':
#             title = input("введи название книги:")
#             try:
#                 year = int(input("введи год выпуска: "))
#                 titles.append(title)
#                 years.append(year)
#                 print(f"книга '{title}' добавлена в каталог")
#             except ValueError:
#                 print("год должен быть числом")
#         elif choice == '5':
#             print("выход из программы")
#             break
#         else:
#             print("ошибка")
# books_catalog()

def linearsearch(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1
def xz():
    list1 = [5,2,8,1,9]
    list2 = [4,7,2,6,4]
    list3 = [10,15,12,11]
    list4 = [22,18,16,14,13]
    print("список 1:", list1)
    print("список 2:", list2)
    print("список 3:", list3)
    print("список 4:", list4)
    combined_list = list1 + list2 + list3 + list4
    print("\nобъединенный список:", combined_list)
    while True:
        order = input("\nвыберите сортировку 1 по возрастанию, 2 по убыванию: ")
        if order in ['1', '2']:
            break
        print("выберете 1 или 2")
    if order == '1':
        combined_list.sort()
        print("отсортировано по возрастанию:", combined_list)
    else:
        combined_list.sort(reverse=True)
        print("отсортировано по убыванию:", combined_list)
    try:
        search_value = int(input("\nвведите значение для поиска: "))
        index = linearsearch(combined_list, search_value)
        if index != -1:
            print(f"значение {search_value} найдено на позиции {index + 1}")
        else:
            print(f"значение {search_value} не найдено в списке")
    except ValueError:
        print("ошибка")
xz()


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
def get_unique_elements(*lists):
    all_elements = []
    for lst in lists:
        all_elements.extend(lst)
    unique_elements = []
    for element in all_elements:
        if all_elements.count(element) == 1:
            unique_elements.append(element)
    return unique_elements
def xz2():
    list1 = [5, 2, 8, 1, 9, 100]
    list2 = [3, 7, 2, 6, 4, 100]
    list3 = [10, 15, 12, 11, 200]
    list4 = [20, 18, 16, 14, 13, 300]
    print("список 1:", list1)
    print("список 2:", list2)
    print("список 3:", list3)
    print("список 4:", list4)
    unique_list = get_unique_elements(list1, list2, list3, list4)
    print("\nуникальные элементы:", unique_list)
    if not unique_list:
        print("нет уникальных элементов")
        return
    while True:
        order = input("\nвыберите сортировку 1 по возрастанию, 2 по убыванию: ")
        if order in ['1', '2']:
            break
        print("введите 1 или 2")
    if order == '1':
        unique_list.sort()
        print("отсортировано по возрастанию:", unique_list)
    else:
        unique_list.sort(reverse=True)
        print("отсортировано по убыванию:", unique_list)
    try:
        search_value = int(input("\nвведите значение для поиска: "))
        search_list = unique_list.copy()
        if order == '2':
            search_list.sort()
        index = binary_search(search_list, search_value)
        if index != -1:
            if order == '1':
                actual_index = index
            else:
                actual_index = len(unique_list) - 1 - index
            print(f"значение {search_value} найдено на позиции {actual_index + 1}")
            print(f"список: {unique_list}")
        else:
            print(f"значение {search_value} не найдено")
    except ValueError:
        print("ошибка")
xz2()