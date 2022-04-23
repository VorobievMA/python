#for i in range(10):
    #print(i)

# my_sting = 'Hello, world'
# for i in range(len(my_sting)):
#     print(my_sting[i])

# for i in range(5, 10, 2): # с, по, шаг.
#     print(i)
# for i in range(20, 10, -2): # с, по, шаг.
#     print(i)

#my_sting = 'Hello, world'
 # for char in my_sting:
 #    print(char)

# for char in range(0, len(my_sting), 2):
#     print(my_sting[char])

# n=10
# while n >= 1:
#     if n == 5:
#         print("n=5")
#         continue
#     print(n)
#     n -= 1
# else:
#     print('else')

# if n != 1:
#     pass
# else:
#     pass
# flag = True
# while flag:
#     number = input("vvedi:")
#     if not number:
#         continue
#     if not number.isdigit():
#         continue
#     if int(number) == 7:
#         print("viigrl")
#         break

############### Списки

# my_list = []
# my_list = list()
# print(my_list)
# my_list = [1, 2, 3, 4]
# print(my_list)
#
# my_list = [1, str, 3.7, 4.0, 5]
# print(my_list)
#
# my_list = [(1, 2, 3,), ("1", 2, 3), (3.7, 4.0,)]
# print(my_list)
#
# my_list = ["h", "l", "l", "o"]
# print(my_list[0])
# print(my_list[2])
# print(my_list[-1])
#
# my_list = [(1, 2, 3,), ("1", 2, 3), (3.7, 4.0,)]
# print(my_list[0][1])
# print(my_list[-1][1])

# my_list = ["H", "e", "l", "l", "o", "W", "o", "r", "l", "d",]
# print(my_list[1:7])
# print(my_list[0:])
# print(my_list[:8])
# print(my_list[:])
# print(my_list[-5:-2])

# изменение
# my_list = [1, 2, 3, 4, 5]
# print(my_list)
# my_list[0] = 0
# my_list[3] = 0
# my_list[-1] = 0
# print(my_list)
# my_list[1] = [1, 2, 8]
# print(my_list)
# my_list[1:1] = [1, 2, 8]
# print(my_list)
# my_list[1:2] = [1, 2, 8]
# print(my_list)
# my_list = [1, 2, 3] + [4, 5]
# print(my_list)

# Методы списков
# my_list = [1, 3, 5]
# print(my_list)
# my_list.append(7)
# print(my_list)
# my_list.extend([9, 11, 13])
# print(my_list)
# my_list.insert(0, 0)
# print(my_list)
# my_list.insert(-1, 15)


# my_list = [1, 3, 3, 5]
# print(my_list)
# temp = my_list.remove(3)
# print(temp)
# print(my_list)
# my_list.pop(0)
# print(my_list)

# my_list = [1, 2, 3, 3, 3, 4, 5, 6, 7]
# for i in range(3):
#     my_list.remove(3)
#     print(my_list)
# my_list.insert(2, 3)
# print(my_list)

# my_list = [1, 2, 3, 3, 3, 4, 5, 6, 7]
# for i in range(2):
#     my_list.remove(3)
# print(my_list)
# my_list = [1, 2, 3, 3, 3, 4, 5, 6, 7]
# n = 3
# for number in my_list:
#     if number == n:
#         #my_list.remove(n)
#         my_list.pop(number)
# print(my_list)
# print(n in my_list)
# my_list = [1, 2, 3, 3, 3, 4, 5, 6, 7]
# n = 3
# flag = True
# while flag:
#     if n in my_list:
#         my_list.remove(n)
#         continue
#     flag = False
# print(my_list)
# print(n in my_list)

# my_list = [1, 2, 3, 3, 3, 4, 5, 6, 6, 7]
# print(my_list)
# my_list.clear()
# print(my_list)
# my_list = [1, 2, 3, 3, 3, 4, 5, 6, 6, 7]
# print(my_list.count(4))
# print(my_list.count(6))
# print(my_list.index(4))
# print(my_list.index(7))
# print(my_list.index(3))

# my_list = [99, 0, 25, 4]
# my_list.sort()
# print(my_list)
# my_list = [99, 0, 25, 4]
# new_list = sorted(my_list, reverse=False)
# print(my_list)
# print(new_list)
#
# nams = ['', '!', 'jasika', 'ban', 'wendy']
# print(nams)
# nams.sort(key=len)
# print(nams)

# nams = ['', '!', 'jasika', 'ban', 'wendy']
# slice = nams[0::2]
# print(slice)
#
# numbers = [1, 2, 3, 4, 5, 6, 7]
# print(numbers[::2])
# print(numbers[:0:-2])

# Кортежи
# my_tuple = ()
# my_tuple = tuple()
# my_tuple = (1, "str", 3.9, 4, 5)
# print(my_tuple)
# my_tuple = 1, "str", 3.9, 4, 5
# print(my_tuple)
#
# my_tuple = 'str'
# print(type(my_tuple))
#
# my_tuple = 1, ["str", 3.9], 4, 5
# print(my_tuple)
#
# my_tuple = 1, "str", 3.9, 4, 5
# print(my_tuple.index(4))
# my_tuple = 1, "str", 3.9, 4, 5
# print(my_tuple.count("str"))
#
# my_tuple = 1, 2, 3
# a, b, c = my_tuple
# print(a, b, c)

# numbers = [-20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for i in range(13):
#     a = numbers[i]
#     print(a, "-", a*9/5+32)

# print("c", "F")
# for temp in range(0,110,10):
#     print({temp}, {temp*1.8+32})

