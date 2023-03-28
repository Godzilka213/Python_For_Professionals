# БАНКОВСКАЯ КАРТА
# def hide_card(card):
#     return '*' * 12 + card.replace(' ', '')[-4:]
#
#
# card = '905 678123 45612 56'
#
# print(hide_card(card))
# import json

# ВЫВОДИМ ВСЕ ЭЛЕМЕНТЫ СОВПАДАЮЩИЕ С ЧЕТНОСТЬЮ ПЕРВОГО

# def same_parity(args):
#     return list(filter(lambda x: x % 2 == args[0] % 2, args))
#
#
# print(same_parity([-7, 0, 67, -9, 70, -29, 90]))
# OR
# def same_parity(nums):
#     return [i for i in nums if i % 2 == nums[0] % 2]
# print(same_parity([-7, 0, 67, -9, 70, -29, 90]))


# ВАЛИДНЫЙ ПАРОЛЬ

# def is_valid(password):
#     return password.isdigit() and len(password) in range(4,7)
#     # valid = True
#     # for _ in password:
#     #     if ' ' in password:
#     #         return False
#     # if 4 <= len(password) <= 6:
#     #     for i in password:
#     #         if i.isalpha():
#     #             valid = False
#     # else:
#     #     valid = False
#     # return valid
#
#
# print(is_valid('4676'))


# ТИП ДАННЫХ, КВАРГИ СОРТИРУЕМ ПО АЛФАВИТУ

# def print_given(*args, **kwargs):
#     kwargs = sorted(kwargs.items())
#     for i in args:
#         print(i, type(i))
#     for k, v in kwargs:
#         print(k, v, type(v))
#
#
#
# print_given(1, [1, 2, 3], 'three', b=2, d=4, c=3, a=1)


# ФОРМАТИРУЕМ СТРОКУ ОТ РЕГИСТРА

# def convert(txt):
# low = 0
# up = 0
# for i in txt:
#     if i.islower():
#         low += 1
#     elif i.isupper():
#         up += 1
# if low >= up:
#     return txt.lower()
# else:
#     return txt.upper()

# print(convert('pi31415!'))
# OR
# def convert(txt):
#     low = len(list(filter(str.islower, txt)))
#     up = len(list(filter(str.isupper, txt)))
#     if low >= up:
#         return txt.lower()
#     else:
#         return txt.upper()
# print(convert('pi31415!'))


# АНАГРАММЫ В АЛФАВИТНОМ ПОРЯДКЕ

# word = 'abba'
# anagrams = ['aabb', 'abcd', 'bbaa', 'dada']


# def filter_anagrams(word, words):
#     letters = sorted(word)
#     # result = []
#     # for i in words:
#     #     if sorted(list(i)) == letters:
#     #         result.append(i)
#     # return result
#     # OR return [i for i in words if letters == sorted(i)]
#
#
# print(filter_anagrams(word, anagrams))


# ЛАЙК likes

# def likes(names):
#     if len(names) == 0:
#         return 'Никто не оценил данную запись'
#     elif len(names) == 1:
#         return f'{names[0]} оценил(а) данную запись'
#     elif len(names) == 2:
#         return f'{names[0]} и {names[1]} оценили данную запись'
#     elif len(names) == 3:
#         return f'{names[0]}, {names[1]} и {names[2]} оценили данную запись'
#     else:
#         return f'{names[0]}, {names[1]} и {len(names[2:])} других оценили данную запись'
#
# print(likes(['Эндрю', 'Тоби', 'Том', 'Артур']))


# ИНДЕКС БЛИЖАЙШЕГО ЧИСЛА ИЗ СПИСКА

# def index_of_nearest(numbers, num):
#     if len(numbers) == 0:
#         return -1
#     else:
#         s = min(numbers, key=lambda x: abs(x - num))
#         return numbers.index(s)
#
#
# print(index_of_nearest([7, 13, 3, 5, 18], 0))


# СОЗДАЕМ СЛОВАРЬ С ПЕРВОЙ БУКВОЙ СЛОВА И МАКСИМАЛЬНОЙ ДЛИНОЙ СЛОВА НА ЭТУ БУКВУ

# words = ['fruit', 'football', 'February', 'forest', 'Family']
#
#
# def spell(*args):
#     my_dict = {}
#     for i in args:
#         my_dict[i[0].lower()] = my_dict.get(i[0].lower(), len(i))
#         if len(i) > my_dict[i[0].lower()]:
#             my_dict[i[0].lower()] = len(i)
#     return my_dict
#
#
# print(spell(*words))


# ПРАВИЛЬНОЕ СУЩЕСТВИТЕЛЬНОЕ


# def choose_plural(num, words):
#     suffixes = {
#         1: 0, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 0: 2,
#     }
#     if 11 <= num % 100 <= 14:
#         return f'{num} {words[2]}'
#     else:
#         return f'{num} {words[suffixes[num % 10]]}'
#     # if num % 10 == 0 or 5 <= num % 10 <= 9 or 11 <= num % 100 <= 14:
#     #     return words[2]
#     # elif 2 <= num % 10 <= 4:
#     #     return words[1]
#     # else:
#     #     return words[0]
#
#
# print(choose_plural(11, ('пример', 'примера', 'примеров')))


# САМОЕ БОЛЬШОЕ ЧИСЛО ПЕРЕСТАНОВКОЙ ЧИСЕЛ

# def get_biggest(num):
#     if len(num) != 0:
#         len_max = len(str(max(num)))
#         num = sorted(num, key=lambda x: str(x) * len_max, reverse=True)
#         res = ''
#         for i in num:
#             res += str(i)
#         return int(res)
#     return -1
#
#
# print(get_biggest([72, 7, 71]))


# КРАТЧАЙШИЙ ПУТЬ

# d1, d2, d3 = [int(input()) for i in range(3)]
# res = []
# res.append(d1 + d3 + d2)
# res.append(d1 * 2 + d2 * 2)
# res.append(d1 + d3 * 2 + d1)
# res.append(d2 + d3 * 2 + d2)
# print(min(res))


# СХОЖИЕ БУКВЫ

# en, ru = 'AaBCcEeHKMOoPpTXxy', 'АаВСсЕеНКМОоРрТХху'
# letters = [input() for _ in range(3)]
# s = sum(1 if i in ru else 0 for i in letters)
# if s == len(letters):
#     print('ru')
# elif s == 0:
#     print('en')
# else:
#     print('mix')
# print(['en', 'mix', 'mix', 'ru'][sum(1 if i in ru else 0 for i in letters)])


# ПЕРЕВОРОТ

# n, x, y, a, b = list(map(int, input().split()))
# my_list = list(range(1, n + 1))
#
# my_list[x-1: y] = my_list[x-1: y][::-1]
# my_list[a-1: b] = my_list[a-1: b][::-1]
# print(*my_list)


# БОЛЕЕ ОДНОГО

# numbers = list(map(int, input().split()))
# my_set = set()
# for i in numbers:
#     if numbers.count(i) > 1:
#         my_set.add(i)
# print(*sorted(my_set))
# OR
# nums = list(map(int, input().split()))
# print(*set(i for i in nums if nums.count(i) > 1))


# num = list(map(str, list(range(1, int(input()) + 1))))
# res = {}
# for i in num:
#     for j in i:
#         res[i] = res.get(i, 0) + int(j)
#
# print(n)


# МАКСИМАЛЬНАЯ ГРУППА

# nums = range(1, int(input()) + 1)
# d = dict()
# for i in nums:
#     sum_i = sum(int(j) for j in str(i))
#     d.setdefault(sum_i, []).append(i)
# t = (list(d.values()))
# print(len(max(t, key=len)))
# # OR
# d = {}
# for i in range(1, int(input()) + 1):
#     s = sum([int(x) for x in str(i)])
#     d[s] = d.get(s, 0) + 1
# print(max(d.values()))
# OR
# data = {}
#
# for i in range(1, int(input()) + 1):
#     sum_of_digits = sum(map(lambda d: int(d), str(i)))
#     data[sum_of_digits] = data.get(sum_of_digits, 0) + 1
#
# print(max(data.values()))


