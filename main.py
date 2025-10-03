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

#задание 1
n = int(input("введите число: "))
for i in range(1, 11):
    result = n * i
    print(f"{n} * {i} = {result}")
#задание 2
def main():
    exchange_rates = {
        'USD': 1.0,
        'EUR': 0.85,
        'GBP': 0.73,
        'JPY': 110.0,
        'RUB': 75.0
    }
    while True:
        print("конвертер волют")
        print("1) конвертировать валюту")
        print("2) показать доступные валюты")
        print("3) выйти из программы")
        choice = input("выберите пункт меню 1-3: ")
        if choice == '1':
            convert_currency(exchange_rates)
        elif choice == '2':
            show_currencies(exchange_rates)
        elif choice == '3':
            print("до свидания")
            break
        else:
            print("ошибка, выберете 1,2,3")
def convert_currency(rates):
    print("\nконвертация валюты")
    print("доступные валюты:", ", ".join(rates.keys()))
    from_currency = input("из какой валюты конвертировать например, USD: ").upper()
    to_currency = input("в какую валюту конвертировать например, EUR: ").upper()
    if from_currency not in rates or to_currency not in rates:
        print("ошибка: неизвестная валюта")
        return
    try:
        amount = float(input(f"сумма в {from_currency}: "))
        if amount <= 0:
            print("сумма должна быть положительной")
            return
    except ValueError:
        print("ошибка: введите корректное число")
        return
    amount_in_usd = amount / rates[from_currency]
    result = amount_in_usd * rates[to_currency]
    print(f"\nрезультат конвертации:")
    print(f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}")
def show_currencies(rates):
    print("\nдоступные валюты")
    for currency, rate in rates.items():
        print(f"{currency}: 1 USD = {rate} {currency}")
if __name__ == "__main__":
    main()

#задание 3
print("введите границы диапазона:")
start = int(input("начало: "))
end = int(input("конец: "))
if start > end:
    start, end = end, start
while True:
    number = int(input(f"введите число от {start} до {end}: "))
    if start <= number <= end:
        break
    print("число вне диапазона! Попробуйте снова.")
print(f"\nчисла диапазона {start}-{end}:")
for i in range(start, end + 1):
    if i == number:
        print(f"!{i}!", end=" ")
    else:
        print(f"{i}", end=" ")
print("\n")

#задание 4
import random
print("угадай число от 1 до 500")
secret = random.randint(1, 500)
popitka = 0
while True:
    try:
        user_guess = int(input("твое число: "))
        popitka += 1
        if user_guess < secret:
            print("больше")
        elif user_guess > secret:
            print("меньше")
        else:
            print(f"правильно {secret}")
            print(f"ты угадал за {popitka} попыток")
            break
    except:
        print("вводи только числа")