# voz_grupp = [1, 9, 7, 15, 23, 37, 69]
# summ = 0.0
# for i in range(7):
#     a = voz_grupp[i]
#     if a <= 2:
#         summ = summ + 0
#              else 2 < a <= 12:
#             summ = summ + 14.00
#                  else if 12 < a <= 65:

# ages = []
# while True:
#     age = input("vozrast  ")
#     if age:
#         ages.append(age)
#         continue
#     sum = 0
#     for a in ages:
#         a = int(a)
#         if a <= 2:
#             sum += 0
#         elif 3 <= a <= 12:
#             sum += 14
#         elif a >= 65:
#             sum += 18
#         else:
#             sum += 23
#     ages.clear
#     print(sum)

# set множества
# my_list = [1, 2, 3]
# my_set = {1, 2, 3}
# my_set = {1, 2, 2, 3, 4, 'str', (6, 7, 8), (6, 7, 8)}
# print(my_set)
# my_list_1 = [1, 2, 3]
# my_list_2 = [3, 2, 1]
# print(set(my_list_1) == set(my_list_2))
# my_set = {1, 2, 2, 3, 4, 'str', (6, 7, 8), (6, 7, 8)}
# # изменение множеств
# my_set = {1, 2, 2, 3, 4, 5}
# print(my_set)
# my_set.add(6)
# print(my_set)
# my_set.update(['str', 'helli', 8, 9, 9, 0])
# print(my_set)
#
# my_set = set('Hello, world')
# print(my_set)
# my_set.pop()
# print(my_set)
#
# my_set = set('Hello, world')
# print(my_set)
# my_set.remove("e")
# print(my_set)
# my_set = set('Hello, world')
# print(my_set)
# my_set.discard(1)
# print(my_set)
# my_set.clear()
# print(my_set)
#
# my_set = {1, 2, 3, 4, 5, 6}
# for elem in my_set:
#     print(elem)
#     if elem == 2:
#         print("two")
#         continue
#
# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}
# # объединение union
# print(a | b)
# print(a.union(b))
#
# #intersectioon
# print(a & b)
# print(a.intersection(b))
#
# # differnce
# print(a - b)
# print(a.difference(b))
#
# # symetric difeerence
# print(a ^ b)
# print(a.symmetric_difference(b))
#
# print()
# print(a <= b)
# print(a.issubset(b))
# print()
# print(a >= b)
# print(a.issuperset(b))
# print()
# print(a.isdisjoint(b))

# словари dict
# key: value
# mydict = {}
# mydict = dict()
# mydict = {
#     "name": "bob",
#     "job": "dev",
#     "age": 40,
#     1: 1,
#     (0, 0, 0): False,
#     }
# print(mydict['age'])
# print(mydict[(0, 0, 0)])
# mydict = dict([(1, "bob"), (2, "dev"), (3, '3')])
# print(mydict[2])
# mydict = dict(name='Bane', job="dev", age=40)
# print(mydict["age"])
# mydict = {
#     "name": "bob",
#     "job": "dev",
#     "age": 40,
#     "children": ["jim", "jo", "jane"]
#     }
# print(mydict[["children"][0]])
# print(mydict.get("name"))
# # методы словарей
# square = {1: 1, 2: 4, 3: 9, 4: 16}
# square.update({5: 25, 6: 36}) # дополнение
# print(square)
# square.update({6: 0})
# print(square)
# # удаление
# print(square.pop(6))
# print(square.pop(9, 81))
# print(square.popitem())
# #square.clear()
# print(square)
#
# print(square.keys())
# print(square.values())
# print(square.items())
#
# print(4 in square)
# print( 4 not in square.values())
# print(3 in square.items())
# for x, y in square.items():
#     print(f'{x} {y}')
# list_1 = [1, 2, 3]
# list_2 = [3, 2, 1]
# for x, y in zip(list_1, list_2):
#     print(x, y)

# упр 25
# nums = []
# flag = True
# while flag:
#     #num = int(input("vvedi chislo"))
#     if num == 0 and not nums:
#         print("noll")
#         continue
#     if num == 0:
#         # result = 0
#         # for nm in nums:
#         #     result +=nm
#         print(sum(nums)/len(nums))
#         nums.clear()
#     nums.append(num)


# nums_1 = input("vvedi xhtrez probel")
# nums = nums_1.split(' ')# сепаратор
# print(nums_1)
# print(nums)

# for i in range(1, 100, 1):
#     if i % 2:
#         print(i, "Fizz")
#     elif i % 3:
#         print(i, "Buzz")
#     elif i // 2 and i // 3:
#         print(i, "Fizz and Buzz")
#     elif i % 2 and i % 3:
#         print("not")

# 30
# for i in range(1, 100):
#     if (i % 3 == 0) and i % 5 == 0:
#         print("Fizz Buzz")
#     if (i % 3 == 0):
#         print("Fizz")
#         continue
#     if i % 5 == 0:
#         print("Buzz")
#     print(i)
# функции
# def hello_world():
#     '''
#      vivdvod
#     :return:
#     '''
#     print("Hello world")
# #   return None
#
#
# print(hello_world.__doc__)

# def greet(*name):
#     for name in names:
#         print(f"Hello {name}!")
#
#
# greet('Jon')
#
# names = {"j", "b", "el"}
# # for name in names:
# #     greet(name)
#
# greet(*names)

# def speak(name, phrase):
# #     print(f"Hello{name}")
# #     print(f'{phrase}')
# #
# #
# # speak('bay', 'bob')
# # speak(name='jon', phrase="hello, world")


# def speak(name, phrase):
#     return f"Hellow, {name}!\n {phrase}"
#
# print(speak('jon', 'im dev'))