# ТРУДНОСТИ ПЕРЕВОДА

# from functools import reduce
#
# n = int(input())
# lst = [set(input().split(', ')) for i in range(n)]
# my_set = reduce(lambda x, y: x & y, lst)
# print(', '.join(sorted(my_set)) if my_set else 'Сериал снять не удастся')


# СХОЖИЕ СЛОВА

# gl = 'ауоыиэяюёе'
# main_word = input()
# words = [input() for i in range(int(input()))]
# check = [i for i in range(len(main_word)) if main_word[i] in gl]
#
# for i in words:
#     res = [j for j in range(len(i)) if i[j] in gl]
#     if check == res:
#         print(i)


# КОРПОРАТИВНАЯ ПОЧТА

# email = '@beegeek.bzz'
# old = [input() for i in range(int(input()))]
# new = [input() for j in range(int(input()))]
# res = []
# counter = 1
# for i in new:
#     if i + email not in old:
#         res.append(i + email)
#         old.append(i + email)
#     elif i + email in old:
#         while i + str(counter) + email in old:
#             counter += 1
#         res.append(i + str(counter) + email)
#         old.append(i + str(counter) + email)
#         counter = 1
#
# print(*res, sep='\n')
# OR
# emails = set(input() for _ in range(int(input())))
# for _ in range(int(input())):
#     emp = input()
#     email = f'{emp}@beegeek.bzz'
#     count = 0
#     while email in emails:
#         count += 1
#         email = f'{emp}{count}@beegeek.bzz'
#     emails.add(email)
#     print(email)


# ФАЙЛЫ В ФАЙЛЕ

# def file():
#     with open('files.txt', 'r', encoding='utf-8') as file:
#         data = []
#         for line in file.readlines():
#             line = line.split()
#             data.append(line)
#         # Получаем список списков ^_^ в отсортированном виде, как требуется по расширению и название по алфавиту
#         data = sorted(data, key=lambda x: (x[0].split('.')[1], x[0]))
#         # Создаем словари с именами файлов и их размерами
#         name = {}
#         mass = {}
#         for i in range(len(data)):
#             name.setdefault(data[i][0].split('.')[1], []).append(data[i][0])
#             mass.setdefault(data[i][0].split('.')[1], []).append([int(data[i][1]), data[i][2]])
#         # Приводим размеры файлов в байты и получаем максимальную размерность файлов от общего размера
#         size = {'B': 1,
#                 'KB': 1024,
#                 'MB': 1024 * 1024,
#                 'GB': 1024 * 1024 * 1024,
#                 }
#         summary = 0
#         result_size = []
#         for k, v in mass.items():
#             for i in v:
#                 summary += i[0] * size[i[1]]
#             if summary < 1024:
#                 result_size.append([summary, 'B'])
#             elif summary < 1024 * 1024:
#                 result_size.append([summary / 1024, 'KB'])
#             elif summary < 1024 * 1024 * 1024:
#                 result_size.append([summary / 1024 / 1024, 'MB'])
#             else:
#                 result_size.append([summary / 1024 / 1024 / 1024, 'GB'])
#             summary = 0
#
#         # Вывод
#         j = 0
#         for k, v in name.items():
#             print(*v, sep='\n')
#             print('----------')
#             print(f'Summary: {round(result_size[j][0])} {result_size[j][1]}', end='\n\n')
#             j += 1
#
#
# file()

# КВАРТАЛЫ

# from datetime import date
#
# dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27), date(2021, 10, 11),
#          date(2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19), date(2013, 8, 21),
#          date(1666, 6, 6), date(1968, 5, 26)]
#
# for d in dates:
#     print(f'{d.year}-Q{(d.month - 1) // 3 + 1}')


# МИН И МАКС ДАТА

# from datetime import date
#
# dates = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]
#
#
# def get_min_max(d):
#     if len(d) == 0:
#         return ()
#     return min(d), max(d)
#
#
# print(get_min_max(dates))


# ДАТЫ ОТ И ДО


# from datetime import date
#
#
# def get_date_range(d1, d2):
#     d1 = d1.toordinal()
#     d2 = d2.toordinal()
#     lst = []
#     if d1 == d2:
#         return [date.fromordinal(d1)]
#     elif d1 > d2:
#         return []
#
#     for i in (range(d1, d2 + 1)):
#         lst.append(date.fromordinal(i))
#     return lst
#
#
# date1 = date(2021, 10, 1)
# date2 = date(2021, 10, 5)
#
# print(*get_date_range(date1, date2), sep='\n')


# КОЛИЧЕСТВО СУББОТ

# from datetime import date
#
#
# def saturdays_between_two_dates(d1, d2):
#     start = d1.toordinal()
#     end = d2.toordinal()
#     if start > end:
#         start, end = end, start
#
#     return len([date.fromordinal(i) for i in range(start, end + 1) if date.weekday(date.fromordinal(i)) == 5])
#
#
# date1 = date(2021, 11, 1)
# date2 = date(2021, 11, 22)
#
# print(saturdays_between_two_dates(date1, date2))


# ЧАСЫ, МИНУТЫ, СЕКУНДЫ

# from datetime import date, time
#
# my_date = date(2021, 12, 31)
# my_time = time(21, 15, 17)
#
# print(my_date)
# print(my_time)


# РАЗНЫЕ ФОРМАТЫ ДАТЫ

# from datetime import date
#
# andrew = date(1992, 8, 24)
#
# print(andrew.strftime('%Y-%m'))   # выводим дату в формате YYYY-MM
# print(andrew.strftime('%B (%Y)'))   # выводим дату в формате month_name (YYYY)
# print(andrew.strftime('%Y-%j'))   # выводим дату в формате YYYY-day_number


# from datetime import date
#
# date1 = date.fromisoformat(input())
# date2 = date.fromisoformat(input())
#
# print(min(date1, date2).strftime('%d-%m (%Y)'))


# from datetime import date
#
# lst = sorted([date.fromisoformat(input()) for _ in range(int(input()))])
#
# for i in lst:
#     print(i.strftime('%d/%m/%Y'))


# ИНТЕРЕСНАЯ ДАТА

# from datetime import date
#
# def print_good_dates(dates):
#
#     dates = sorted(dates)
#     for i in dates:
#         if int(str(i)[0:4]) == 1992 and int(str(i)[-2:]) + int(str(i)[-5:-3]) == 29:
#             print(i.strftime('%B %d, %Y'))
#
# dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
# print_good_dates(dates)


# КОРРЕКТНАЯ ДАТА

# from datetime import date
#
#
# def is_correct(d, m, y):
#     try:
#         my_date = date(int(y), int(m), int(d))
#         return True
#     except ValueError:
#         return False
#
#
# print(is_correct(31, 12, 2021))


# КОРРЕКТНЫЕ ДАТЫ

# from datetime import date
#
#
# def is_correct():
#     d = input()
#     counter = 0
#     while d != 'end':
#         day, month, year = d.split('.')
#         try:
#             f = date(int(year), int(month), int(day))
#             counter += 1
#             print('Корректная')
#         except:
#             print('Некорректная')
#         d = input()
#     print(counter)
#
#
# is_correct()


# ПОЛУЧАЕМ DATETIME

# from datetime import datetime
#
# text = 'Уважаемый пациент, доктор готов принять Вас 15.07.2022 в 08:30'
#
# dt = datetime.strptime(text, 'Уважаемый пациент, доктор готов принять Вас %d.%m.%Y в %H:%M')
#
# print(dt)


# СЕКУНДЫ В ДАТУ И ДАТУ В СЕКУНДЫ

# from datetime import datetime
#
# seconds = 2483228800
# dt = datetime(2011, 11, 4)
#
# print(datetime.fromtimestamp(seconds))
# print(dt.timestamp())


# ПОКУПКИ ДО ПОЛУДНЯ

# from datetime import datetime
#
# times_of_purchases = [datetime(2017, 10, 1, 12, 23, 25), datetime(2017, 10, 1, 15, 26, 26),
#                       datetime(2017, 10, 1, 15, 42, 57), datetime(2017, 10, 1, 17, 49, 59),
#                       datetime(2017, 10, 2, 6, 37, 10), datetime(2017, 10, 2, 6, 42, 53),
#                       datetime(2017, 10, 2, 8, 56, 45), datetime(2017, 10, 2, 9, 18, 3),
#                       datetime(2017, 10, 2, 12, 23, 48), datetime(2017, 10, 2, 12, 45, 5),
#                       datetime(2017, 10, 2, 12, 48, 8), datetime(2017, 10, 2, 12, 10, 54),
#                       datetime(2017, 10, 2, 19, 18, 10), datetime(2017, 10, 2, 12, 31, 45),
#                       datetime(2017, 10, 3, 20, 57, 10), datetime(2017, 10, 4, 7, 4, 57),
#                       datetime(2017, 10, 4, 7, 13, 31), datetime(2017, 10, 4, 7, 13, 42),
#                       datetime(2017, 10, 4, 7, 21, 54), datetime(2017, 10, 4, 14, 22, 12),
#                       datetime(2017, 10, 4, 14, 50), datetime(2017, 10, 4, 15, 7, 27),
#                       datetime(2017, 10, 4, 12, 44, 49), datetime(2017, 10, 4, 12, 46, 41),
#                       datetime(2017, 10, 4, 16, 32, 33), datetime(2017, 10, 4, 16, 34, 44),
#                       datetime(2017, 10, 4, 16, 46, 59), datetime(2017, 10, 4, 12, 26, 6)]
# a = len(times_of_purchases)
# c = 0
# for i in times_of_purchases:
#     if i.hour < 12:
#         c += 1
# print('До полудня' if a < c else 'После полудня')
# OR
# from datetime import datetime
#
# times_of_purchases = [datetime(2017, 10, 1, 12, 23, 25), datetime(2017, 10, 1, 15, 26, 26),
#                       datetime(2017, 10, 1, 15, 42, 57), datetime(2017, 10, 1, 17, 49, 59),
#                       datetime(2017, 10, 2, 6, 37, 10), datetime(2017, 10, 2, 6, 42, 53),
#                       datetime(2017, 10, 2, 8, 56, 45), datetime(2017, 10, 2, 9, 18, 3),
#                       datetime(2017, 10, 2, 12, 23, 48), datetime(2017, 10, 2, 12, 45, 5),
#                       datetime(2017, 10, 2, 12, 48, 8), datetime(2017, 10, 2, 12, 10, 54),
#                       datetime(2017, 10, 2, 19, 18, 10), datetime(2017, 10, 2, 12, 31, 45),
#                       datetime(2017, 10, 3, 20, 57, 10), datetime(2017, 10, 4, 7, 4, 57),
#                       datetime(2017, 10, 4, 7, 13, 31), datetime(2017, 10, 4, 7, 13, 42),
#                       datetime(2017, 10, 4, 7, 21, 54), datetime(2017, 10, 4, 14, 22, 12),
#                       datetime(2017, 10, 4, 14, 50), datetime(2017, 10, 4, 15, 7, 27),
#                       datetime(2017, 10, 4, 12, 44, 49), datetime(2017, 10, 4, 12, 46, 41),
#                       datetime(2017, 10, 4, 16, 32, 33), datetime(2017, 10, 4, 16, 34, 44),
#                       datetime(2017, 10, 4, 16, 46, 59), datetime(2017, 10, 4, 12, 26, 6)]
# # Создаем список с временем до 12 и после 12, соответственно АМ или РМ
# dts = [d.strftime('%p') for d in times_of_purchases]
# # Выводим результат при помощи count()
# print(['До полудня', 'После полудня'][dts.count('PM') > dts.count('AM')])


# ОБЪЕДИНЕНИЕ И СОРТИРОВКА ПО СЕКУНДАМ

# from datetime import date, time, datetime
#
# dates = [date(1793, 8, 23), date(1410, 3, 11), date(804, 11, 12), date(632, 6, 4),
#          date(295, 1, 23), date(327, 8, 24), date(167, 4, 16), date(229, 1, 24),
#          date(1239, 2, 5), date(1957, 7, 14), date(197, 8, 24), date(479, 9, 6)]
#
# times = [time(7, 33, 27), time(21, 2, 10), time(17, 20, 47), time(20, 8, 59),
#          time(12, 42, 56), time(15, 9, 57), time(17, 47, 9), time(9, 40, 2),
#          time(11, 47, 1), time(17, 27, 10), time(17, 55, 40), time(9, 14, 9)]
# full = list(zip(dates, times))
# res = [datetime.combine(d, t) for d, t in full]
#
# print(*sorted(res,key=lambda x: x.second), sep='\n')
# OR
# dt = map(datetime.combine, dates, times)
# print(*sorted(dt, key=lambda x: x.second), sep='\n')


# САМЫЙ БЫСТРЫЙ УЧЕНИК

# from datetime import datetime
#
# data = {'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'),
#         'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'),
#         'Анна': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'),
#         'Илина': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'),
#         'Герман': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'),
#         'Руслан': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'),
#         'Лера': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'),
#         'Егор': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'),
#         'Максим': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'),
#         'Саша': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'),
#         'Марина': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')}
#
# for k, v in data.items():
#     start = datetime.strptime(v[0], '%d.%m.%Y %H:%M:%S').timestamp()
#     finish = datetime.strptime(v[1], '%d.%m.%Y %H:%M:%S').timestamp()
#     data[k] = finish - start
#
# print(min(data, key=data.get))


# ДНЕВНИК КОСМОНАВТА

# from datetime import datetime
#
# with open('diary.txt', 'r', encoding='utf-8') as file:
#     file = (file.read().split('\n\n'))
#     print(*sorted(file, key=lambda x: datetime.strptime(x[:17], '%d.%m.%Y; %H:%M')), sep='\n\n')


# БРОНИРОВАНИЕ ДАТЫ

# from datetime import datetime
#
#
# def is_available_date(close, book):
#     booked = []
#     free = []
#     # Получаем дни и диапазоны забронированных дней в booked
#     for day in close:
#         if len(day) == 10:
#             booked.append(datetime.strptime(day, '%d.%m.%Y').toordinal())
#         else:
#             day = day.split('-')
#             booked.append(list(range(datetime.strptime(day[0], '%d.%m.%Y').toordinal(),
#                                      datetime.strptime(day[1], '%d.%m.%Y').toordinal() + 1)))
#     # Получаем дни и дипапазоны бронируемых дней
#     book = book.split('-')
#     if len(book) == 2:
#         free.append(list(range(datetime.strptime(book[0], '%d.%m.%Y').toordinal(),
#                                datetime.strptime(book[1], '%d.%m.%Y').toordinal() + 1)))
#     else:
#         free.append(datetime.strptime(book[0], '%d.%m.%Y').toordinal())
#     # Перебираем все даты и получаем множество забронированных дат
#     set_booked = set()
#     for i in booked:
#         if type(i) is list:
#             for j in i:
#                 set_booked.add(j)
#         else:
#             set_booked.add(i)
#     # Перебираем все даты и получаем множество бронируемых дат
#     set_free = set()
#     for j in free:
#         if type(j) is list:
#             for k in j:
#                 set_free.add(k)
#         else:
#             set_free.add(j)
#     # Выводим True или False при помощи .isdisjoint
#     return set_booked.isdisjoint(set_free)
#
#
# dates = ['04.11.2021', '05.11.2021-09.11.2021']
# some_date = '01.11.2021'
# print(is_available_date(dates, some_date))
# OR
# from datetime import datetime
#
#
# def sd(s):  # функция превращает строку в дату
#     return datetime.strptime(s, '%d.%m.%Y')
#
#
# def dk(spd):  # функция превращает строку c датой или интервалом дат в кортеж из 2 дат
#     return (sd(spd[:10]), sd(spd[11:])) if '-' in spd else (sd(spd), sd(spd))
#
#
# def is_available_date(sp, d):
#     for x in sp:  # проверяем, пересекаются ли кортежи дат гостя и отеля
#         if not (dk(x)[1] < dk(d)[0] or dk(x)[0] > dk(d)[1]):
#             return False  # если пересекаются, то выводим False
#     return True  # а если нет, то True
#
#
# dates = ['04.11.2021', '05.11.2021-09.11.2021']
# some_date = '06.11.2021'
# print(is_available_date(dates, some_date))