# def args(*args):
#     print(args)
#     print(type(args))
#
#
# args(1, 2, 3, "Helo", (1, 3, 5))
#
# def kwargs(**rwargs):
#     print(kwargs)
#     print(type(kwargs))
#
# kwar = {'key_1': "value_1", 'key_2': 'value_2'}
# kwargs(a='1', b='2', c='3')
# kwargs(**kwar)


# def calc(first, second, operator):
#     try:
#         if operator == "+":
#             return first+second
#         if operator == "-":
#             return first-second
#         if operator == "*":
#             return first * second
#         if operator == "/":
#             return first / second
#     except ZeroDivisionError as error:
#         print(error)
#     except Exception as e:
#         print(e)
#
# while True:
#     first, second, operator = input("vvedi dva chisla").split(" ")
#     result = calc(int(first), int(second), operator)
#     print(result)

#upr 35

# def rast(x):
#     a = 4
#     b = 0.25
#     price = a + ((x * 1000)/140) * b
#     print(price)
#
#
# rast(1)

# def taxi(km):
#     base = 4
#     evry_140m = 0.25
#     m = (km * 1000) / 140
#     return base + int(m) * evry_140m
#
#
# print(taxi(0.5))

# upr 36

# def price(numder_goods):
#     if numder_goods <= 0:
#         return
#     if numder_goods == 1:
#         return 10.95
#     return 10.95 + 2.95 * (numder_goods - 1)
#
# print(price(1))
# from copy import copy, deepcopy
# my_list_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(my_list_1)
# my_list_2 = copy(my_list_1) # поверхостная копия первй элемент
# my_list_2 = deepcopy(my_list_1)# полная копия
# print(my_list_2)
# my_list_1[0][0] = 'AA'
# my_list_1[0] = 'BB'
# print(my_list_1)
# print(my_list_2)

# import copy
# from copy import copy

# def sq(num: int):
#     pow = []
#     for x in range(num):
#         pow.append(x ** 2)
#     return pow
#
#
# print(sq(10))
# # Списковые включения и генераторы списков
# result = [x ** 2 for x in range(10)] # генераторы
# print(result)
# pow_dict = {x: x ** 2 for x in range(10)}
# print(pow_dict)
#
# tuple_sq = result = (x ** 2 for x in range(10) if x % 2 == 0)
# print(tuple_sq)
#
# for number in tuple_sq:
#     print(number)

# def infinit():
#     num = 0
#     while True:
#         if num == 100:
#             break
#         yield num
#         num += 1
#
# for i in infinit():
#     print(i)

# def calc(a, b):
#     yield a + b
#     yield a - b
#     yield a * b
#     yield a / b
#
# print(list(calc(3, 6)))
# for i in calc(3, 6):
#     print(i)

# def prch(x):
#     if x >= 1:
#         pass
#     else:
#         print("PNH")
#     if x % 3:
#         pass
#     else:
#         print("False")
#     if x % 2:
#         pass
#     else:
#         print("False")
#     if x % x:
#         pass
#     else:
#         print("True")
#
# prch(10)

#генераоры
# from random import randint
#
# def ip_gen():
#     for _ in range(10):
#         a = randint(0, 255)
#         b = randint(0, 255)
#         c = randint(0, 255)
#         d = randint(0, 255)
#         ip = f'{a}. {b}. {c}. {d}'
#         yield ip
#
# for index, l in enumerate(ip_gen(), start=1):
#     print (index, l)
#
# def get_next_num():
#     n = 2
#     while True:
#         yield n
#         n *= 2
#
# for num in get_next_num():
#     if num > 256:
#         break
#     print(num)
#
# # включения
# pow =[]
# for x in range(10):
#     pow.append(x ** 2)
# print(pow)
#
# pow_list = [x ** 2 for x in range(10)]
# print(pow_list)
#
# pow_list = [x ** 2 for x in pow]
# print(pow_list)
#
# pow_list = [x ** 2 for x in range(10) if x % 2 == 0]
# print(pow_list)
#
#
# pow_dict = [{x: x ** 2} for x in range(10)]
# print(pow_dict)

# tuple_list = ( x ** 2 for x in range(10))
# print(tuple_list)
# for i in tuple_list:
#     print(i)
#
# tuple_list = tuple(x ** 2 for x in range(10) if x % 2 == 0)
# print(tuple_list)
#
# set_list = {x // 2 for x in range(10)}
# print(set_list)
#
# dict_list = {x: {x: x // 2} for x in range(10)}
# print(dict_list)

#файлы и работа с ними

# file = open('text.txt', 'r')
# print(file.read())
# file.close()
# print("*" * 90)
# file = open("text.txt", 'r')
# for line in file:
#     print(line, end="")
# file.close()

#менеджер контекста with ...as
# with open('text.txt', 'r') as file:
#     for line in file:
#         print(line, end="")

# file = open('text.txt', 'r')
# print(file.read(16))
# file.close()

# with open('text.txt', "r") as file:
#     first_part = file.read(16)
#     print(first_part)
#     file.seek(4)
#     second_part = file.read(16)
#     print(second_part)
#
# with open('text.txt', 'r') as f:
#     for line in f.readline():
#         print(line)

# запись в файл
# file = open("example.txt", "w")
# fiel.write('Hello, world\n')
# file.close()
#
# nums = [x * x for x in range(10)]
#
# for num in nums:

# txt = []
# with open('text.txt', 'r') as file:
#     for line in file:
#         txt.append(line)
# print(txt)
# with open('example.txt', 'w') as file:
#     for line in txt:
#         file.write(line)
#
# with open('example.txt', 'a') as file:
#     file.write("\n\n\n")
#     file.writelines(txt)
#
# with open('example_print.txt', 'w') as file:
#     for line in txt:
#         print(line, file=file)

# работа с файлами
# import os
# print(f'текущая директория {os.getcwd()}')# вызоа текущей папки
# os.mkdir('tmp_folder\\1') #создание папки
# os.makedirs(r'temp_folder\tmp_level_1\tmp_level_2')
# os.rmdir(r'temp_folder\tmp_level_1\tmp_level_2') # удаление папок
# os.rmdir(r'temp_folder\tmp_level_1')
# import os.path

# file = open('tmp.txt', 'w')
# file.write('Hello world')
# file.close()
# print(f'est li fail{os.path.exists("tmp.txt")}')
# os.remove('tmp.txt')
# print(f'est li fail{os.path.exists("tmp.txt")}')

# os.mkdir('temp')
# print(os.path.isdir('temp'))
# print(os.path.isfile('temp'))
# print(os.path.exists('temp'))
# os.rmdir('temp')
# print(os.path.exists('temp'))

# from pathlib import Path #нужно для копирования и тд
# .txt
# txt_files = list(Path('.').glob('*.txt'))
# print(txt_files)
# for file in txt_files:
#     print(file.absolute())
# print("-" * 90)
# # glob
# from glob import glob
# files = glob('e*_print*')
# print(f'vse na e: {files}')

# перемещение
# target_folder = Path('target_folder')
# target_folder.mkdir(exist_ok=True)
# source_path = Path('.')
# txt_files = source_path.glob("*.txt")
# for txt_files in txt_files:
#     filename = txt_files.name
#     target_path = target_folder.joinpath(filename)
#     print(f'ptrtnosim fail {filename}')
#     print(target_path.exists())
#     txt_files.rename(target_path)
#     print(target_path.exists())

# копирование файлов
# from shutil import copy
# source_file = 'target_folder/Hello.txt'
# target_file = 'Hello2.txt'
# target_file_path = Path(target_file)
# copy(source_file, target_file)

# получение инфы о файле

# for py_file in Path('.').glob("*.py"):
#     print(f'имя с расiирением {py_file}')
#     print(f'tолько имя {py_file.stem}')
#     print(f'только расширение {py_file.suffix}')
#
# from datetime import datetime, timedelta
#
# current_file_path = Path('main.py')
# file_stat = current_file_path.stat()
# print(f'размер файла в байтах {file_stat.st_size}')
# print(f'Время последнего обращения {datetime.fromtimestamp(file_stat.st_atime)}')
# print(f"Время последнего изменения {datetime.fromtimestamp(file_stat.st_mtime)}")
# print(f'разница ежду временами', end='')
# print(timedelta.fromtimestamp(file_stat.st_atime))

# Архивирование и разархивирование файлов .zip
# from zipfile import ZipFile
# with ZipFile('txt_file.zip', 'w')as zfile:
#     for txt_file in Path("target_folder").glob("*txt"):
#         print(f'dob v arhiv {txt_file}')
#         zfile.write(txt_file)
#
# os.mkdir('extract_folder')
# with ZipFile('txt_file.zip') as zfile:
#     zfile.printdir()
#     zfile.extractall(path='extract_folder')

# csv- comon separted value
# name , surname, age
# roman, putanov, 20
# jon, jons, 40
# jane, joe, 22
# import csv
# with open('csv.csv') as file:
#     reader = csv.reader(file, delimiter="'")
#     for row in reader:
#         print(row)
#
# with open('csv.csv', 'a') as file:
#     writer = csv.writer(file)
#     writer.writerow(['garry, 48, boss, 1b'])

# class i oop
# my_list = [1, 2, 3]
# class Test:
#     pass
#
# test = Test()
# print(test)
# test.name = 'jon'
# print(test.name)

# class Employee:
#     all_employes = []
#     name = 'Employee'
#     drive = False
#
#     def __init__(self, name, age, position, place):
#         self.name = name
#         self.age = age
#         self.position = position
#         self.place = place
#
#         Employee.all_employes.append(self)
#         # self.__class__.all_employes.append(self)
#
#
# jane = Employee('Jane', 35, 'manager', '1a')
# jon = Employee("Jon", 40, "dev", "2a")
# bob = Employee('Bob', 25, "QA", "3a")
# sam = Employee(name='sam', age=28, position='dev', place='4a')
#
# for atr in jon, jane, bob:
#     print(atr.place)
#
# print(len(Employee.all_employes))
# for emp in Employee.all_employes:
#     print(emp.name)
#
# sam.drive = True
# print(sam.drive)
# print(Employee.name)
# print(sam.__class__.name)

# class Circle:
#     '''Класс круг'''
#     all_circle = []
#     pi = 3.14
#
#     def __init__(self, r=1):
#         self.radius = r
#         self.__class__.all_circle.append(self)
#
#     def area(self):
#         return self.__class__.pi * self.radius * self.radius
#
#     @classmethod
#     def total_area(cls):
#         '''Метод для вычисления площади всех кругов'''
#         total = 0
#         # self.__class__.all_circle
#         for c in cls.all_circle:
#             total += c.area()
#         return total
#     # @staticmethod
#     # def total_area():
#     #     '''Метод для вычисления площади всех кругов'''
#     #     total = 0
#     #     #self.__class__.all_circle
#     #     for c in Circle.all_circle:
#     #         total +=c.area()
#     #     return total
#
#
# circle_1 = Circle(3)
# circle_2 = Circle()
# circle_3 = Circle(2)
# print(circle_1.area())
# print(circle_2.area())
# print(circle_3.area())
#
# cr1 = circle_1.area()
# cr2 = circle_2.area()
# cr3 = circle_3.area()
# print(cr1 + cr2 +cr3)
# print(Circle.total_area())
# инкапсуляция
# class Character:
#     def __init__(self, name, health=100):
#         self.name = name
#         self.__health = health
#
#     @property # геттер
#     def health(self):
#         return self.__health
#
#     @health.setter #суттер
#     def health(self, new_value):
#         if new_value >= 200 or new_value <= 0:
#             raise Exception('znachnie zdorovia >200')
#         self.__health = new_value
#
#
#     # def show_health(self):
#     #     return  self.__health
#     #
#     # def new_health(self, other):
#     #     self.__health = other
#
# knight = Character('knight', 150)
# print(knight.health)
# knight.health = 199
# print(knight.health)
# # print(knight.show_health())
# # knight.__health = 1
# # print(knight.show_health())
# # print(knight.health)