# from datetime import datetime, timedelta
#
# dt = datetime(2021, 11, 4, 13, 6) + timedelta(weeks=1, hours=12)
#
# print(dt.strftime('%d.%m.%Y %H:%M:%S'))


# from datetime import date, timedelta
#
# today = date(2021, 11, 4)
# birthday = date(2022, 10, 6)
#
# days = (birthday - today).days
#
# print(days)


# from datetime import datetime, timedelta
#
# data = datetime.strptime(input(), '%d.%m.%Y')
# yesterday = data - timedelta(days=1)
# tommorow = data + timedelta(days=1)
# print(yesterday.strftime('%d.%m.%Y'),
#       tommorow.strftime('%d.%m.%Y'), sep='\n')


# from datetime import timedelta
#
# h, m, s = input().split(':')
# data = timedelta(hours=int(h), minutes=int(m), seconds=int(s)).total_seconds()
# print(int(data))


# ТАЙМЕР

# from datetime import datetime, timedelta
#
# time_input = input()
# plus = int(input())
# data = datetime.strptime(time_input, '%H:%M:%S') + timedelta(seconds=plus)
# print(data.strftime('%H:%M:%S'))


# КОЛИЧЕСТВО ВОСКРЕСЕНИЙ В ГОДУ
#
# from datetime import datetime
#
#
# def num_of_sundays(y):
#     data = datetime(year=y, month=12, day=31)
#     print(data)
#     return data.strftime('%U')
#
#
# print(num_of_sundays(2000))


# ПРОДУКТИВНОСТЬ

# from datetime import datetime, timedelta
#
# pattern = '%d.%m.%Y'
# start = datetime.strptime(input(), pattern)
#
# for i in range(1, 11):
#     print(start.strftime(pattern))
#     start += timedelta(days=1 + i)


# СОСЕДНИЕ ДАТЫ

# from datetime import datetime
#
# pattern = '%d.%m.%Y'
#
# dates = [datetime.strptime(i, pattern) for i in input().split()]
# print([abs(dates[i] - dates[i + 1]).days for i in range(len(dates) - 1)])


# СПИСОК ВСЕХ ДАТ

# from datetime import datetime
#
#
# def fill_up_missing_dates(lst):
#     lst = list(map(lambda x: datetime.strptime(x, '%d.%m.%Y').toordinal(), lst))
#     min_data = min(lst)
#     max_data = max(lst)
#     return [datetime.fromordinal(i).strftime('%d.%m.%Y') for i in range(min_data, max_data + 1)]
#
#
# dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']
#
# print(fill_up_missing_dates(dates))


# РАСПИСАНИЕ

# from datetime import datetime, timedelta
#
# start = datetime.strptime(input(), '%H:%M')
# finish = datetime.strptime(input(), '%H:%M')
#
# while (start + timedelta(minutes=45)) <= finish:
#     print(f"{start.strftime('%H:%M')} - {(start + timedelta(minutes=45)).strftime('%H:%M')}")
#     start = start + timedelta(minutes=55)


# import time
#
# for i in [0.7, 0.5, 1.0, 2.5, 3.3]:
#     print(f'Waiting for {i} seconds')
#     time.sleep(i)
# print('The end')


# ОБЩЕЕ ВРЕМЯ

# from datetime import datetime
# from functools import reduce
#
# data = [('07:14', '08:46'),
#         ('09:01', '09:37'),
#         ('10:00', '11:43'),
#         ('12:13', '13:49'),
#         ('15:00', '15:19'),
#         ('15:58', '17:24'),
#         ('17:57', '19:21'),
#         ('19:30', '19:59')]
#
# data_time = list(map(lambda x: (datetime.strptime(x[1], '%H:%M')) - (datetime.strptime(x[0], '%H:%M')), data))
# data_time = reduce(lambda x, y: x + y, data_time)
#
# print(data_time.seconds // 60)


# КОЛИЧЕСТВО ДНЕЙ ВЫПАВШИХ НА 13Е ЧИСЛО

# from datetime import datetime
#
# pattern = '%d.%m.%Y'
# start = datetime.strptime('01.01.0001', pattern).toordinal()
# finish = datetime.strptime('31.12.9999', pattern).toordinal()
# my_dict = dict.fromkeys(range(7), 0)
#
# for i in range(start, finish + 1):
#     day = datetime.fromordinal(i).strftime('%d')
#     if int(day) == 13:
#         week_day = datetime.fromordinal(i).weekday()
#         my_dict[week_day] = my_dict.get(week_day) + 1
#
# print(*list(my_dict.values()), sep='\n')
# OR
# from datetime import date
#
# my_dict = dict.fromkeys((range(7)), 0)
#
# for i in range(1, 10_000):
#     for j in range(1, 13):
#         my_dict[date(i, j, 13).weekday()] = my_dict.get(date(i, j, 13).weekday()) + 1
# print(*list(my_dict.values()), sep='\n')


# ВРЕМЯ РАБОТЫ

# from datetime import datetime, timedelta
#
# data = datetime.strptime(input(), '%d.%m.%Y %H:%M')
# # Переводим дату в timedelta для возможности сравнить время
# new = timedelta(hours=data.hour, minutes=data.minute)
#
# # Начало и конец работы в будни и выходные
# work_day = [timedelta(hours=9), timedelta(hours=21)]
# not_work_day = [timedelta(hours=10), timedelta(hours=18)]
#
# # Проверяем условие для будних дней в секундах
# if work_day[0].seconds <= new.seconds < work_day[1].seconds and data.weekday() in [0, 1, 2, 3, 4]:
#     # Получаем время в минутах
#     before = (work_day[1].seconds - new.seconds) // 60
#     print(before)
#
# # Проверяем условие для выходного дня в секундах
# elif not_work_day[0].seconds <= new.seconds < not_work_day[1].seconds and data.weekday() in [5, 6]:
#     # Получаем время в минутах
#     before = (not_work_day[1].seconds - new.seconds) // 60
#     print(before)
#
# # Не попали в рабочее время
# else:
#     print('Магазин не работает')
#
# print(data.weekday())
# OR
# from datetime import datetime
#
# date = datetime.strptime(input(), '%d.%m.%Y %H:%M')
#
# start, end = (date.replace(hour=i, minute=0) for i in ((9, 21), (10, 18))[date.weekday() > 4])
# print(start)
# if start <= date < end:
#     print((end - date).seconds // 60)
# else:
#     print('Магазин не работает')


# ДАТЫ НАЧИНАЯ С НЕЧЕТНОЙ, КАЖДАЯ ТРЕТЬЯ И НЕ ПОНЕДЕЛЬНИК, ЧЕТВЕРГ

# from datetime import datetime, timedelta
#
# pattern = '%d.%m.%Y'
# start, finish = datetime.strptime(input(), pattern), datetime.strptime(input(), pattern)
# # Находим начальную дату вывода(нечетную)
# while (start.day + start.month) % 2 == 0:
#     start = start + timedelta(days=1)
# # Выводим каждую третью дату если не понедельник, четверг
# while start <= finish:
#     if start.weekday() not in [0, 3]:
#         print(start.strftime(pattern))
#     start += timedelta(days=3)


# СОТРУДНИКИ ОРГАНИЗАЦИИ, САМЫЕ СТАРЫЕ

# from datetime import datetime
#
# pattern = '%d.%m.%Y'
# lst = [input() for i in range(int(input()))]
# my_dict = {}
# # Создаем словарь дата(ключ): ФИО(значение)
# for i in lst:
#     # Создаем дату при помощи среза
#     key_data = datetime.strptime(i[-10:], pattern)
#     # Добавляем к датам ФИО
#     my_dict[key_data] = my_dict.get(key_data, []) + [i[:-11]]
#
# # Получаем дату самого старого сотрудника
# data = min(my_dict)
# # Получаем количество сотрудников с одинаковой датой
# length = len(my_dict[data])
# # Выводим дату, ФИО если старый сотрудник один
# if length == 1:
#     print(data.strftime(pattern), *my_dict[data])
# else:
#     print(data.strftime(pattern), length)