#полиморфизм

# class Dog:
#     def __init__(self, name, phrase):
#         self.name = name
#         self.phrase = phrase
#
#     def say(self):
#         print(self.phrase)
#
# class Cat:
#     def __init__(self, name, phrase):
#         self.name = name
#         self.phrase = phrase
#
#     def say(self):
#         print("miau")
#
# class Cow:
#     def __init__(self, name, phrase):
#         self.name = name
#         self.phrase = phrase
#
#     def say(self):
#         print("Mumu")
#
# cow = Cow('Mila', "mu")
# cat = Cat('vasia', '123')
# dog= Dog('yanus', "gav")
#
# cow.say()
# cat.say()
# dog.say()
#
# for x in cow, cat, dog:
#     x.say()

# class Perrot:
#     def Fly(self):
#         print('popugai letaet')
#
#     def swin(self):
#         print("popugai ne plavaet")
#
#
# class Puingwin:
#     def Fly(self):
#         print('popugai ne letaet')
#
#     def swin(self):
#         print("popugai plavaet")
#
# def fly_test(bird):
#     bird.fly()
#
# parrot = Perrot()
# puingwin = Puingwin()


# Наследование
# from random import randint
# class Character:
#     def __init__(self, name, health=100):
#         self.name = name
#         self.__health = health
#
#     @property # геттер
#     def health(self):
#         return self.__health
#
#     @health.setter #суттер
#     def health(self, new_value):
#         if new_value >= 200:
#             raise Exception('znachnie zdorovia >200')
#         self.__health = new_value
#
#     @staticmethod
#     def attack():
#         print('eto metod v dochernem classe')
#
# class Enemy(Character):
#     def __init__(self, name, damage):
#         super().__init__(name)
#         self.damage = damage
#
#     def attack(self):
#         return randint(0, self.damage)
#
# class Kight(Character):
#     def __init__(self, name, damage):
#         super().__init__(name)
#         self.damage = damage
#
#     def attack(self):
#         return randint(0, self.damage)
#
#
# char = Character('character', 2)
# knight = Kight('Artur', 25)
# knight.health = 199
# print(char.name)
# print(knight.name)
# print(knight.health)
# print(knight.attack())
#
# gost = Enemy('gost', 10)
#
# while True:
#     dmg = int(input("ddtlb ehjy"))
#     knight.damage = dmg
#     print(f"delai udar {gost.name}")
#     dmg = knight.attack()
#     gost.health -= dmg
#     print(f"vi nanesli {knight.damage}")
#     print(f"uvraga {gost.name} ostalos {gost.health}")
#     if gost.health <= 0:
#         print("vin")
#         break

# class Vehicle:
#     def __init__(self):
#         self.name = name
#         self.wheels = wheels
#
#     def wheels(self):
#         return self.wheels
#
#     def ping(self):
#         print("v doxh classe")
#
#
# class Car(Vehicle):
#     def __init__(self):
#         self.name = name
#         self.wheels = wheels
#         self.color = color



# car = Car(name="Tiguan", wheels=4, color="black")
# car.ping()

# множественное наследование
# class Boat:
#     def swim(self):
#         print("hod")
#
# class Car:
#     def drive(self):
#         print("ezda")
#
# class Amfib(Car, Boat):
#     def go(self):
#         print(" i to i to")
#
#
# aaph = Amfib()
# aaph.swim()
# aaph.drive()
# aaph.go()
# print(type(aaph))
# print(isinstance(aaph, Car))

# dandermethod

# class Number:
#     def __init__(self, value):
#         self.value = value
#     @staticmethod
#     def to_string():
#     def update(self,index,  other):
#         number_list =[ x for x in str(self.value)]
#         number_list(index) = other
#         print(numbet_list)
#
#     def __str__(self):
#         return str(self.value)
#
#
#     def __repr__(self):
#         return f'Number({self.value})'
#
#
# number = Number(4567)
# print(number)

# import functools
#
#
# class Number:
#     def __init__(self, value):
#         self.value = value
#         print(type(self.value))
#
#     @staticmethod
#     def to_string(first_number, second_number):
#         return str(first_number) + str(second_number)
#
#     def update(self, index, other):
#         number_list = [x for x in str(self.value)]
#         number_list[index] = other
#         result = functools.reduce(Number.to_string, number_list)
#         self.value = int(result)
#
#     def __str__(self):
#         return str(self.value)
#
#     def __repr__(self):
#         return f'Number({self.value})'
#
#     def __eq__(self, other):
#         # Определяет поведение оператора ==
#         if isinstance(other, Number):
#             return self.value == other.value
#         if isinstance(other, int):
#             return self.value == other
#         raise TypeError('Тип данных не поддерживается')
#
#     def __lt__(self, other):
#         # Определяет поведение оператора <
#         if isinstance(other, Number):
#             return self.value < other.value
#         if isinstance(other, int):
#             return self.value < other
#         raise TypeError('Тип данных не поддерживается')
#
#     def __gt__(self, other):
#         # Определяет поведение оператора >
#         if isinstance(other, Number):
#             return self.value > other.value
#         if isinstance(other, int):
#             return self.value > other
#         raise TypeError('Тип данных не поддерживается')
#
#
#     def __le__(self, other):
#         # Отделяет поведение метода <=
#         if isinstance(other, Number):
#             return self.value <= other.value
#         if isinstance(other, int):
#             return self.value <= other
#         raise TypeError('Тип данных не поддерживается')
#
#
#     def __ge__(self, other):
#         # Определяет поведение метода >=
#         if isinstance(other, Number):
#             return self.value >= other.value
#         if isinstance(other, int):
#             return self.value >= other
#         raise TypeError('Тип данных не поддерживается')
#
# number_1 = Number(4586)
# number_2 = Number(4895)
#
# print(number_1 >= number_2)
# print(number_1)
# print(number_1 == number_2)
# print(number_1 < number_2)
# print(number_1 > 0)
# print(number_1 > False)
# print(number_1 >= number_2)


# obrabotka dannih iz faila
# import csv
#
# with open('csv.csv', 'r') as cars, open('car_status') as car_status:
#     car_reder = csv.reder(cars)
# class My(Exception):
#     pass


# def calc(a, b):
#     return a/b
#
#
# try:
#     print(calc(5, 3))
#     print(calc(2, 3))
#     print(calc(3, 0))
# # except ZeroDivisionError as error:
# #     print(error)
# except My as error:
#     raise My


# class VAlue(Exception):
#     pass
#
#
# class Valuet(Exception):
#     pass
#
# expected = 25
# while True:
#     try:
#         number = int(input("vvedi"))
#         if number < expected:
#            raise VAlue("bolche")
#         elif number > expected:
#             raise Valuet("bolche")
#         else:
#             print("win")
#     except VAlue as vtse:
#         print('znach<')
#     except Valuet as vtse:
#         print('znach>')


# my_set = {1, 2, (1,), "hello"}
# print(my_set)
# my_dict = {(1, 1): True, (1, 3): False, (3, 4): 3}
# print(my_dict)
# print(my_dict.get(1, 1))
#
# class Dot:
#     def __init__(self, x , y):
#         self.x = x
#         self.y = y
#
#
#     def __repr__(self):
#         return f'Dot({self.x}, {self.y})'
#
#
# zero_zero = Dot(0, 0)
#
# my_set = {1, 2, zero_zero}
# print(my_set)
# zero_zero.x = 5
# my_set = {1, 2, zero_zero}
# print(my_set)


# my_dict = {zero_zero: True,
#            one_two, False,
#           trhee: True}
# print(my_dict.get(zero_zero))

#zad 56
# file = open('csv.csv', 'r')
# for line in file:
#     print(file.read(10), end="")
# file.close()
# import os.path
#
#
# class Emply(Exception):
#     pass
#
#
# class FileNot(Exception):
#     pass
#
# file_name = input("vvedi:")
# if not file_name:
#     raise Emply
#
# if not file_name:
#     raise FileNot
#
# if not os.path.exists(file_name):
#     raise FileNot(f'net faila: {file_name}')
#
# with open(file_name, 'r') as file_for_read:
#     counter = 1
#     for row in file_for_read:
#         if counter <= 10:
#             print(row, end="")
#             counter += 1

#zad 59
# with open("csv.csv", 'r') as file_for_read:
#      counter = 1
#      for row in file_for_read:
#          if counter <= 20:
#              print(counter, row, end="")
#              counter += 1

# file = open('csv.csv', 'r')
# for line in file:
#     print(file.read(10), end="")
# file.close()
# import os.path
#
#
# class Emply(Exception):
#     pass
#
#
# class FileNot(Exception):
#     pass
#
# file_name = input("vvedi:")
# if not file_name:
#     raise Emply
#
# if not file_name:
#     raise FileNot
#
# file.target = file_name.split()
# print(file.target)
# if not os.path.exists(file_name):
#     raise FileNot(f'net faila: {file}')
#
# with open(file, 'r') as file_for_read, open('target.txt', 'w') as target_f:
#     counter = 1
#     for row in file_for_read:
#         line = f'{counter}: {row}'
#         print(line, end="")
#         counter += 1

# with open("csv.csv", "r") as source, open("text.txt", "w") as target_f:
#     for index, row in enumerate(source):
#         line = f'{index}: {row}'
#         target_f.write(line)


#zad 61

#if line.startswith('#'):
#    coninue

#zad 57

import tkinter

# window = tkinter.Tk()
# greeting = tkinter.Label(text='vvedi imia!', fg='blue', bg='red', width=20, height=20)
# greeting.pack()
# btn = tkinter.Button(text='hai',  fg='white', bg='black', width=5, height=5)
# btn.pack()
# enty = tkinter.Entry(text='enter a value', fg='blue', bg='red', width=20)
#
# enty.pack()
# name = enty.get()
# print(name)
# window.mainloop()

# window = tkinter.Tk()
# window.minsize(100, 100)
# first_frame = tkinter.Frame()
# second_frame = tkinter.Frame()
#
# first_lbl = tkinter.Label(master=first_frame, text='ferst lable', relief=tkinter.RIDGE)
# second_lbl = tkinter.Label(master=second_frame, text='second lable', relief=tkinter.GROOVE)
# first_lbl.pack()
# second_lbl.pack()
#
# first_frame.pack()
# second_frame.pack()
# window.mainloop()