# СОТРУДНИКИ ОРГАНИЗАЦИИ, ДАТЫ ДНЕЙ РОЖДЕНИЯ
#
# from datetime import datetime
#
# pattern = '%d.%m.%Y'
# lst = [input() for i in range(int(input()))]
# my_dict = {}
# # Создаем словарь дата(ключ): ФИО(значение)
# for i in lst:
#     # Создаем дату при помощи среза
#     key_data = datetime.strptime(i[-10:], pattern)
#     # Добавляем к датам ФИО
#     my_dict[key_data] = my_dict.get(key_data, []) + [i[:-11]]
# # Замудренный вывод
# res = []
# res_2 = []
# for k, v in my_dict.items():
#     if len(v) > 1:
#         res.append(k)
#     else:
#         res_2.append(k)
# res = sorted(res)
# res_2 = sorted(res_2)
# if len(res) > 0:
#     for i in res:
#         print(i.strftime(pattern))
# else:
#     for i in res_2:
#         print(i.strftime(pattern))

# СОТРУДНИКИ ОРГАНИЗАЦИИ, ПОСЛЕДНИЙ ДЕНЬ РОЖДЕНИ В ТЕЧЕНИИ 7 ДНЕЙ ОТ ТЕКУЩЕЙ ДАТЫ

# from datetime import datetime, timedelta
#
# pattern = '%d.%m.%Y'
# check = datetime.strptime(input(), pattern)
# lst = [input() for i in range(int(input()))]
# my_dict = {}
# # Создаем словарь дата(ключ): ФИО(значение)
# for i in lst:
#     # Создаем дату при помощи среза
#     key_data = datetime.strptime(i[-10:], pattern)
#     # Приводим год ключа к году проверки или +1 для конца года
#     if check < key_data.replace(year=check.year) <= check + timedelta(days=7) or \
#         check < key_data.replace(year=check.year + 1) <= check + timedelta(days=7):
#         # Добавляем к датам ФИО
#         my_dict[key_data] = my_dict.get(key_data, []) + [i[:-11]]
# if len(my_dict) > 0:
#     birthday = max(my_dict.items())
#     print(*birthday[1])
# else:
#     print('Дни рождения не планируются')


# ЛОЖНЫЕ НОВОСТИ

# from datetime import datetime
#
# days = ['день', 'дня', 'дней']
# hours = ['час', 'часа', 'часов']
# minutes = ['минута', 'минуты', 'минут']
# txt = 'До выхода курса осталось:'
# main_data = datetime.strptime('08.11.2022 12:00', '%d.%m.%Y %H:%M')
#
#
# def choose_plural(num, words):
#     suffixes = {
#         1: 0, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 0: 2,
#     }
#     if 11 <= num % 100 <= 14:
#         return f'{num} {words[2]}'
#     else:
#         return f'{num} {words[suffixes[num % 10]]}'
#
#
# data = datetime.strptime(input(), '%d.%m.%Y %H:%M')
# res = main_data - data
# d = res.days
# h = res.seconds // 3600
# m = int(res.seconds / 60 % 60)
#
# if main_data <= data:
#     print('Курс уже вышел!')
#
# # Если остались часы и минуты
# elif d < 1:
#     if h == 0:
#         print(f'{txt} {choose_plural(m, minutes)}')
#     elif m == 0:
#         print(f'{txt} {choose_plural(h, hours)}')
#     else:
#         print(f'{txt} {choose_plural(h, hours)}', 'и', f'{choose_plural(m, minutes)}')
# else:
#     if h != 0:
#         print(f'{txt} {choose_plural(d, days)}', 'и', f'{choose_plural(h, hours)}')
#     else:
#         print(f'{txt} {choose_plural(d, days)}')

# ВРЕМЯ ВЫПОЛНЕНИЯ

# import time
#
#
# def add(a, b, c):
#     time.sleep(3)
#     return a + b + c
#
#
# def calculate_it(add, *args):
#     start = time.monotonic()
#     s = add(*args)
#     end = time.monotonic()
#     res = end - start
#     return s, res
#
#
# print(calculate_it(add, 1, 2, 3))


# СПИСОК ФУНКЦИЙ

# import time
#
#
# def slow(arg):
#     time.sleep(3)
#
#
# def fast(arg):
#     time.sleep(1)
#
#
# def get_the_fastest_func(funcs, arg):
#     res = []
#     for i in funcs:
#         s = time.perf_counter()
#         i(arg)
#         f = time.perf_counter()
#         res.append(f - s)
#     huh = list(zip(funcs, res))
#     huh = sorted(huh, key=lambda x: x[1])
#     return huh[0][0]
#
#
# funcs = [slow, fast]
#
# print(get_the_fastest_func(funcs, 0))


# ВИСОКОСНЫЙ ГОД

# from calendar import isleap
#
# data = [print(isleap(int(input()))) for i in range(int(input()))]


# КАЛЕНДАРЬ НА МЕСЯЦ

# import calendar
#
# month_ = list(calendar.month_abbr)
# data = input()
# print(calendar.month(int(data[:4]), month_.index(data[-3:])))


# МЕСЯЦ

# from datetime import datetime
# from calendar import day_name
#
# data = datetime.strptime(input(), '%Y-%m-%d').weekday()
# list_day = list(day_name)
#
# print(list_day[data])


# КОЛИЧЕСТВО ДНЕЙ В МЕСЯЦЕ

# import calendar
#
# y, m = input().split()
# print(calendar.monthrange(int(y), int(m))[1])


# КОЛИЧЕСТВО ДНЕЙ В МЕСЯЦЕ

# import calendar
#
# year, m = input().split()
# m_index = list(calendar.month_name).index(m)
# print(calendar.monthrange(int(year), m_index)[1])


# ОТСОРТИРОВАННЫЙ СПИСОК ДАТ

# from datetime import date
# import calendar
#
#
# def get_days_in_month(y, m):
#     m_index = list(calendar.month_name).index(m)
#     m_range = int(calendar.monthrange(y, m_index)[1])
#     res = []
#     for i in range(1, m_range + 1):
#         res.append(date(year=y, month=m_index, day=i))
#     return res
#
#
# print(get_days_in_month(2021, 'December'))


# СПИСОК ГОДОВ ВЫПАДАЮЩИХ НА ПОНЕДЕЛЬНИК

# from datetime import date
# import calendar
#
#
# def get_all_mondays(yr):
#     res = []
#     for i in range(1, 13):
#         days = calendar.monthrange(yr, i)[1]
#         for j in range(1, days + 1):
#             day = date(year=yr, month=i, day=j)
#             if day.weekday() == 0:
#                 res.append(date(year=yr, month=i, day=j))
#     return res
#
# print(get_all_mondays(2021))


# ТРЕТИЙ ЧЕТВЕРГ МЕСЯЦА

# import calendar
# from datetime import date
#
# year = int(input())
# counter = 0
# for month in range(1, 13):
#     for week in calendar.monthcalendar(year, month):
#
#         if week[3]:
#             counter += 1
#             if counter == 3:
#                 print(date(year=year, month=month, day=week[3]).strftime('%d.%m.%Y'))
#                 counter = 0
#                 break


# ОБРАТНЫЙ ПОРЯДОК

# import sys
#
# data = list(map(str.strip, sys.stdin))
#
# for line in data:
#     print(line[::-1])


# РАЗМАХ ДАННЫХ

# import sys
# from datetime import datetime
#
# data = []
# for i in sys.stdin:
#     data.append(datetime.fromisoformat(i.rstrip('\n')))
# print(max(data).toordinal() - min(data).toordinal())


# ЛЕММА О ТРЕХ НОСКАХ

# import sys
#
# name = ['Анри', 'Дима']
# numbers = list(reversed([int(i) for i in sys.stdin]))
#
# if numbers[0] % 2 == 0:
#     print(name[(len(numbers) - 1) % 2])
#
# else:
#     print(name[len(numbers) % 2])