# boorders = {
#     "flat": tkinter.FLAT,
#     "suncen": tkinter.SUNKEN,
#
# }
# window = tkinter.Tk()
# for relief_name in boorders.items():
#     frame = tkinter.Frame(master=window, relief=relief)
#     frame.pack()
#     lbl = tkinter.Label(master=frame, text=relief_name)
#     lbl.pack()
#
# window.mainloop()

# window = tkinter.Tk()
# window.minsize(100, 100)
#
# for i in range(3):
#     window.columnconfigure(i, weight=1, minsize=75)
#     window.rowconfigure(i, weight=1, minsize=50)
#     for j in range(3):
#         frame = tkinter.Frame(master=window, relief=tkinter.RAISED, borderwidth=1)
#         frame.grid(row=i, column=j, padx=5, pady=5)
#         lbl = tkinter.Label(master=frame, text=f'Row: {i}, \nCOL: {j}')
#         lbl.pack()
#
# window.mainloop()

# ввод данных и кнопка
# from tkinter import messagebox
#
# window = tkinter.Tk()
# window.title('vvedi adres')
# frame = tkinter.Frame()
# frame.pack()
# lbl_1_name = tkinter.Label(master=frame, text='name: ')
# ent_1_name = tkinter.Entry(master=frame, width=50)
# lbl_1_name.grid(row=0, column=0, sticky=tkinter.E)
# ent_1_name.grid(row=0, column=1)
#
# lbl_1_secondname = tkinter.Label(master=frame, text='secondname')
# ent_1_secondname = tkinter.Entry(master=frame, width=50)
# lbl_1_secondname.grid(row=2, column=0, sticky=tkinter.W)
# ent_1_secondname.grid(row=2, column=1)
#
# lbl_1_country = tkinter.Label(master=frame, text='country')
# ent_1_country = tkinter.Entry(master=frame, width=50)
# lbl_1_country.grid(row=3, column=0)
# ent_1_country.grid(row=3, column=1)
#
# lbl_1_city = tkinter.Label(master=frame, text='city')
# ent_1_city = tkinter.Entry(master=frame, width=50)
# lbl_1_city.grid(row=4, column=0)
# ent_1_city.grid(row=4, column=1)
#
# lbl_1_street = tkinter.Label(master=frame, text='street')
# ent_1_street = tkinter.Entry(master=frame, width=50)
# lbl_1_street.grid(row=5, column=0)
# ent_1_street.grid(row=5, column=1)
#
# lbl_1_index = tkinter.Label(master=frame, text='index')
# ent_1_index = tkinter.Entry(master=frame, width=50)
# lbl_1_index.grid(row=6, column=0, sticky=tkinter.W)
# ent_1_index.grid(row=6, column=1)
#
# def info():
#     messagebox.showinfo('save data')
#
# btn = tkinter.Button(master=frame, text='save...', command=info)
# btn.grid(row=7, column=1)
# window.mainloop()

# счетчик и +- кнопки
# def dec():
#     value = int(lbl_valve['text'])
#     lbl_valve['text'] = f'{value - 1}'
#
# def inc():
#     value = int(lbl_valve['text'])
#     lbl_valve['text'] = f'{value + 1}'
#
# window = tkinter.Tk()
# window.rowconfigure(0, minsize=50, weight=1)
# window.columnconfigure([0, 1, 2], minsize=50, weight=1)
# btn_dec = tkinter.Button(master=window, text='-', command=dec)
# btn_dec.grid(row=0, column=0)
# btn_inc = tkinter.Button(master=window, text='+', command=inc)
# btn_inc.grid(row=0, column=2)
# lbl_valve = tkinter.Label(master=window, text="0")
# lbl_valve.grid(row=0, column=1)
#
# window.mainloop()


from random import randint

# def roll():
#     lbl_result['text'] = str(randint(0, 10))
# window = tkinter.Tk()
# window.rowconfigure([0, 1], minsize=50)
# window.columnconfigure(0, minsize=100)
#
# btn = tkinter.Button(text='bros', command=roll)
# btn.grid(row=0, column=0, sticky='NSEW')
# lbl_result = tkinter.Label()
# lbl_result.grid(row=1, column=0)
#
# window.mainloop()