# УРОК СТАТИСТИКИ

# import sys
#
# high = list(map(int, sys.stdin))
#
# if len(high) > 0:
#     middle = sum(high) / len(high)
#     print(f'Рост самого низкого ученика: {min(high)}',
#           f'Рост самого высокого ученика: {max(high)}', f'Средний рост: {middle}', sep='\n')
# else:
#     print('нет учеников')


# КОММЕНТАТОР

# import sys
#
# lst = list(map(str.strip, sys.stdin))
# counter = sum([1 for i in lst if i.startswith('#')])
#
# print(counter)


# БЕЗ КОММЕНТАРИЕВ

# import sys
#
# lst = list(map(str.rstrip, sys.stdin))
# res = [print(i) for i in lst if not i.strip().startswith('#')]
# OR
# for i in lst:
#     if i.strip().startswith('#'):
#         continue
#     print(i)


# ПАНОРАМНОЕ АГЕНСТВО

# import sys
# SECOND TRY
# # Считываем потоковый ввод данных, убираем переносы и создаем список по ' / '
# lst = [i.strip().split(' / ') for i in sys.stdin]
# # Фильтруем по категориям в lst не доходя до самой категории, чтобы не словить ошибку
# res = filter(lambda x: x[1] == lst[-1][0], lst[:-1])
# # Сортируем по степени достоверности И по алфавиту
# res_sorted = sorted(res, key=lambda x: (float(x[-1]), x))
# # Выводим новости
# print_var = [print(i[0]) for i in res_sorted]
# OR
# from sys import stdin
#
# news = [i.strip().split(' / ') for i in stdin]
# filtered = filter(lambda x: x[1] == news[-1][0], news[:-1])
#
# print(*(i[0] for i in sorted(filtered, key=lambda x: (float(x[2]), x[0]))), sep='\n')


# ЭТО ТОЧНО PYTHON ?

# from datetime import datetime
# import sys
#
# pattern = '%d.%m.%Y'
# data = [datetime.strptime(i.strip(), pattern) for i in sys.stdin]
# set_data = set(data)
#
# if sorted(set_data) == data:
#     print('ASC')
# elif sorted(set_data, reverse=True) == data:
#     print('DESC')
# else:
#     print('MIX')


# ГУРУ ПРОГРЕССИЙ

# import sys
#
# numbers = [int(i) for i in sys.stdin]
# ap = 1
# gp = 1
# for i in range(len(numbers) - 1):
#     if numbers[i + 1] - numbers[i] == 1:
#         ap += 1
#     elif numbers[i + 1] // numbers[i] == 2:
#         gp += 1
# if ap == len(numbers):
#     print('Арифметическая прогрессия')
# elif gp == len(numbers):
#     print('Геометрическая прогрессия')
# else:
#     print('Не прогрессия')


# СОЗДАЕМ ФАЙЛ

# import csv
#
# with open('writing_test.csv', 'w', encoding='utf-8') as csv_file:
#     # создаем writer объект и указываем названия столбцов
#     writer = csv.DictWriter(csv_file, fieldnames=['first_col', 'second_col'])
#     # записываем первую строку с названиями столбцов
#     writer.writeheader()
#     # записываем строку с данными
#     writer.writerow({'first_col': 'value1', 'second_col': 'value2'})
#     s.writerow


# СКИДКИ

# import csv
#
# with open('sales.csv', 'r', encoding='utf-8') as file:
#     # Считываем файл и создаем словарь
#     rows = csv.DictReader(file, delimiter=';', quotechar='"')
#     # Перебираем и сравниваем цены
#     for row in rows:
#         if int(row['old_price']) > int(row['new_price']):
#             print(row['name'])


# СРЕДНЯЯ ЗАРПАЛАТА

# import csv
#
# with open('salary_data.csv', 'r', encoding='utf-8') as file:
#     # Считываем файл в виде словарей
#     rows = csv.DictReader(file, delimiter=';')
#     # Общая сумма зарплат
#     amount = {}
#     # Количество работников
#     count_name = {}
#     # Получаем численные значения
#     for row in rows:
#         amount[row['company_name']] = amount.get(row['company_name'], 0) + int(row['salary'])
#         count_name[row['company_name']] = count_name.get(row['company_name'], 0) + 1
#     # Список компаний с среднеарифметическими значениями зарплат
#     res = {}
#     for k, v in amount.items():
#         res[k] = res.get(k, 0) + amount[k] // count_name[k]
#     # Выводим компании в отсортированном виде по возрастанию зарплат
#     for name in sorted(res, key=lambda x: res[x]):
#         print(name)


# СОРТИРОВКА ПО СТОЛБЦУ

# import csv
#
# col = int(input())
# with open('deniro.csv', 'r', encoding='utf-8') as file:
#     # Создаем итератор при помощи .reader()
#     rows = csv.reader(file)
#     # Печатаем строки сортируя в lambda
#     for row in sorted(rows, key=lambda x: int(x[col - 1]) if col != 1 else x[col - 1]):
#         print(*row, sep=',')


# ФУНКЦИЯ csv_columns()

# import csv
#
#
# def csv_columns(file_name):
#     with open(file_name, 'r', encoding='utf-8') as file:
#         rows = csv.DictReader(file)
#         my_dict = {}
#
#         for row in rows:
#             for k in list(row.keys()):
#                 my_dict[k] = my_dict.get(k, []) + [row[k]]
#         return my_dict
#
#
# print(csv_columns('exam.csv'))
# OR
# import csv
#
# def csv_columns(filename):
#
#     with open(filename, encoding="utf-8") as file_in:
#         rows = list(csv.reader(file_in))
#         return {key: value for key, *value in zip(*rows)}


# ПОПУЛЯРНЫЕ ДОМЕНЫ

# import csv
#
# with open('data.csv', 'r', encoding='utf-8') as file, open('domain_usage.csv', 'w', encoding='utf-8') as new_file:
#     rows = csv.reader(file)
#     # Убираем заголовок
#     a = next(rows)
#     # Получаем список с доменами
#     data = [row[2].split('@')[1] for row in rows]
#     # Создаем словарь и считаем количество доменов
#     my_dict = {}
#     for k in data:
#         my_dict[k] = my_dict.get(k, 0) + 1
#     # Сортируем словарь по количеству доменов и алфавиту
#     my_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: (item[1], item[0]))}
#     # Записали заголовок
#     new_file.write('domain,count\n')
#     # Записываем значения отсортированного словаря
#     for k, v in my_dict.items():
#         new_file.write(f'{k},{str(v)}\n')
# OR
# import csv
#
# with open('data.csv', encoding='utf-8') as csv_file:
#     rows = csv.DictReader(csv_file, delimiter=',')
#     dct = {}
#     for row in rows:
#         domain = row['email'].split('@')[-1]
#         dct[domain] = dct.get(domain, 0) + 1
#
# with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file, delimiter=',')
#     writer.writerow(['domain', 'count'])
#     for row in sorted(dct.items(), key=lambda x: (x[1], x[0])):
#         writer.writerow(row)


# Wi-Fi МОСКВЫ

# import csv
#
# with open('wifi.csv', 'r', encoding='utf-8') as file:
#     # Получаем итератор
#     rows = csv.DictReader(file, delimiter=';')
#     res = {}
#     # Наполняем итоговый словарь
#     for row in rows:
#         res[row['district']] = res.get(row['district'], 0) + int(row['number_of_access_points'])
#     # Сортируем и выводим районы с количеством пользователей
#     for k, v in sorted(res.items(), key=lambda x: (int(-x[1]), x[0])):
#         print(f'{k}: {v}')


# ПОСЛЕДНИЙ ДЕНЬ НА ТИТАНИКЕ

# import csv
#
# with open('titanic.csv', 'r', encoding='utf-8') as file:
#     rows = csv.DictReader(file, delimiter=';')
#     # Получаем всех выживших с возрастом менее 18 лет
#     res = filter(lambda x: int(x['survived']) == 1 and float(x['age']) < 18, rows)
#     # Сортируем
#     res_sort = sorted(res, key=lambda x: x['sex'] == 'female' and float(x['age']) < 18)
#     for row in res_sort:
#         print(row['name'])


# ЛОГ-ФАЙЛ

# from datetime import datetime
# import csv
#
# with open('name_log.csv', 'r', encoding='utf-8') as file:
#     rows = csv.DictReader(file)
#     data = {}
#     # Создаем словарь по емэйл: все изменения ника, если встретится новое имя, произойдет перезапись значения
#     for row in sorted(rows, key=lambda x: datetime.strptime(x['dtime'], '%d/%m/%Y %H:%M')):
#         data[row['email']] = [row['username'], row['email'], row['dtime']]
# # Записываем заголовки, сортируем словарь по емэйлу и записываем
# with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as new_file:
#     writer = csv.writer(new_file, )
#     writer.writerow(['username', 'email', 'dtime'])
#     for i in sorted(data.items(), key=lambda x: x[1][1]):
#         writer.writerow(i[1])
# OR
# import csv
# from datetime import datetime
#
# with open('name_log.csv', encoding='UTF-8') as f:
# 	header, *rows = csv.reader(f)
#
# d = {i[1]:i for i in sorted(rows, key=lambda x: datetime.strptime(x[2], '%d/%m/%Y %H:%M'))}
#
# with open('new_name_log.csv', 'w', encoding='UTF-8', newline='') as f:
# 	w = csv.writer(f)
# 	w.writerow(header)
# 	w.writerows(sorted(d.values(), key=lambda x: x[1]))


# ПРОЩЕ ЧЕМ КАЖЕТСЯ 🌶️

# import csv
#
#
# def condense_csv(file, id_name):
#     with open(file, 'r', encoding='utf-8') as data:
#         rows = csv.reader(data)
#         objects = {}
#         for row in rows:
#             obj_id = row[0]
#             name = row[1]
#             value = row[2]
#             if obj_id not in objects:
#                 objects[obj_id] = {}
#             objects[obj_id][name] = value
#
#     with open('condensed.csv', 'w', encoding='utf-8', newline='') as new_data:
#         writer = csv.writer(new_data)
#         writer.writerow([id_name] + list(objects[next(iter(objects))].keys()))
#         for name, props in objects.items():
#             writer.writerow([name] + list(props.values()))
#
#
# condense_csv('data_csv.csv', 'ID')
# OR
# import csv
#
#
# def condense_csv(filename, id_name):
#     with open(filename, encoding='utf-8') as file:
#         objects = {}
#         # Создаем словарь со словарями
#         for obj, attr, value in csv.reader(file):
#             if obj not in objects:
#                 objects[obj] = {id_name: obj}
#             objects[obj][attr] = value
#     # Записываем словари
#     with open('condensed.csv', 'w', encoding='utf-8') as file:
#         writer = csv.DictWriter(file, fieldnames=objects[obj])
#         writer.writeheader()
#         writer.writerows(objects.values())
#
#
# condense_csv('data_csv.csv', 'id')


# ВОЗРАСТАНИЕ КЛАССОВ 🌶️

# import csv
#
# with open('student_counts.csv', 'r', encoding='utf-8') as file, \
#     open('sorted_student_counts.csv', 'w', encoding='utf-8') as new_file:
#     rows = csv.DictReader(file)
#     title = rows.fieldnames
# # Сортируем заголовок -> 1-А, 1-Б, 2-А...
#     title_sort = sorted(title[1:], key=lambda x: (int(x.split('-')[0]), x.split('-')[1]))
# # Вставялем 'year' в начало т.к. при сортировки его не учитывали
#     title_sort.insert(0, title[0])
#     res = {}
#
#     writer = csv.DictWriter(new_file, fieldnames=title_sort)
# # Записываем заголовок
#     writer.writeheader()
# # Записываем ключи из отсортированного заголовка и записываем значение по этим ключам из общего файла
#     for i in rows:
#         for j in title_sort:
#             res[j] = i[j]
#         writer.writerow(res)


# ГОЛОДНЫЙ СТУДЕНТ 🌶️

# import csv
#
# with open('prices.csv', 'r', encoding='utf-8') as file:
#     rows = list(csv.DictReader(file, delimiter=';'))
#     shop = {}
#     # Добавляем название магазина и самый дешевый товар
#     for row in rows:
#         shop[row['Магазин']] = sorted(list(row.items())[1:], key=lambda x: int(x[1]))[0]
#     # Выбираем из данных предложений самый дешевый товар, самый меньший в лексинографическом порядке
#     buy = sorted(shop.items(), key=lambda x: (int(x[1][1]), x[1][0], x[0]))[0]
#     # Выводим название магазина и цену
#     print(f'{buy[1][0]}: {buy[0]}')


# JSON

# import json
#
# countries = {'Monaco': 'Monaco', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi', 'Kazakhstan': 'Nur-Sultan',
#              'Mali': 'Bamako', 'Colombia': 'Bogota', 'Finland': 'Helsinki', 'Costa Rica': 'San Jose',
#              'Cuba': 'Havana', 'France': 'Paris', 'Gabon': 'Libreville', 'Liberia': 'Monrovia',
#              'Angola': 'Luanda', 'India': 'New Delhi', 'Canada': 'Ottawa', 'Australia': 'Canberra'}
# print(json.dumps(countries, indent='   ', sort_keys=True, separators=(',', ' - ')))


# ЗАПИСЬ JSON

# import json
#
# club1 = {"name": "FC Byern Munchen", "country": "Germany", "founded": 1900,
#          "trainer": "Julian Nagelsmann", "goalkeeper": "M. Neuer", "league_position": 1}
#
# club2 = {"name": "FC Barcelona", "country": "Spain", "founded": 1899,
#          "trainer": "Xavier Creus", "goalkeeper": "M. Ter Stegen", "league_position": 7}
#
# club3 = {"name": "FC Manchester United", "country": "England", "founded": 1878,
#          "trainer": "Michael Carrick", "goalkeeper": "D. De Gea", "league_position": 8}
# my_list = [club1, club2, club3]
# with open('data.json', 'w', encoding='utf-8') as file:
#     json.dump(my_list, file, indent=3)


# КИРИЛЛИЧЕСКИЕ СИМВОЛЫ

# import json
#
# specs = {
#     'Модель': 'AMD Ryzen 5 5600G',
#     'Год релиза': 2021,
#     'Сокет': 'AM4',
#     'Техпроцесс': '7 нм',
#     'Ядро': 'Cezanne',
#     'Объем кэша L2': '3 МБ',
#     'Объем кэша L3': '16 МБ',
#     'Базовая частота': '3900 МГц'
# }
#
# specs_json = json.dumps(specs, indent=3, ensure_ascii=False)
#
# print(specs_json)


# ФУНКЦИЯ is_correct_json()

# import json
#
#
# def is_correct_json(data):
#     try:
#         if json.loads(data):
#             return True
#     except json.decoder.JSONDecodeError:
#         return False


# print(is_correct_json('number = 17'))


# ЭЛЕМЕНТЫ JSON

# import sys
# import json
#
# data = json.loads(sys.stdin.read())
# for k, v in data.items():
#     if type(v) is list:
#         print(k, end=': ')
#         print(*v, sep=', ')
#     else:
#         print(f'{k}: {v}')


# РАЗНЫЕ ТИПЫ

# import json
#
# with open('data.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
#     result = []
#
#     for item in data:
#         if type(item) == bool:
#             result.append(not item)
#         elif type(item) == str:
#             result.append(item + '!')
#         elif type(item) == int:
#             result.append(item + 1)
#         elif type(item) == list:
#             result.append(item * 2)
#         elif type(item) == dict:
#             item["newkey"] = None
#             result.append(item)
#
# with open('updated_data.json', 'w', encoding='utf-8') as new_file:
#     json.dump(result, new_file, indent=3)


# ОБЪЕДИНЕНИЕ ОБЪЕКТОВ

# import json
#
# with open('data1.json', 'r', encoding='utf-8') as first, \
#     open('data2.json', 'r', encoding='utf-8') as second:
#     first = json.load(first)
#     second = json.load(second)
#     res = first | second
# with open('data_merge.json', 'w', encoding='utf-8') as new_file:
#     json.dump(res, new_file, indent=3)