# class Convertet(tkinter.Tk): # конвертер в фаренгейт
#     def __init__(self):
#         super().__init__()
#         self.title = 'konvert temp'
#         self.geometry('200x50')
#         self.resizable(width=False, height=False)
#
#         self.frame = tkinter.Frame(self)
#         self.frame.grid(row=0, column=0, padx=10)
#         self.ent_temp = tkinter.Entry(self.frame, width=10)
#         self.lbl_temp = tkinter.Label(self.frame, text='\N{DEGREE FAHRENHEIT}')
#         self.ent_temp.grid(row=0, column=0, sticky="E")
#         self.lbl_temp.grid(row=0, column=1, sticky='W')
#
#         self.btn = tkinter.Button(self, text='\N{RIGHTWARDS BLACK ARROW}', command=self.convert)
#         self.btn.grid(row=0, column=1, padx=10)
#         self.lbl_res = tkinter.Label(self, text="\N{DEGREE CELSIUS}")
#         self.lbl_res.grid(row=0, column=2, padx=10)
#
#
#     def convert(self):
#         fareng = self.ent_temp.get()
#         if not fareng:
#             self.lbl_res['text'] = f"vvedi znachenie"
#             self.ent_temp.insert(0, 'vvedi znchenie')
#             return
#         celsius = ((5/9) * float(fareng)) - 32
#         self.lbl_res['text'] = f'{round(celsius, 2)} \N{DEGREE CELSIUS}'
#
# if __name__ == '__main__':
#     app = Convertet()
#     app.mainloop()
# from tkinter.filedialog import askopenfilename, asksaveasfilename
#
# def open_file():
#     filepath = askopenfilename(
#         filetypes=[('Text Files', "*.txt"), ("All Files", "*,*")]
#     )
#     # проверка на путь
#     txt_edit.delete(1.0, tkinter.END)
#     # чтение файла
#     with open(filepath, 'r') as input_file:
#         text = input_file.read()
#         txt_edit.insert(tkinter.END, text) # вставка значения в text edit
#     window.title(f'red txt - {filepath}')
#
# def save_file():
#     filepath = asksaveasfilename(
#         defaultextension='txt',
#         filetypes=[('Text Files', "*.txt"), ("All Files", "*,*")]
#     )
#     if not filepath:
#         return
#     with open(filepath, 'w') as output_file:
#         text = txt_edit.get(1.0, tkinter.END)
#
#
# window = tkinter.Tk()
# window.title('textovi redaktor')
# window.rowconfigure(0, minsize=800, weight=1)
# window.columnconfigure(1, minsize=800, weight=1)
#
# txt_edit = tkinter.Text(window)
# txt_edit.grid(row=0, column=1, sticky='NSEW')
# fr_btn = tkinter.Frame(window, relief=tkinter.SOLID)
# fr_btn.grid(row=0, column=0, sticky="NS")
# btn_open = tkinter.Button(fr_btn, text='Otkr', command=open_file)
# btn_open.grid(row=0, column=0, padx=5, pady=5)
# btn_save = tkinter.Button(fr_btn, text='Save', command="")
# btn_save.grid(row=1, column=0, padx=5, pady=5)
#
# window.mainloop()

#декораторы

# def firs_test():
#     print("test 1")
#
#
# def second_test():
#     print("test 2")
#
# def simple_decor(func):
#     def wr():
#         print('Run')
#         func()
#         print('stop')
#
#     return wr
#
# firs_test_wr = simple_decor(firs_test)
# second_test_wr = simple_decor(second_test)
#
# firs_test_wr()
# second_test_wr()
#
# @simple_decor
# def first_test():
#     print('test 1')
#
# test = first_test
# test()
#
# print()
#
# def  param_transfer(fn):
#     def wr(arg):
#         print(f'RUN {str(fn.__name__)}(), arans: {str(arg)}')
#         fn(arg)
#         print(f'Yello')
#
#     return wr
#
# @param_transfer
# def print_sqrt(num):
#     print(num ** 0,5)
#
#
# print_sqrt(4)
#
# def decor_ret(fn):
#     def wr(*args, **kwargs):
#         print(f'run: {str(fn.__name__)}')
#         return fn(*args, **kwargs)
#     return wr
#
#
# @decor_ret
# def calc(val):
#     return val ** 2
#
#
# print(calc(2))
# tmp = calc(3)
# print(tmp)

from pygame.color import THECOLORS
import pygame
import sys

#backgraund = pygame.image.load('') # путь у фону
# pygame.init()
#
# screen = pygame.display.set_mode((800, 800))
# screen.fill(THECOLORS['white'])
# r = pygame.Rect(50, 50, 100, 200)
# pygame.draw.rect(screen, THECOLORS['red'], r, 10)
# font = pygame.font.SysFont('None', 72, bold=True, italic=True)
# text = font.render('Hello', True, THECOLORS['green'])
# screen.blit(text, (400, 450))
# # pygame.draw.line(screen, THECOLORS['green'], (0, 0), (400, 400), 10)
# pygame.draw.polygon(screen, THECOLORS['green'], ((80, 80), (500, 50), (600, 600)), 10)
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

    #screen.blit(backgraund, (0, 0))
    #pygame.display.update()
    #pygame.display.flip()



#pygame.draw.line() # оверхность, цвет, начало, конец, ширина
#pygame.draw.lines() # оверхность, цвет, начало, позиции точек, ширина
#pygame.draw.circle() поверхность, цвет, позиция, радиус, ширина
#pygame.draw.ellipse() поверхность, цвет, Rect, ширина
#pygame.draw.plygon() поверхность цвет позиции точек ширина
 #bs4, requests flask django
 #pytorch tensorflow keras

pygame.init()
import time

display_w = 600
display_h = 600
pygame.display.set_caption('pySnace')
display = pygame.display.set_mode((display_w, display_h))
pygame.display.update()
clock = pygame.time.Clock()
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

snake_block = 10
game_over = False

x = display_w / 2
y = display_h / 2

x_change = 0
y_change = 0
snake_speed = 15

font = pygame.font.SysFont(None, 50)
def massege(text, color):
    msg = font.render(text, True, color)
    display.blit(msg, (display_w // 2, display_h // 2))

def game_loop():
    game_play = True
    game_close = False
    snake_block = 10
    x = display_w / 2
    y = display_h / 2
    x_change = 0
    y_change = 0
    snake_list = []


    while not game_play:
        while game_close:
            display.fill(white)
            massege('game over q- end, c - next', red)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_play = False
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_play = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -snake_block
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = snake_block
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0



        x += x_change
        y += y_change
        if x >= display_w or x < 0 or y >= display_h or y < 0:
            game_close = True
        # if x == display_w or x == 0:
        #     game_over = True
        # if y == display_h or y == 0:
        #     game_over = True

        display.fill(white)
        pygame.draw.rect(display, blue, [x, y, 10, 10])
        snake_head = [x, y]
        snake_list.append(snake_part)

        if len(snake_list) > snake_length:
            def snake_list():

        pygame.display.update()
        clock.tick(snake_speed)



    pygame.quit()
    quit()


game_loop()