# ВОССТАНОВЛЕНИЕ НЕДОСТАЮЩИХ КЛЮЧЕЙ

# with open('people.json', 'r', encoding='utf-8') as file:
#     # Считали джейсонину
#     data = json.load(file)
#     # Получили длины всех словарей
#     len_dict = [len(i.keys()) for i in data]
#     # Получили индекс самого длинного словаря
#     index = len_dict.index(max(len_dict))
#     # Получили сам словарь -> ЭТАЛОН
#     max_dict = data[index]
#     result = []
#     # Пробегаемся по всем словарям из списка
#     for i in data:
#         # Пробегаемся по всем ключам из эталона и записываем эти ключ: None в случае отствутствия в i словаре
#         for k in max_dict:
#             i.setdefault(k, None)
#         result.append(i)
#
# with open('updated_people.json', 'w', encoding='utf-8') as new_file:
#     # Записываем список словарей в джейсонину
#     json.dump(result, new_file, indent=3)
# OR
# import json
#
# with open('people.json', encoding='utf8') as fi, open('updated_people.json', 'w') as fo:
#     people = json.load(fi)
#     # Создаем словарь со всеми найденными ключами и задаем значение None
#     d = {k: None for i in people for k in i.keys()}
#     # Делаем update при помощи | и получаем изначальные значения из файла
#     json.dump([d | i for i in people], fo)


# Я ИСПОВЕДУЮ Python, А ТЫ ?

# import json
#
# with open('countries.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
#     result = {}
#     # Создаем ключ(религию): значение(список стран)
#     for i in data:
#         result.setdefault(i['religion'], []).append(i['country'])
#
# with open('religion.json', 'w', encoding='utf-8') as new_file:
#     json.dump(result, new_file, indent=3)


# СПОРТИВНЫЕ ПЛОЩАДКИ

# import csv
# import json
#
# with open('playgrounds.csv', 'r', encoding='utf-8') as file:
#     rows = csv.reader(file, delimiter=';')
#     next(rows)
#     result = {}
#
#     for obj, area, region, adres in rows:
#         # Создаем округа со словарями
#         result.setdefault(area, {})
#         # В округ добавляет словарь с регионом и списком адресов
#         result[area].setdefault(region, []).append(adres)
#
# with open('addresses.json', 'w', encoding='utf-8') as new_file:
#     json.dump(result, new_file, indent=3, ensure_ascii=False)


# СТУДЕНТЫ КУРСА

# import json
# import csv
#
# with open('students.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
#     # Фильтруем исходный файл
#     new_data = list(filter(lambda x: int(x['age']) >= 18 and int(x['progress']) >= 75, data))
#     # Создаем словарь с нужным ключом и значением
#     result = {i['name']: i['phone'] for i in new_data}
#     # Сортируем ключи по алфавиту
#     result = sorted(result.items(), key=lambda x: x[0])
#
# with open('data.csv', 'w', encoding='utf-8', newline='') as new_file:
#     writer = csv.writer(new_file)
#     # Записываем заголовок
#     writer.writerow(['name', 'phone'])
#     # Записываем имя и телефон
#     for name, phone in result:
#         writer.writerow([name, phone])


# БАССЕЙНЫ

# import json
# from datetime import datetime
#
# with open('pools.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
#     # Фильтруем по времени, чтобы бассейн работал в момент времени 10:00-12:00
#     data = filter(lambda x: datetime.strptime(x['WorkingHoursSummer']['Понедельник'].split('-')[0], '%H:%M').time() <=
#                          datetime.strptime('10:00', '%H:%M').time()
#                          and datetime.strptime(x['WorkingHoursSummer']['Понедельник'].split('-')[1], '%H:%M').time() >=
#                          datetime.strptime('12:00', '%H:%M').time(), data)
#     # Сортируем по длине и по ширине если встретился такой же длины
#     data_sort = sorted(data, key=lambda x: (int(x['DimensionsSummer']['Length']),
#                                             (int(x['DimensionsSummer']['Width']))), reverse=True)
#     # Выводим самый длинный или самый длинный и широкий бассейн
#     print(f'''{data_sort[0]["DimensionsSummer"]["Length"]}x{data_sort[0]["DimensionsSummer"]["Width"]}
# {data_sort[0]["Address"]}''')


# РЕЗУЛЬТАТЫ ЭКЗАМЕНА

# import csv
# import json
# from datetime import datetime
#
#
# with open('exam_results.csv', 'r', encoding='utf-8') as file:
#     rows = csv.DictReader(file)
#     next(rows)
#     res = {}
#     rows = sorted(rows, key=lambda x: datetime.strptime(x['date_and_time'], '%Y-%m-%d %H:%M:%S'))
#
#     for row in rows:
#         res.setdefault((row['email'], row['name'], row['surname']), {}).setdefault(int(row['score']), []). \
#             append(datetime.strptime(row['date_and_time'], '%Y-%m-%d %H:%M:%S'))
#     new_list = []
#     new = {}
#     for k, v in res.items():
#         max_key = max(v.keys())
#         new['name'] = k[1]
#         new['surname'] = k[2]
#         new['best_score'] = max_key
#         new['date_and_time'] = str(v[max_key][-1])
#         new['email'] = k[0]
#         new_list.append(new)
#         new = {}
#     new_list = sorted(new_list, key=lambda x: x['email'])
#
# with open('best_scores.json', 'w', encoding='utf-8') as new_file:
#     json.dump(new_list, new_file, indent=3)
# OR
# import json, csv
#
# with open('exam_results.csv', encoding='utf8') as file:
#     head, *rows = list(csv.reader(file, delimiter=','))
#
# rows.sort(key=lambda x: x[2])  # sort by score
# rows.sort(key=lambda x: x[3])  # sort by time
# rows.sort(key=lambda x: x[4])  # sort by email
#
# data = {}
# for name, surname, score, date_and_time, email in rows:
#     data[email] = {'name': name, 'surname': surname, 'best_score': int(score),
#                    'date_and_time': date_and_time, 'email': email}
#
# with open('best_scores.json', 'w', encoding='utf8') as file:
#     json.dump(list(data.values()), file, indent=3)


# ОБЩЕСТВЕННОЕ ПИТАНИЕ-1

# import json
#
#
# with open('food_services.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
#     filter_data = filter(lambda x: x['IsNetObject'] == 'да', data)
#     res = {}
#     shop = {}
#     for i in data:
#         res[i['District']] = res.get(i['District'], 0) + 1
#
#     for j in filter_data:
#         shop[j['OperatingCompany']] = shop.get(j['OperatingCompany'], 0) + 1
#
#     region_popular = max(res.items(), key=lambda x: x[1])
#     shop_popular = max(shop.items(), key=lambda x: x[1])
#     print(f'''{region_popular[0]}: {region_popular[1]}
# {shop_popular[0]}: {shop_popular[1]}''')
# OR
# import json
#
# with open("food_services.json", "r", encoding="utf-8") as f:
#     cafes = list(json.load(f))
#     dst = [i["District"] for i in cafes]
#     cmp = [i["OperatingCompany"] for i in cafes if i["OperatingCompany"]]
#     mfd, mfc = max(set(dst), key=dst.count), max(set(cmp), key=cmp.count)
#
#     print(f"{mfd}: {dst.count(mfd)}\n{mfc}: {cmp.count(mfc)}")


# ОБЩЕСТВЕННОЕ ПИТАНИЕ-2

# import json
#
# # name, IsNetObject, OperatingCompany, TypeObject, AdmArea, District, Address, SeatsCount
# with open('food_services.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
#     res = {}
#     data = sorted(data, key=lambda x: x['SeatsCount'])
#     for i in data:
#         res.setdefault(i['TypeObject'], {})
#         res[i['TypeObject']] = {i['Name']: i['SeatsCount']}
#     res = sorted(res.items())
#     for k, v in res:
#         for i, j in v.items():
#             print(f'{k}: {i}, {j}')
