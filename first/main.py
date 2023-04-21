# БАНКОВСКАЯ КАРТА
# def hide_card(card):
#     return '*' * 12 + card.replace(' ', '')[-4:]
#
#
# card = '905 678123 45612 56'
#
# print(hide_card(card))


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
#                             datetime.strptime('10:00', '%H:%M').time()
#                             and datetime.strptime(x['WorkingHoursSummer']['Понедельник'].split('-')[1],
#                                                   '%H:%M').time() >=
#                             datetime.strptime('12:00', '%H:%M').time(), data)
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


# РАБОТА С ZIP ФАЙЛАМ

# КОЛИЧЕСТВО ФАЙЛОВ

# from zipfile import ZipFile
#
# with ZipFile('workbook.zip') as zip_file:
#     info = zip_file.infolist()
#     # /is_dir() проверяет это файл или папка
#     print(len([i.filename for i in info if i.is_dir() is not True]))


# ОБЪЕМ ФАЙЛОВ

# from zipfile import ZipFile
#
# with ZipFile('workbook.zip') as zip_file:
#     info = zip_file.infolist()
#     size_bef = sum([i.file_size for i in info])
#     size_aft = sum([i.compress_size for i in info])
#     print(f'''Объем исходных файлов: {size_bef} байт(а)
# Объем сжатых файлов: {size_aft} байт(а)''')


# НАИЛУЧШИЙ ПОКАЗАТЕЛЬ

# from zipfile import ZipFile
#
# with ZipFile('workbook.zip') as zip_file:
#     info = zip_file.infolist()
#     # Получили список названий файлов
#     name = [i.filename for i in info if i.is_dir() is not True]
#     # Получили список степень сжатия файлов
#     size = [(i.compress_size / i.file_size) * 100 for i in info if i.is_dir() is not True]
#     # Объединили списки
#     all = list(zip(name, size))
#     # Отсортировали по сжатию
#     all = sorted(all, key=lambda x: x[1])
#     # Выводим название файла
#     print(list(all)[0][0].split('/')[1])
# OR
# from zipfile import ZipFile
#
# with ZipFile("workbook.zip") as zip_file:
#     filelist = zip_file.infolist()
#     t = ((f.filename, f.compress_size/f.file_size) for f in filelist
#          if f.file_size != 0)
#     print(min(t, key=lambda x: x[1])[0].split("/")[-1])


# ИЗБРАННЫЕ

# from zipfile import ZipFile
# from datetime import datetime
#
# with ZipFile('workbook.zip') as zip_file:
#     data = datetime.strptime('2021-11-30 14:22:00', '%Y-%m-%d %H:%M:%S')
#     info = zip_file.infolist()
#     favorit = [i.filename.split('/') for i in info if datetime(*i.date_time) >= data and i.is_dir() is not True]
#     favorit_sort = [print(i[-1]) for i in sorted(favorit, key=lambda x: x[-1])]


# ФОРМАТИРОВАННЫЙ ВЫВОД

# from zipfile import ZipFile
# from datetime import datetime
#
# with ZipFile('workbook.zip') as zip_file:
#     info = zip_file.infolist()
#     info = sorted(info, key=lambda x: x.filename.split('/')[-1])
#     for i in info:
#         if not i.is_dir():
#             print(f'''{i.filename.split('/')[-1]}
#   Дата модификации файла: {datetime(*i.date_time)}
#   Объем исходного файла: {i.file_size} байт(а)
#   Объем сжатого файла: {i.compress_size} байт(а)''')
#             print()


# СОЗДАНИЕ АРХИВА

# from zipfile import ZipFile
#
# file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
#               'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
#               'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']
# Создаем архив
# with ZipFile('files.zip', 'w') as zip_file:
#     Записываем файлы
#     file = [zip_file.write(i) for i in file_names]


# ЗАПИСЬ В АРХИВ

# from zipfile import ZipFile
# import os.path
#

# file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
#               'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
#               'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']
# new_file_names = [i for i in file_names if os.path.getsize(i) <= 100]
# with ZipFile('files.zip', 'a') as zip_file:
#     file = [zip_file.write(i) for i in new_file_names]


# ФУНКЦИЯ extract_this()

# from zipfile import ZipFile
#
#
# def extract_this(zip_name, *args):
#     with ZipFile(zip_name) as zip_file:
#         info = zip_file.infolist()
#         info = [i.filename for i in info if not i.is_dir()]
#         if args:
#             for i in info:
#                 if i.split('/')[-1] in args:
#                     zip_file.extract(i)
#         else:
#             zip_file.extractall()
#
#
# extract_this('workbook.zip', 'earth.jpg', 'exam.txt')
# OR
# from zipfile import ZipFile
#
#
# def extract_this(zip_name: str, *args):
#     if not args:
#         args = None
#     with ZipFile(zip_name) as zf:
#         zf.extractall(members=args)


# ОДИНОКАЯ ФУНКЦИЯ

# import pickle
# import sys
#
# file_name, *data = list(map(str.strip, sys.stdin))
# with open(file_name, 'rb') as file:
#     real_func = pickle.load(file)
#
# print(real_func(*data))


# ТЫ НЕ ПРОЙДЕШЬ

# import pickle
#
#
# def filter_dump(name_pickl, some_list, type_data):
#     with open(name_pickl, 'wb') as file:
#         a = [i for i in some_list if type(i) == type_data]
#         pickle.dump(a, file)
#
# filter_dump('numbers.pkl', [1, '2', 3, 4, '5'], int)


# КОНТРОЛЬНАЯ СУММА

# import pickle
#
# file, num = input(), int(input())
# with open(file, 'rb') as data:
#     info = pickle.load(data)
#     change = [i for i in info if type(i) == int]
#     check = sum(change) if type(info) == dict else max(change, default = 0)*min(change, default = 0)
#     print(['Контрольные суммы не совпадают', 'Контрольные суммы совпадают'][num == check])


# ШАХМАТЫ БЫЛИ ЛУЧШЕ🌶️

# from zipfile import ZipFile
# import json
#
#
# def is_correct_json(data):
#     try:
#         a = json.loads(data)
#         if a:
#             return a
#     except json.decoder.JSONDecodeError:
#         return False
#
#
# new_name = []
# with ZipFile('data.zip') as zip_file:
#     # Получаем пути к файлам
#     name = [i.filename for i in zip_file.infolist() if i.is_dir() is not True]
#     for i in name:
#         # Попробуй прочитать файл и если он джейсонина, добавляем в список
#         with zip_file.open(i) as file:
#             try:
#                 a = file.read().decode('utf-8')
#                 func = is_correct_json(a)
#                 if func:
#                     new_name.append(func)
#             except:
#                 continue
# # Фильтруем по футбольному клубу
# new_name = filter(lambda x: x['team'] == 'Arsenal', new_name)
# # Выводим имя и фамилию
# out = [print(i['first_name'], i['last_name']) for i in
#        sorted(new_name, key=lambda x: (x['first_name'], x['last_name']))]


# СТРУКТУРА АРХИВА🌶️🌶️

# from zipfile import ZipFile
#
#
# def size_def(data):
#     for unit in ('B', 'KB', 'MB', 'GB'):
#         if data < 1024:
#             return f'{round(data)} {unit}'
#         data /= 1024
#
#
# with ZipFile('desktop.zip') as zip_file:
#     info = zip_file.infolist()
#     for i in info:
#         if i.is_dir():
#             i = i.filename
#             print(f"""{'  ' * (len(i[:len(i) - 1].split('/')) - 1)}{i.split('/')[-2]}""")
#         else:
#             print(f"""{'  ' * (len(i.filename.split('/')) - 1)}{i.filename.split('/')[-1]} {size_def(i.file_size)}""")


# Я И САМ СВОЕГО РОДА ПЕРЕВОДЧИК

# import string
#
# alphabet = string.ascii_lowercase
# txt = input()
# translate = input().lower()
# my_dict = {}
# for i in range(len(txt)):
#     my_dict[alphabet[i]] = txt[i]
# print(my_dict)
# answer = translate.maketrans(my_dict)
# print(translate.translate(answer))
# OR
# from string import ascii_letters
#
# translator = str.maketrans(ascii_letters, input() * 2)
#
# print(input().translate(translator))
# OR
# from string import ascii_lowercase as lc
#
# tbl = str.maketrans(lc, input())
# print(input().lower().translate(tbl))


# 6.4.1 numedtuple()

# from collections import namedtuple
#
# Fruit = namedtuple('Fruit', ('name', 'color', 'vitamins'))


# 6.4.2

# from collections import namedtuple
#
# Game = namedtuple('Game', 'name developer publisher')
#
# ExtendedGame = namedtuple('ExtendedGame', [*Game._fields, 'release_date', 'price'])


# 6.4.3

# from collections import namedtuple
# import pickle
#
# Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])
#
# with open('data.pkl', 'rb') as file:
#     reader = pickle.load(file)
# for i in reader:
#     for j in zip(Animal._fields, i):
#         print(f'{j[0]}: {j[1]}')
#     print()


# 6.4.4

# from collections import namedtuple
#
# User = namedtuple('User', ['name', 'surname', 'email', 'plan'])
#
# users = [User('Mary', 'Griffin', 'sonnen@yahoo.com', 'Basic'),
#          User('Brenda', 'Young', 'retoh@outlook.com', 'Silver'),
#          User('Kathleen', 'Lyons', 'balchen@att.net', 'Gold'),
#          User('Pamela', 'Hicks', 'corrada@sbcglobal.net', 'Silver'),
#          User('William', 'Townsend', 'kosact@verizon.net', 'Gold'),
#          User('Clayton', 'Morris', 'berserk@yahoo.com', 'Silver'),
#          User('Dorothy', 'Dennis', 'sequin@live.com', 'Gold'),
#          User('Tyler', 'Walker', 'noahb@comcast.net', 'Basic'),
#          User('Joseph', 'Moore', 'ylchang@sbcglobal.net', 'Silver'),
#          User('Kenneth', 'Richardson', 'tbusch@me.com', 'Bronze'),
#          User('Stephanie', 'Bush', 'neuffer@live.com', 'Gold'),
#          User('Gregory', 'Hughes', 'juliano@att.net', 'Basic'),
#          User('Tracy', 'Wallace', 'sblack@me.com', 'Silver'),
#          User('Russell', 'Smith', 'isaacson@comcast.net', 'Bronze'),
#          User('Megan', 'Patterson', 'hoangle@outlook.com', 'Basic')]
# Сортируем по подписке при помощи индекса
# res = sorted(users, key=lambda x: (('Gold', 'Silver', 'Bronze', 'Basic').index(x.plan), x.email))
# for i in res:
#     print(f'''{i.name} {i.surname}
#   Email: {i.email}
#   Plan: {i.plan}'''
#     print()


# ВЫ КТО ТАКИЕ? Я ВАС НЕ ЗВАЛ

# from datetime import datetime
# import csv
#
# with open('meetings.csv', 'r', encoding='utf-8') as file:
#     rows = csv.reader(file)
#     title = next(file)
#     for row in sorted(rows, key=lambda x: (datetime.strptime(f'{x[-2]}{x[-1]}', '%d.%m.%Y%H:%M'))):
#         print(row[0], row[1])
# OR
# from collections import namedtuple
# import csv
# from datetime import datetime
#
# with open('meetings.csv', encoding='utf-8') as inf:
#     rows = csv.reader(inf)
#     title = next(rows)
#     Friend = namedtuple('Friend', title)
#     friends = [Friend(*row) for row in rows]
# schedule = sorted(friends, key=lambda x: datetime.strptime(f'{x.meeting_date} {x.meeting_time}', '%d.%m.%Y %H:%M'))
# print(*[f'{x.surname} {x.name}' for x in schedule], sep='\n')


# way = 'DDUDUU'
# ground_level = 0
# amount = 0
#
# for i in way:
#     if i == 'U':
#         ground_level += 1
#     else:
#         ground_level -= 1
#     if i == 'U' and ground_level == 0:
#         amount += 1
#
# print(amount)


# 6.5.1

# from collections import defaultdict
#
# data = [('Books', 1343), ('Books', 1166), ('Merch', 616), ('Courses', 966), ('Merch', 1145), ('Courses', 1061),
#         ('Books', 848), ('Courses', 964), ('Tutorials', 832), ('Merch', 642), ('Books', 815), ('Tutorials', 1041),
#         ('Books', 1218), ('Tutorials', 880), ('Books', 1003), ('Merch', 951), ('Books', 920), ('Merch', 729),
#         ('Tutorials', 977), ('Books', 656)]
#
# my_dict = defaultdict(int)
# for k, v in data:
#     my_dict[k] += v
# for k, v in sorted(my_dict.items()):
#     print(f'{k}: ${v}')


# 6.5.2

# from collections import defaultdict
#
# staff = [('Sales', 'Robert Barnes'), ('Developing', 'Thomas Porter'), ('Accounting', 'James Wilkins'),
#          ('Sales', 'Connie Reid'), ('Accounting', 'Brenda Davis'), ('Developing', 'Miguel Norris'),
#          ('Accounting', 'Linda Hudson'), ('Developing', 'Deborah George'), ('Developing', 'Nicole Watts'),
#          ('Marketing', 'Billy Lloyd'), ('Sales', 'Charlotte Cox'), ('Marketing', 'Bernice Ramos'),
#          ('Sales', 'Jose Taylor'), ('Sales', 'Katie Warner'), ('Accounting', 'Steven Diaz'),
#          ('Accounting', 'Kimberly Reynolds'), ('Accounting', 'John Watts'), ('Accounting', 'Dale Houston'),
#          ('Developing', 'Arlene Gibson'), ('Marketing', 'Joyce Lawrence'), ('Accounting', 'Rosemary Garcia'),
#          ('Marketing', 'Ralph Morgan'), ('Marketing', 'Sam Davis'), ('Marketing', 'Gail Hill'),
#          ('Accounting', 'Michelle Wright'), ('Accounting', 'Casey Jenkins'), ('Sales', 'Evelyn Martin'),
#          ('Accounting', 'Aaron Ferguson'), ('Marketing', 'Andrew Clark'), ('Marketing', 'John Gonzalez'),
#          ('Developing', 'Wilma Woods'), ('Sales', 'Marie Cooper'), ('Accounting', 'Kay Scott'),
#          ('Sales', 'Gladys Taylor'), ('Accounting', 'Ann Bell'), ('Accounting', 'Craig Wood'),
#          ('Accounting', 'Gloria Higgins'), ('Marketing', 'Mario Reynolds'), ('Marketing', 'Helen Taylor'),
#          ('Marketing', 'Mary King'), ('Accounting', 'Jane Jackson'), ('Marketing', 'Carol Peters'),
#          ('Sales', 'Alicia Mendoza'), ('Accounting', 'Edna Cunningham'), ('Developing', 'Joyce Rivera'),
#          ('Sales', 'Joseph Lee'), ('Sales', 'John White'), ('Marketing', 'Charles Bailey'),
#          ('Sales', 'Chester Fernandez'), ('Sales', 'John Washington')]
# my_dict = defaultdict(int)
# for k, v in staff:
#     my_dict[k] += 1
# for i in sorted(my_dict.items()):
#     print(f'{i[0]}: {i[1]}')


# 6.5.3

# from collections import defaultdict
#
# staff_broken = [('Developing', 'Miguel Norris'), ('Sales', 'Connie Reid'), ('Sales', 'Joseph Lee'),
#                 ('Marketing', 'Carol Peters'), ('Accounting', 'Linda Hudson'), ('Accounting', 'Ann Bell'),
#                 ('Marketing', 'Ralph Morgan'), ('Accounting', 'Gloria Higgins'), ('Developing', 'Wilma Woods'),
#                 ('Developing', 'Wilma Woods'), ('Marketing', 'Bernice Ramos'), ('Marketing', 'Joyce Lawrence'),
#                 ('Accounting', 'Craig Wood'), ('Developing', 'Nicole Watts'), ('Sales', 'Jose Taylor'),
#                 ('Accounting', 'Linda Hudson'), ('Accounting', 'Edna Cunningham'), ('Sales', 'Jose Taylor'),
#                 ('Marketing', 'Helen Taylor'), ('Accounting', 'Kimberly Reynolds'), ('Marketing', 'Mary King'),
#                 ('Sales', 'Joseph Lee'), ('Accounting', 'Gloria Higgins'), ('Marketing', 'Andrew Clark'),
#                 ('Accounting', 'John Watts'), ('Accounting', 'Rosemary Garcia'), ('Accounting', 'Steven Diaz'),
#                 ('Marketing', 'Mary King'), ('Sales', 'Gladys Taylor'), ('Developing', 'Thomas Porter'),
#                 ('Accounting', 'Brenda Davis'), ('Sales', 'Connie Reid'), ('Sales', 'Alicia Mendoza'),
#                 ('Marketing', 'Mario Reynolds'), ('Sales', 'John White'), ('Developing', 'Joyce Rivera'),
#                 ('Accounting', 'Steven Diaz'), ('Developing', 'Arlene Gibson'), ('Sales', 'Robert Barnes'),
#                 ('Sales', 'Charlotte Cox'), ('Accounting', 'Craig Wood'), ('Marketing', 'Carol Peters'),
#                 ('Marketing', 'Ralph Morgan'), ('Accounting', 'Kay Scott'), ('Sales', 'Evelyn Martin'),
#                 ('Marketing', 'Billy Lloyd'), ('Sales', 'Gladys Taylor'), ('Developing', 'Deborah George'),
#                 ('Sales', 'Charlotte Cox'), ('Marketing', 'Sam Davis'), ('Sales', 'John White'),
#                 ('Sales', 'Marie Cooper'), ('Marketing', 'John Gonzalez'), ('Sales', 'John Washington'),
#                 ('Sales', 'Chester Fernandez'), ('Sales', 'Alicia Mendoza'), ('Sales', 'Katie Warner'),
#                 ('Accounting', 'Jane Jackson'), ('Sales', 'Chester Fernandez'), ('Marketing', 'Charles Bailey'),
#                 ('Marketing', 'Gail Hill'), ('Accounting', 'Casey Jenkins'), ('Accounting', 'James Wilkins'),
#                 ('Accounting', 'Casey Jenkins'), ('Marketing', 'Mario Reynolds'), ('Accounting', 'Aaron Ferguson'),
#                 ('Accounting', 'Kimberly Reynolds'), ('Sales', 'Robert Barnes'), ('Accounting', 'Aaron Ferguson'),
#                 ('Accounting', 'Jane Jackson'), ('Developing', 'Deborah George'), ('Accounting', 'Michelle Wright'),
#                 ('Accounting', 'Dale Houston')]
# my_dict = defaultdict(set)
# for k, v in staff_broken:
#     my_dict[k].add(v)
# for k, v in sorted(my_dict.items()):
#     print(f'{k}: {", ".join(sorted(v))}')


# ФУНКЦИЯ wins():

# from collections import defaultdict
#
#
# def wins(lst):
#     answer = defaultdict(set)
#     for k, v in lst:
#         answer[k].add(v)
#     return answer
#
#
# # Вызов функции
# result = wins([('Тимур', 'Артур'), ('Тимур', 'Дима'), ('Дима', 'Артур')])
# # Выводим ответ
# for winner, losers in sorted(result.items()):
#     print(winner, '->', *sorted(losers))


# ФУНКЦИЯ flip_dict()

# from collections import defaultdict
#
#
# def flip_dict(my_dict):
#     result = defaultdict(list)
#     for k, v in my_dict.items():
#         for i in v:
#             result[i].append(k)
#     return result
#
#
# print(flip_dict({'a': [1, 2], 'b': [3, 1], 'c': [2]}))


# ФУНКЦИЯ best_sender()

# from collections import defaultdict
#
#
# def best_sender(messages, senders):
#     result = defaultdict(list)
#     for k, v in zip(senders, messages):
#         result[k].append(len(v.split()))
#     return max(result.items(), key=lambda x: (sum(x[1], len(x[0]))))[0]
#
#
# messages = ['How is Stepik for everyone', 'Stepik is useful for practice']
# senders = ['Bob', 'Charlie']
#
# print(best_sender(messages, senders))


# 6.6.1

# from collections import OrderedDict
#
# data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе',
#                     'AdmArea': 'Центральный административный округ', 'District': 'район Арбат',
#                     'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})
# print(OrderedDict(reversed(data.items())))


# 6.6.2

# from collections import OrderedDict
#
# data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе',
#                     'AdmArea': 'Центральный административный округ', 'District': 'район Арбат',
#                     'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})
# new_data = OrderedDict()
# for i in range(len(data) // 2):
#     k, v = data.popitem(last=False)
#     new_data[k] = v
#     k, v = data.popitem()
#     new_data[k] = v
# print(new_data)
# OR
# from collections import OrderedDict
#
# data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе',
#                     'AdmArea': 'Центральный административный округ', 'District': 'район Арбат',
#                     'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})
#
# new = OrderedDict()
# while data:
#     new.setdefault(*data.popitem(last=(len(new) % 2)))
#
# print(new)


# 6.6.3

# from collections import OrderedDict
#
# data = OrderedDict(
#     {'Law & Order': 1990, 'The Practice': 1997, 'Six Feet Under': 2001, 'Joan of Arcadia': 2003, 'The West Wing': 1999,
#      'Deadwood': 2004, 'The Sopranos': 1999, 'Boston Legal': 2004, 'ER': 1994, 'Friday Night Lights': 2006, '24': 2001,
#      'Heroes': 2006, 'Lost': 2004, 'Dexter': 2006, 'Damages': 2007, 'Big Love': 2006, 'House': 2004,
#      'Downton Abbey': 2010, "Grey's Anatomy": 2005, 'Homeland': 2011, 'Breaking Bad': 2008, 'Game of Thrones': 2011,
#      'CSI: Crime Scene Investigations': 2000, 'Boardwalk Empire': 2010, 'True Blood': 2008, 'House of Cards': 2013,
#      'True Detective': 2014})
# data.sorted_keys = lambda reverse=False: sorted(data.keys(), reverse=reverse)
# data.sorted_values = lambda reverse=False: sorted(data.values(), reverse=reverse)
# print(data.sorted_values())

# ФУНКЦИЯ custom_sort() 🌶️

# from collections import OrderedDict
#
#
# def custom_sort(ordered_dict, by_values=False):
#     if by_values:
#         for k, v in sorted(ordered_dict.items(), key=lambda x: x[1]):
#             ordered_dict.move_to_end(k, v)
#     else:
#         for k, v in sorted(ordered_dict.items()):
#             ordered_dict.move_to_end(k, v)
#
#
# data1 = OrderedDict(e=11, b=22, a=99, g=33, c=33, d=33, h=99, f=77, i=88, k=44)
# custom_sort(data1, by_values=False)
#
# print(*data1.items())


# 6.7.1

# from collections import Counter
#
# files = ['emoji_smile.jpeg', 'city-of-the-sun.mp3', 'dhook_hw.json', 'sample.xml',
#          'teamspeak3.exe', 'project_module3.py', 'math_lesson3.mp4', 'old_memories.mp4',
#          'spiritfarer.exe', 'backups.json', 'python_for_beg1.mp4', 'emoji_angry.jpeg',
#          'exam_results.csv', 'project_main.py', 'classes.csv', 'plants.xml',
#          'cant-help-myself.mp3', 'microsoft_edge.exe', 'steam.exe', 'math_lesson4.mp4',
#          'city.jpeg', 'bad-disease.mp3', 'beauty.jpeg', 'hollow_knight_silksong.exe',
#          'whatsapp.exe', 'photoshop.exe', 'telegram.exe', 'yandex_browser.exe',
#          'math_lesson7.mp4', 'students.csv', 'emojis.zip', '7z.zip',
#          'bones.mp3', 'python3.zip', 'dhook_lsns.json', 'carl_backups.json',
#          'forest.jpeg', 'python_for_pro8.mp4', 'yandexdisc.exe', 'but-you.mp3',
#          'project_module1.py', 'nothing.xml', 'flowers.jpeg', 'grades.csv',
#          'nvidia_gf.exe', 'small_txt.zip', 'project_module2.py', 'tab.csv',
#          'note.xml', 'sony_vegas11.exe', 'friends.jpeg', 'data.pkl']
#
# data = Counter([i.split('.')[1] for i in files])
# for k, v in sorted(data.items()):
#     print(f'{k}: {v}')


# ФУНКЦИЯ count_occurences()

# from collections import Counter
#
#
# def count_occurences(word, words):
#     words = words.lower().split()
#     word = word.lower()
#     return Counter(words)[word]
#
#
# word = 'python'
# words = 'Python Conferences python training python events'

# print(count_occurences(word, words))


# НЕ ПОЛЕНИМСЯ И ЗАПИШЕМ

# from collections import Counter
#
# txt = input().split(',')
# # Считаем одинаковые записи и выводим
# for k, v in sorted(Counter(txt).items()):
#     print(f'{k}: {v}')

# А СКОЛЬКО СТОИТ КУРС?

# from collections import Counter
#
#
# def uc(txt):
#     """
#         Функция должна определять, число символа по юникоду.
#         Далее все найденные числа суммируем.
#     """
#     return sum([ord(i) for i in txt if i.replace(' ', '')])
#
#
# # Создали счетчик
# txt = Counter(sorted(input().split(',')))
# # Максимальная длина товара -> для рассчета пробелов при выводе
# max_len = len(max(txt, key=len))
# # Выводим с учетом макс. длины слова
# for k, v in txt.items():
#     # print(f'{k + (" " * (max_len - len(k)))}: {uc(k)} UC x {v} = {uc(k) * v} UC')
# # OR
#     print(f'{k.ljust(max_len, " ")}: {uc(k)} UC x {v} = {uc(k) * v} UC')


# THE ZEN OF PYTHON

# from string import ascii_lowercase
# from collections import Counter
#
# with open('pythonzen.txt', 'r', encoding='utf-8') as file:
#     words = file.read().lower()
#     new_words = list(filter(str.strip, words))
#     result = []
#     for word in sorted(new_words):
#         if word in ascii_lowercase:
#             result.append(word)
#     for k, v in sorted(Counter(result).items()):
#         print(f'{k}: {v}')
# OR
# from collections import Counter
#
# with open('pythonzen.txt', 'r', encoding='utf-8') as file:
#     letters = Counter([letter.lower() for letter in file.read() if letter.isalpha()])
#
# for letter in sorted(letters):
#     print(f'{letter}: {letters[letter]}')


# В ПОИСКАХ СЛОВ 😇

# from collections import Counter
#
# txt = Counter(input().lower().split()).most_common()
# print(max(txt, key=lambda x: x[1])[0])


# В ПОИСКАХ СЛОВ 😋

# from collections import Counter
#
# txt = Counter(input().lower().split()).most_common()
# comparative = min(txt, key=lambda x: x[1])
# answer = [k for k, v in txt if v == comparative[1]]
# print(*sorted(answer), sep=', ')


# В ПОИСКАХ СЛОВ 🥳

# from collections import Counter
#
# txt = Counter(input().lower().split()).most_common()
# comparative = max(txt, key=lambda x: x[1])
# answer = [k for k, v in txt if v == comparative[1]]
# answer = sorted(answer)
# print(answer[-1])


# СТАТИСТИКА ДЛИН СЛОВ

# from collections import defaultdict
#
# txt = input().split()
# result = defaultdict(int)
# for i in txt:
#     result[len(i)] += 1
# [print(f'Слов длины {k}: {v}') for k, v in sorted(result.items(), key=lambda x:x[1])]
# OR
# from collections import Counter
#
# res = Counter(len(word) for word in input().split())
# for k, v in sorted(res.items(), key=lambda t: t[1]):
#     print(f'Слов длины {k}: {v}')
# OR
# from collections import Counter

# words = Counter(map(len, input().split())).most_common()
# for length, count in sorted(words, key=lambda x: x[1]):
#     print(f'Слов длины {length}: {count}')


# ВСЕ ЕЩЕ ОДИН

# import sys
#
# data = list((map(str.strip, sys.stdin)))
# print(sorted(data, key=lambda x: int(x.split()[1]))[1].split()[0])
# OR
# from collections import Counter
# import sys
#
# c = Counter()
# for data in sys.stdin:
#     name, score = data.split()
#     c[name] = int(score)
# print(c.most_common()[-2][0])


# 6.8.6

# from collections import Counter
#
# data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')
# data.max_values = lambda: list(filter(lambda x: x[1] == max(data.values()), data.most_common()))
# data.min_values = lambda: list(filter(lambda x: x[1] == min(data.values()), data.most_common()))
# print(data.max_values())


# HERE WE GO AGAIN

# from collections import Counter
# import csv
#
# with open('name_log.csv', 'r', encoding='utf-8') as file:
#     rows = csv.reader(file)
#     title = next(file)
#     c = sorted(Counter(i[1] for i in rows).items())
# [print(f'{k}: {v}') for k, v in c]
# OR
# from collections import Counter
# import csv
#
# with open('name_log.csv', 'r', encoding='utf-8') as file:
#     rows = csv.reader(file)
#     title = next(file)
#     c = Counter()
#     for row in sorted(rows, key=lambda x: x[1]):
#         c[row[1]] += 1
# [print(f'{k}: {v}') for k, v in c.items()]


# ФУНКЦИЯ scrabble()

# from collections import Counter
#
#
# def scrabble(symbols, word):
#     symbols = Counter(symbols.lower())
#     word = Counter(word.lower())
#     return symbols >= word
#
# print(scrabble('1Btee25g.ge.1e24k', 'Beegeek'))


# ФУНКЦИЯ print_bar_chart()

# from collections import Counter
#
#
# def print_bar_chart(data, mark):
#     counter = Counter(data)
#     max_space = len(max(counter.keys(), key=len)) + 1
#     for k, v in counter.most_common():
#         print(f'{k.ljust(max_space, " ")}|{mark*v}')
#
#
# languages = ['java', 'java', 'python', 'C++', 'assembler', 'java', 'C++', 'C', 'pascal', 'C++', 'pascal', 'java']
#
# print_bar_chart(languages, '☭')


# БЕСПЛАТНЫЕ КУРСЫ БЕРУТ СВОЕ 😢

# import csv, json
# from collections import Counter
#
# counter = Counter()
# money = 0
#
#
# def sum_things(name_file):
#     with open(name_file, 'r', encoding='utf-8') as file:
#         title, *rows_1 = csv.reader(file)
#         for name, f, s, t in rows_1:
#             counter[name] += sum(map(int, [f, s, t]))
#
#
# with open('prices.json', 'r', encoding='utf-8') as price:
#     cost = json.load(price)
#     for i in range(1, 5):
#         sum_things(f'quarter{i}.csv')
#     for k, v in counter.most_common():
#         money += cost[k] * v
# print(money)


# БЕСПЛАТНЫЕ КУРСЫ БЕРУТ СВОЕ 😭

# from collections import Counter
#
# books = Counter(map(int, input().split()))
# money = 0
# for i in range(int(input())):
#     book, price = map(int, input().split())
#     if books[book] > 0:
#         money += price
#     books[book] -= 1
#
# print(money)
# OR
# from collections import Counter
#
# books = Counter(map(int, input().split()))
# total = 0
#
# for _ in range(int(input())):
#     book, price = map(int, input().split())
#     total += bool(books[book]) * price
#     books -= Counter({book: 1})
#
# print(total)


# FOR FUN ^_^

# my_list = [1, 2, 3]
#
#
# def apppend_new(num, m=None):
#     if m is None:
#         m = [5, 6, 9]
#     res = m.copy()
#     res.append(num)
#     return res
#
#
# num = int(input())
# print(apppend_new(num))
# print(apppend_new(num))


# ЗООПАРК

# import json
# from collections import ChainMap
#
# with open('zoo.json', 'r', encoding='utf-8') as file:
#     info = ChainMap(*json.load(file))
#     print(sum(info.values()))


# БУЛОЧНЫЙ МАГНАТ

# from collections import ChainMap, Counter
#
# bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
# meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
# sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
# vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
# toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}
#
# all_things = ChainMap(bread, meat, sauce, vegetables, toppings)
# buying = Counter(input().split(','))
#
# max_space = len(max(buying, key=len))
# money = 0
#
# for k, v in sorted(buying.items()):
#     print(f'{k.ljust(max_space, " ")} x {v}')
#     money += all_things[k] * v
#
# print(f'''{"-" * max(len(f'ИТОГ: {money}р'), max_space + 3 + len(str(max(buying.values()))))}
# ИТОГ: {money}р''')


# ФУНКЦИЯ get_all_values()

# from collections import ChainMap
#
#
# def get_all_values(chainmap, txt):
#     my_set = set()
#     for i in chainmap.maps:
#         if i.get(txt, None) != None:
#             my_set.add(i[txt])
#     return my_set
#
#
# chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
# result = get_all_values(chainmap, 'nam')
#
# print(*sorted(result))


# ФУНКЦИЯ deep_update()

# from collections import ChainMap
#
#
# def deep_update(chainmap, key, value):
#     for i in chainmap.maps:
#         if key in i:
#             i[key] = value
#     if key not in chainmap.keys():
#         chainmap[key] = value
#
#
#
# chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
# deep_update(chainmap, 'age', 20)
#
# print(chainmap)


# ФУНКЦИЯ

# from collections import ChainMap
#
#
# def get_value(chainmap, key, from_left=True):
#     if from_left is True and key in chainmap:
#         return chainmap[key]
#     elif from_left is False and key in chainmap:
#         chainmap = ChainMap(*chainmap.maps[::-1])
#         return chainmap[key]
#
#
# chainmap = ChainMap({'age': 20}, {'city': 'Moscow'}, {'name': 'Anri', 'age': 20}, {'name': 'Timur', 'age': 29})
#
# print(get_value(chainmap, 'age', False))


# EPISODE 7 ^_^
# ______________


# РЕВЬЮ КОДА 😤

# total = 0
#
# with open('data.txt', 'r', encoding='utf-8') as file:
#     for _ in file.readlines():
#         total += 1
#
# print(total)


# РЕВЬЮ КОДА 😠

# def swapcase_vowels(string):
#     vowels = 'aeiouy'
#     swapped_string = ''
#
#     for char in string:
#         if char in vowels:
#             char = char.upper()
#         swapped_string += char
#
#     return swapped_string


# РЕВЬЮ КОДА 😡

# a = int(input())
# b = int(input())
# numbers = []
#
# for i in range(a, b + 1):
#     if i % 7 == 0:
#         numbers.append(i)
#
# print(numbers)


# РЕВЬЮ КОДА 🤬

# def get_max_index(numbers):
#     max_index = numbers.index(max(numbers))
#
#     return max_index


# 7.2.1

# blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2},
#               {'Likes': 13, 'Comments': 2, 'Shares': 1},
#               {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3},
#               {'Comments': 4, 'Shares': 2},
#               {'Photos': 8, 'Comments': 1, 'Shares': 1},
#               {'Photos': 3, 'Likes': 19, 'Comments': 3}]
#
# total_likes = 0
#
# for post in blog_posts:
#     try:
#         total_likes += post['Likes']
#     except KeyError:
#         total_likes -= 1
# print(total_likes)


# 7.2.2

# food = ['chocolate', 'chicken', 'corn', 'sandwich', 'soup', 'potatoes', 'beef', 'lox', 'lemonade']
# fifth = []
#
# for x in food:
#     try:
#         fifth.append(x[4])
#     except IndexError:
#         fifth.append('_')
# print(fifth)


# 7.2.3

# numbers = [6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]
#
# remainders = []
#
# for number in numbers:
#     try:
#         remainders.append(36 % number)
#     except ZeroDivisionError:
#         pass
# print(remainders)


# ONLY NUMBERS

# import sys
# from decimal import Decimal
#
# num = Decimal(0)
# counter = 0
# all = [i.strip() for i in sys.stdin]
# for i in all:
#     try:
#         num += Decimal(i)
#     except:
#         counter += 1
# print(num)
# print(counter)


# ЯНВАРЬ, ФЕВРАЛЬ...

# import calendar
#
# key = list(range(1, 13))
# value = list(calendar.month_name[1:])
# month = dict(zip(key, value))
# # Или так создать словарь с месяцами
# # months = {num: month for num, month in enumerate(calendar.month_name) if month}
# try:
#     data = int(input())
#     print(month[data])
# except KeyError:
#     print('Введено число из недопустимого диапазона')
# except ValueError:
#     print('Введено некорректное значение')
# OR
# from calendar import month_name
#
# try:
#     print(dict(zip(range(1, 13), month_name[1:]))[int(input())])
# except KeyError:
#     print('Введено число из недопустимого диапазона')
# except:
#     print('Введено некорректное значение')


# ФУНКЦИЯ add_to_list_in_dict()

# def add_to_list_in_dict(data, key, element):
#     try:
#         data[key].append(element)
#     except KeyError:
#         data[key] = [element]


# README.TXT
#
# file = input()
# try:
#     with open(file, 'r', encoding='utf-8') as file:
#         print(file.read())
# except:
#     print('Файл не найден')


# ФУНКЦИЯ get_weekday()

# import calendar, locale
#
# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
#
#
# def get_weekday(number):
#     days = {num: day for num, day in enumerate(calendar.day_name, 1) if day}
#     if not isinstance(number, int):
#         raise TypeError('Аргумент не является целым числом')
#     elif not 1 <= number <= 7:
#         raise ValueError('Аргумент не принадлежит требуемому диапазону')
#     return days[number]
#
#
# try:
#     print(get_weekday(8))
# except ValueError as err:
#     print(err)
#     print(type(err))

# ФУНКЦИЯ get_id()

# def get_id(names: list, name: str):
#     if not isinstance(name, str):
#         raise TypeError('Имя не является строкой')
#     elif not name.istitle() or not name.isalpha():
#         raise ValueError('Имя не является корректным')
#     names.append(name)
#     return len(names)
#
#
# names = ['Timur', 'Anri', 'Dima']
# name = 'Arthur'
#
# print(get_id(names, name))


# ДЕСЕРИАЛИЗАЦИЯ

# import json
#
# try:
#     with open(input(), 'r', encoding='utf-8') as file:
#         info = json.load(file)
#         print(info)
# except ValueError:
#     print('Ошибка при десериализации')
# except FileNotFoundError:
#     print('Файл не найден')
# OR
# import json
#
# try:
#     with open(input(), 'r', encoding='utf-8') as file:
#         try:
#             info = json.load(file)
#             print(info)
#         except:
#             print('Ошибка при десериализации')
# except FileNotFoundError:
#     print('Файл не найден')


# ФУНКЦИЯ is_good_password() 👀

# def is_good_password(string: str):
#     if all(
#         (len(string) >= 9,
#          any(c.islower() for c in string),
#          any(c.isupper() for c in string),
#          any(c.isdigit() for c in string))
#             ):
#         return True
#     else:
#         return False
#
#
# print(is_good_password('4abcdABC'))


# ФУНКЦИЯ is_good_password() 🐍

# class PasswordError(Exception):
#     pass
#
#
# class LengthError(PasswordError):
#     pass
#
#
# class LetterError(PasswordError):
#     pass
#
#
# class DigitError(PasswordError):
#     pass
#
#
# def is_good_password(string: str):
#
#     if len(string) < 9:
#         raise LengthError
#
#     elif string == string.upper() or string == string.lower():
#         raise LetterError
#
#     elif not any(c.isdigit() for c in string):
#         raise DigitError
#
#     return True
#
# try:
#     print(is_good_password('125634623623q'))
# except Exception as err:
#     print(type(err))


# УЖ ЛУЧШЕ МАТРИЦЫ 😐

# import sys
#
#
# class PasswordError(Exception):
#     pass
#
#
# class LengthError(PasswordError):
#     pass
#
#
# class LetterError(PasswordError):
#     pass
#
#
# class DigitError(PasswordError):
#     pass
#
#
# def is_good_password(string: str):
#     if len(string) < 9:
#         raise LengthError
#
#     elif string == string.upper() or string == string.lower():
#         raise LetterError
#
#     elif not any(c.isdigit() for c in string):
#         raise DigitError
#
#     return True
#
#
# passwords = [i.strip() for i in sys.stdin]
#
# for i in passwords:
#     try:
#         if is_good_password(i):
#             print('Success!')
#             break
#
#     except Exception as err:
#         print(err.__class__.__name__)


# EPISODE 8 ^_^
# ______________


# ПОДОЗРИТЕЛЬНО ПРОСТО 🤫

# def traffic(n):
#     if n > 0:
#         print('Не парковаться')
#         traffic(n - 1)
# traffic(3)


# ПОДОЗРИТЕЛЬНО ПРОСТО 🤐

# def print_number(n):
#     if n > 0:
#         print_number(n - 1)
#         print(n)
#
#
# print_number(100)


# 8.2.3

# numbers = [243, -279, 395, 130, 89, 269, 861, 669, 939, 367, -46, 710, 841, -280, -244, 274, -132, 273, 418, 432, -341,
#            437, 360, 960, 195, 792, 106, 461, -35, 980, -80, 540, -358, 69, -26, -416, 597, 96, 533, 232, 755, 894, 331,
#            323, -383, -386, 231, 436, 553, 967, 166, -151, 772, 434, 325, 301, 275, 431, 556, 728, 558, 702, 463, 127,
#            984, 212, 876, -287, -16, -177, 577, 604, 116, 500, 653, 669, 916, 802, 817, 762, -210, -353, 144, -351, 777,
#            805, 692, 22, -303, 249, 190, 411, 236, -274, 174, 380, 71, 124, -85, 430]
#
#
# def print_list(numbers, n=0):
#     if n < len(numbers):
#         print(f'Элемент {n}: {numbers[n]}')
#         print_list(numbers, n + 1)
#
#
# print_list(numbers)


# ОБРАТНЫЙ ПОРЯДОК

# import sys
#
# numbers = [int(i) for i in sys.stdin]
#
#
# def reverse(numbers: list, n=0):
#     if n < len(numbers):
#         reverse(numbers, n + 1)
#         print(numbers[n])
#
#
# reverse(numbers)
# OR
# def recursion():
#     digit = int(input())
#     if digit != 0:
#         recursion()
#     print(digit)
#
# recursion()


# ФУНКЦИЯ triangle() 😥

# def triangle(h):
#     def rec(step):
#         if step > 0:
#             print('*' * step)
#             rec(step - 1)
#
#
#     rec(h)
#
# triangle(h)


# ФУНКЦИЯ triangle() 😰

# def triangle(h):
#     def rec(step):
#         if step > 0:
#             rec(step - 1)
#             print('*' * step)
#
#
#     rec(h)
#
# triangle(h)


# ПЕСОЧНЫЕ ЧАСЫ

# def watch(num=1, size=16, space=16):
#     if size > 4:
#         print((str(num) * size).center(space))
#         watch(num + 1, size - 4)
#         print((str(num) * size).center(space))
#     else:
#
#         print('4444'.center(space))
#
#
#
# watch(num=1, size=16, space=16)


# ФУНКЦИЯ print_digits() 😉

# def print_digits(numbers):
#     def rec(step=0):
#         if step != len(str(numbers)):
#             print(str(numbers)[::-1][step])
#             rec(step + 1)
#
#     rec(0)
#
#
# print_digits(12345)
# OR
# def print_digits(number):
#     if str(number):
#         print(str(number)[-1])
#         print_digits(str(number)[:-1])


# ФУНКЦИЯ print_digits() 😎

# def print_digits(numbers):
#     def rec(step):
#         if step != len(str(numbers)):
#             print(str(numbers)[step])
#             rec(step+1)
#
#     rec(0)
#
#
# print_digits(12345)


# КОЛИЧЕСТВО ЦИФР

# def counter(num):
#     count = 0
#
#     def rec_step(count):
#         if count != len(num):
#             count += 1
#             return rec_step(count)
#         else:
#             return count
#
#     count = rec_step(count)
#     return count
#
#
# print(counter(input()))


# СУММА ЦИФР

# def sum_(num):
#     if not num:
#         return 0
#     return int(num[0]) + sum_(num[1:])
#
#
# print(sum_(input()))


# ФУНКЦИЯ number_of_frogs()

# def number_of_frogs(num):
#     if num == 1:
#         return 77
#     return 3 * (number_of_frogs(num - 1) - 30)
#
#
# print(number_of_frogs(3))


# ФУНКЦИЯ range_sum()

# def range_sum(lst, start, end):
#     if start == end:
#         return lst[start]
#     else:
#         return lst[start] + range_sum(lst, start + 1, end)
#
#
# print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))


# ОБЫЧНОЕ ВОЗВЕДЕНИЕ В СТЕПЕНЬ

# def get_pow(a, n):
#     def rec(step):
#         if step == 0:
#             return 1
#         else:
#             return a * (rec(step - 1))
#
#     return rec(n)
#
#
# print(get_pow(12, 2))


# БЫСТРОЕ ВОЗВЕДЕНИЕ В СТЕПЕНЬ

# Ошибочный вариант решения!!!(см."OR")
# rec = lambda a, step: 1 if step == 0 else a * rec(a, step - 1)
#
#
# def get_fast_pow(a, n):
#     if n % 2 == 0:
#         result = rec(a * a, n // 2)
#         return result
#     else:
#         result = rec(a, n)
#         return result
#
#
# print(get_fast_pow(2, 10000))
# OR
# def get_fast_pow(a, n):
#     if n == 0:
#         return 1
#     if n % 2 == 0:
#         return get_fast_pow(a * a, n // 2)
#     else:
#         return get_fast_pow(a, n - 1) * a
#
#
# print(get_fast_pow(2, 10000))


# ФУНКЦИЯ recursive_sum()

# def recursive_sum(a, b):
#     if a == 0:
#         return b
#     return recursive_sum(a - 1, b + 1)
#
#
# print(recursive_sum(10, 22))


# ФУНКЦИЯ is_power()

# def is_power(num):
#     if num < 2:
#         if num == 1:
#             return True
#         else:
#             return False
#     return is_power(num / 2)
#
#
# print(is_power(100))


# ФУНКЦИЯ tribonacci()

# def tribonacci(n):
#     cache = {1: 1, 2: 1, 3: 1}
#
#     def fib_rec(n):
#         result = cache.get(n)
#         if result is None:
#             result = fib_rec(n - 3) + fib_rec(n - 2) + fib_rec(n - 1)
#             cache[n] = result
#         return result
#
#     return fib_rec(n)
#
#
# print(tribonacci(6))


# ФУНКЦИЯ is_palindrome()

# def is_palindrome(txt):
#     if txt == '' or len(txt) == 1:
#         return True
#     if txt[0] != txt[-1]:
#         return False
#     return is_palindrome(txt[1:-1])
#
# print(is_palindrome('12321'))


# ФУНКЦИЯ to_binary()

# def to_binary(num):
#     b = ''
#     def rec(num):
#         nonlocal b
#         if num // 2 != 0:
#             b = str(num%2) + b
#             return rec(num//2)
#         if num % 2 == 1:
#             b = str(num%2) + b
#         if num % 2 == 0:
#             b = str(num % 2) + b
#     rec(num)
#     return b
#
# print(to_binary(0))
# OR
# def to_binary(n):
#     if n <= 1:
#         return str(n)
#     return to_binary(n // 2) + str(n % 2)
#
#
# print(to_binary(5))


# БЕЗ ЦИКЛОВ

# def without_cycles(num):
#     if num > 0:
#         print(num)
#         without_cycles(num - 5)
#     print(num)
#
#
# num = int(input())
# without_cycles(num)


# ФУНКЦИЯ recursive_sum()
#
# def recursive_sum(lst):
#     total = 0
#
#     def rec(lst):
#         nonlocal total
#         if isinstance(lst, int):
#             total += lst
#         else:
#             for i in lst:
#                 rec(i)
#
#     rec(lst)
#     return total
#
#
# my_list = [1, [4, 4], 2, [1, [2, 10]]]

# print(recursive_sum(my_list))


# ФУНКЦИЯ liner():

# def linear(lst):
#     new_list = []
#     if isinstance(lst, list):
#         for i in lst:
#             if isinstance(i, list):
#                 new_list.extend(linear(i))
#             else:
#                 new_list.append(i)
#         return new_list
#     else:
#         print('Это не список')
#
#
# my_list = [3, [4], [5, [6, [7, 8]]]]
#
# print(linear(my_list))


# ФУНКЦИЯ get_value()

# def get_value(data, key):
#     if key in data:
#         return data[key]
#     for k, v in data.items():
#         if isinstance(v, dict):
#             value = get_value(v, key)
#             if value is not None:
#                 return value
#
#
#
# data = {'firstName': 'Тимур', 'lastName': 'Гуев', 'birthDate': {'day': 10, 'month': 'October', 'year': 1993},
#         'address': {'streetAddress': 'Часовая 25, кв. 127',
#                     'city': {'region': 'Московская область', 'type': 'город', 'cityName': 'Москва'},
#                     'postalCode': '125315'}}
#
# print(get_value(data, 'cityName'))


# ФУНКЦИЯ get_all_values() 🌶️

# def get_all_values(data, key):
#     answer = set()
#     # Базовое решение(случай)
#     if key in data:
#         answer.add(data[key])
#     # Ходим по значениям словарей отыскивая вложенные словари
#     for i in data.values():
#         if isinstance(i, dict):
#             value = get_all_values(i, key)
#             # Проверяем результат вызова функции
#             if value is not None:
#                 answer |= value
#     return answer
#
#
# my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
# result = get_all_values(my_dict, 'top_grade')
#
# print(*sorted(result))
# print(type(result))


# ФУНКЦИЯ dict_travel() 🌶️🌶️

# def dict_travel(data: dict, way=None):
#     # Используем way для сохранения ключей у которых значение dict
#     # При каждом рекурсивном вызове будем иметь пустой список, чтобы путь не был смешанным
#     if way is None:
#         way = []
#     # Бежим по словарю
#     for k, v in sorted(data.items()):
#         # Если way пуст то в виде ключа будет только [k]
#         # Иначе когда way не пустой, то будем получать путь к значению в виде -> a.b: 10
#         if not isinstance(v, dict):
#             print(f'{".".join(way + [k])}: {v}')
#         # Запускаем рекурсию от значения(словаря) и фиксируем то на сколько провалимся ([k]) в поисках не словаря
#         if isinstance(v, dict):
#             dict_travel(v, way + [k])
#
# data = {'d': 1, 'b': {'c': 30, 'a': 10, 'b': 20}, 'a': 100}
#
# dict_travel(data)
# OR
# def dict_travel(data):
#     for k, v in sorted(data.items()):
#         if isinstance(v, dict):
#             dict_travel({f'{k}.{key}': val for key, val in v.items()})
#         else:
#             print(f'{k}: {v}')
#
# data = {'d': 1, 'b': {'c': 30, 'a': 10, 'b': 20}, 'a': 100}
#
# dict_travel(data)


# EPISODE 9 ^_^
# ______________


# СТРОЧНЫЙ АЛФАВИТ


# [print(chr(i)) for i in range(97, 123)]


# ФУНКЦИЯ convert()

# def convert(num):
#     return f'{num:#b}', f'{num:o}', f'{num:X}'
#
# print(convert(int(input())))


# 9.1.3

# films = {'Spider-Man: No Way Home': {'imdb': 8.8, 'kinopoisk': 8.3},
#          'Don"t Look Up': {'imdb': 7.3, 'kinopoisk': 7.6},
#          'Encanto': {'imdb': 7.3, 'kinopoisk': 7.4},
#          'The Witcher': {'imdb': 8.2, 'kinopoisk': 7.3},
#          'Ghostbusters: Afterlife': {'imdb': 7.3, 'kinopoisk': 8},
#          'Harry Potter 20th Anniversary: Return to Hogwarts': {'imdb': 8.1, 'kinopoisk': 8.2},
#          'Shingeki no Kyojin': {'imdb': 9.0, 'kinopoisk': 8.3},
#          'The Matrix': {'imdb': 8.7, 'kinopoisk': 8.5},
#          'The Dark Knight': {'imdb': 9.0, 'kinopoisk': 8.5},
#          'The Shawshank Redemption': {'imdb': 9.3, 'kinopoisk': 9.1},
#          'Avengers: Endgame': {'imdb': 8.4, 'kinopoisk': 7.7}}
# print(min(films, key=lambda x: sum(films[x].values())))


# ФУНКЦИЯ non_negative_even()

# def non_negative_even(lst):
#     return all(map(lambda x: x >= 0 and x % 2 == 0, lst))
# OR
# def non_negative_even(numbers):
#     return all(i >= 0 and i % 2 == 0 for i in numbers)
#
#
# print(non_negative_even([0, 2, 4, 8, 16]))


# ФУНКЦИЯ is_greater()

# def is_greater(data, num):
#     return any(sum(i) > num for i in data)
#
#
# data = [[-3, 4, 0, 1], [1, 1, -4], [0, 0], [9, 3]]
# print(is_greater(data, 10))


# ФУНКЦИЯ custom_isinstance()
#
# def custom_isinstance(list, check):
#     return sum([1 for i in list if isinstance(i, check)])
#
#
# numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
# print(custom_isinstance(numbers, int))


# 9.1.7

# numbers = [-7724, 5023, 3197, -102, -4129, -880, 5857, -2866, -8913, 1195, 9809, 5347, -8071, 903, 3030, -4347, -3354,
#            1024, 8670, 4210, -5228, 8900, 4823, -2002, 4900, 9520, -3658, 1104, -9554, 3064, 9632, -8701, 3384, 4370,
#            2034, 7822, -9694, 3347, 7440, -8459, 3238, -5193, -3381, 5281, 9022, 5559, 7593, -6540, -6204, -2483, 8729,
#            5810, -8254, -9846, -1801, 4882, 3838, -3140, 7609, -3325, 6026, 2994, -1677, 1266, -1893, -4408, -5722,
#            -2841, 9812, 5837, -7474, 4624, -664, 6998, 7888, -971, 8810, 3812, -5396, 2593, 512, -4634, 9735, -3062,
#            9031, -9300, 3657, 6332, 7552, 8125, -725, 4392, 1727, 8194, -2828, -4314, -8967, -7912, -1363, -5957]
# print(numbers.index(max(numbers)))
# # OR
# from operator import itemgetter
# print(max(enumerate(numbers), key=itemgetter(1))[0])


# ФУНКЦИЯ my_pow()

# from functools import reduce
#
# def my_pow(num):
#     num = enumerate(str(num), 1)
#     return reduce(lambda x, y: x + int(y[1])**y[0], num, 0)
# OR
# def my_pow(num):
#     res = 0
#     for p, n in num:
#         res += int(n) ** p
#     return res


# print(my_pow(139))


# 9.1.9

# names = ['Moana', 'Cars', 'Zootopia', 'Ratatouille', 'Coco', 'Inside Out', 'Finding Nemo', 'Frozen']
# budgets = [150000000, 120000000, 150000000, 150000000, 180000000, 175000000, 94000000, 150000000]
# box_offices = [643331111, 462216280, 1023784195, 620702951, 807082196, 857611174, 940335536, 1280802282]
# [print(f'{name}: {plus - cost}$') for name, cost, plus in sorted(zip(names, budgets, box_offices), key=lambda x: x[0])]
# OR
# for name, cost, plus in sorted(zip(names, budgets, box_offices), key=lambda x: x[0]):
#     print(f'{name}: {plus - cost}$')


# ФУНКЦИЯ zip_longest()

# def zip_longest(*args, fill=None):
#     max_len = max(map(len, args))
#     result = [i + [fill] * (max_len - len(i)) for i in args]
#     return list(zip(*result))
#
#
# print(zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_'))
# OR
# import itertools
#
# def zip_longest(*args, fill = None):
#     return list(itertools.zip_longest(*args, fillvalue=fill))


# НЕОБЫЧНАЯ СОРТИРОВКА 🌶️

# txt = list(input())
# txt = sorted(txt)
# for i in sorted(txt, key=lambda x: (not x.islower(), not x.isupper(), int(x) % 2 == 0 if x.isdigit() else x)):
#     print(i, end='')


# ФУНКЦИЯ hash_as_key()

# def hash_as_key(data):
#     result = {}
#     for i in data:
#         if data.count(i) == 1 and hash(i) != -2:
#             result[hash(i)] = i
#         else:
#             result.setdefault(hash(i), []).append(i)
#     return result
#
#
# data = [-1, -2, -3, -4, -5]
#
# print(hash_as_key(data))


# КОЛЛЕКЦИИ

# txt = eval(input())
#
# if isinstance(txt, list):
#     print(txt[-1])
# if isinstance(txt, tuple):
#     print(txt[0])
# elif isinstance(txt, set):
#     print(len(txt))


# МАТЕМАТИЧЕСКИЕ ВЫРАЖЕНИЯ

# import sys
# print(max([eval(i) for i in sys.stdin]))


# МИНИМУМ И МАКСИМУМ

# func = input()
# x = list(map(int, input().split()))
#
# result = [(eval(func)) for x in range(x[0], x[1] + 1)]
#
# print(f'Минимальное значение функции {func} на отрезке [{x[0]}; {x[1]}] равно {min(result)}')
# print(f'Максимальное значение функции {func} на отрезке [{x[0]}; {x[1]}] равно {max(result)}')


# 9.3.1

# data = ['Timur', -16.648911695768902, 'six', -202, 883.0093275936454, -765, (3, 4), -105.10718000213546, 976,
#         -308.96857946288094, 458, ['one', 'two'], 479.92207220345927, -87, -71, 'twelve', 112, -621, -715.0179551194733,
#         'seven', 229, 729, -358, [1, 2, 3], -974, 882, -894.4709033242768, '', 323.7720806756133, 'beegeek', -224, 431,
#         170.6353248658936, -343.0016746052049, 'number', 104.17133679352878, [], -353.5964777099863, 'zero', -113, 288,
#         None, -708.3036176571618]
# fil = filter(lambda x: isinstance(x, (int, float)), data)
# [print(int(i)) for i in fil]


# 9.3.2

# numbers = [4754, -4895, -364, -4764, 4683, 1639, -43, 228, -2701, -1503, 1223, 4340, -1296, 3939, -345, 623, -3275,
#            1003, 4367, -1739, 550, -1217, -1334, 1526, -4359, -3028, -4663, 3356, 3887, 4297, -1982, 1013, 3299, 3556,
#            -3324, 417, 3531, -3134, 1782, 4439, 1652, -985, 4327, 1517, 1225, -915, 2808, -3851, -1005, 3396, 2842,
#            -3879, -3824, -3805, 1609, -4741, -3072, 3573, 4680, 588, -1430, 2378, -1095, -343, 4357, -2164, -3304, 4354,
#            4926, -352, -1187, -3313, 2741, 4786, -2689, 741, 4558, 1442, 62, -1099, -2201, -16, -3115, 1862, 2384, 4072,
#            -90, 204, 1158, -3134, -2512, 756, 4148, 4370, 1756, 3609, -1148, -3909, 4123, -2906, 69, 96, 1111]
# fil = list(filter(lambda x: len(str(abs(x))) == 2 and x % 9 == 0, numbers))
# print(sum(map(lambda x: x**2, fil)))


# 9.3.3

# names = ['ульяна', 'арина', 'Дмитрий', 'Сергей', 'Яна', 'мила', 'Ольга', 'софья', 'семён', 'Никита', 'маргарита',
#          'Василиса', 'Кирилл', 'александр', 'александра', 'Иван', 'андрей', 'Родион', 'максим', 'алиса', 'Артём',
#          'софия', 'владимир', 'дамир', 'Валерий', 'степан', 'Алексей', 'Марк', 'олег', 'ирина', 'Милана', 'мия',
#          'денис', 'Фёдор', 'Елизавета', 'айлин', 'Варвара', 'валерия', 'Алёна', 'Николь', 'юлия', 'Ксения', 'пётр',
#          'георгий', 'Мария', 'глеб', 'илья', 'Захар', 'Дарья', 'Евгения', 'матвей', 'Серафим', 'екатерина', 'Тимофей',
#          'виктор', 'Егор', 'Ника', 'анна', 'даниил', 'тихон', 'вера', 'кира', 'Эмилия', 'Виктория', 'Игорь', 'полина',
#          'алина', 'Давид', 'анастасия', 'Вероника', 'ярослав', 'Руслан', 'татьяна', 'Демид', 'амелия', 'Элина', 'Арсен',
#          'евгений', 'мадина', 'дарина', 'Савелий', 'Платон', 'Аделина', 'диана', 'Айша', 'павел', 'Стефания', 'Тимур',
#          'Ева', 'Елисей', 'Артемий', 'григорий', 'Мирон', 'Мирослава', 'Мира', 'Марат', 'Лилия', 'роман', 'владислав',
#          'Леонид']
# names_sotr = map(str.capitalize, (filter(lambda x: x[0].lower() in ('ам') and len(x) > 4, names)))
# print(*sorted(names_sotr))


# ФУНКЦИЯ sfib()

# fib = lambda x: 1 if x <= 2 else fib(x - 1) + fib(x-2)
# print(fib(5))


# ФУНКЦИЯ print_operation_table()

# def print_operation_table(operation, rows, cols):
#     for i in range(1, rows + 1):
#         res = []
#         for j in range(1, cols + 1):
#             res.append(str(operation(i, j)).ljust(3))
#         print(*res)
# OR
# def print_operation_table(operation, rows, cols):
#     for i in range(1, rows + 1):
#         print(*map(operation, [i] * cols, range(1, cols + 1)))
#
#
# print_operation_table(lambda a, b: a * b, 5, 5)


# ФУНКЦИЯ verification()

# from string import ascii_lowercase, ascii_uppercase, digits
#
#
# def verification(login, password, success, failure):
#     check_box = all([any(map(lambda x: x in ascii_lowercase, password)),
#                      any(map(lambda x: x in ascii_uppercase, password)),
#                      any(map(lambda x: x in digits, password))])
#     if check_box is True:
#         return success(login)
#
#     elif check_box is False:
#         if len([i for i in password if i in ascii_lowercase]) == 0 and \
#             len([i for i in password if i in ascii_uppercase]) == 0:
#             text = 'в пароле нет ни одной буквы'
#             return failure(login, text)
#         elif len([i for i in password if i in ascii_uppercase]) == 0:
#             text = 'в пароле нет ни одной заглавной буквы'
#             return failure(login, text)
#         elif len([i for i in password if i in ascii_lowercase]) == 0:
#             text = 'в пароле нет ни одной строчной буквы'
#             return failure(login, text)
#         else:
#             text = 'в пароле нет ни одной цифры'
#             return failure(login, text)
#
#
# def success(login):
#     print(f'Здравствуйте, {login}!')
#
#
# def failure(login, text):
#     print(f'{login}, попробуйте снова. Текст ошибки: {text}')
#
#
# verification('Arthur_Davletov', 'мойпарольBEE123', success, failure)
# OR
# def verification(login, password, success, failure):
#     vd = {(str.isalpha, str.isascii): 'в пароле нет ни одной буквы',
#           (str.isascii, str.islower): 'в пароле нет ни одной строчной буквы',
#           (str.isascii, str.isupper): 'в пароле нет ни одной заглавной буквы',
#           (bool,        str.isdigit): 'в пароле нет ни одной цифры'}
#     for f in vd:
#         if not any(f[0](i) and f[1](i) for i in password):
#             return failure(login, vd[f])
#     success(login)


# ФУНКЦИЯ numbers_sum()

# def numbers_sum(lst):
#     """Принимает список и возвращает сумму его чисел (int, float),
#     игнорируя нечисловые объекты. 0 - если в списке чисел нет."""""
#     return sum([i for i in lst if isinstance(i, (int, float))])
#
#
# print(numbers_sum(['beegeek', 'stepik', '100']))


# НОВЫЙ print()

# old_print = print
#
#
# def print(*args, **kwargs):
#     res = [i.upper() if isinstance(i, str) else i for i in args]
#     if not kwargs:
#         old_print(*res)
#     else:
#         kwargs = [i[1].upper() for i in kwargs.items()]
#         old_print(*res, sep=kwargs[0], end=kwargs[1])
#
#
# print('beegeek', [1, 2, 3], 4)
# OR
# from sys import stdout
#
# def print(*s, sep=" ", end="\n"):
#     result = sep.upper().join(map(lambda x: str(x).upper() if type(x) is str else str(x), s)) + end.upper()
#     stdout.write(result)


# ФУНКЦИЯ polynom()

# def polynom(num):
#     res = num * num + 1
#     polynom.values.add(res)
#
#     return res
#
#
# polynom.__dict__['values'] = set()
#
# for _ in range(10):
#     polynom(10)
#
# print(polynom.values)


# ФУНКЦИЯ remove_marks()

# def remove_marks(text, marks):
#     remove_marks.__dict__['count'] = remove_marks.__dict__.get('count', 0) + 1
#     marks = list(marks)
#     res = [i for i in text if i not in marks]
#     return ''.join(res)
#
#
# marks = '.,!?'
# text = 'Are you listening? Meet my family! There are my parents, my brother and me.'
#
# for mark in marks:
#     print(remove_marks(text, mark))
#
# print(remove_marks.count)
# OR
# def remove_marks(text, marks):
#     remove_marks.count += 1
#     return ''.join(filter(lambda x: x not in marks, text))
#
#
# remove_marks.count = 0


# ФУНКЦИЯ power()

# def power(step):
#     def square(num):
#         return num ** step
#
#     return square
#
#
# square = power(2)
# print(square(5))


# ФУНКЦИЯ generator_square_polynom()
#
# def generator_square_polynom(a, b, c):
#     def solve(x):
#         f = a*x**2 + b*x + c
#         return f
#
#     return solve
#
#
# f = generator_square_polynom(26, 83, 22)
# print(f(55))

# ФУНКЦИЯ sourcetemplate()

# def sourcetemplate(url):
#     def load(**kwargs):
#         if not kwargs:
#             return url
#         else:
#             txt = [f'{str(k)}={str(v)}' for k, v in sorted(kwargs.items())]
#             return f'{url}?' + '&'.join(txt)
#
#     return load
#
#
# url = 'https://stepik.org/lesson/651459/step/14'
# load = sourcetemplate(url)
# print(load(thread='solutions', unit=648165, sase='agss'))

# ФУНКЦИЯ date_formatter()

# from datetime import date
#
#
# def date_formatter(txt):
#     county_code = {'ru': '%d.%m.%Y',
#                    'us': '%m-%d-%Y',
#                    'ca': '%Y-%m-%d',
#                    'br': '%d/%m/%Y',
#                    'fr': '%d.%m.%Y',
#                    'pt': '%d-%m-%Y'}
#
#     def today(d):
#         return d.strftime(county_code[txt])
#
#     return today
#
#
# date_ru = date_formatter('ca')
# today = date(2015, 12, 7)
# print(date_ru(today))


# ФУНКЦИЯ sort_priority() 🌶️

# def sort_priority(values: list, group: (list, tuple, set)):
#     new_group = [i for i in group if i in values]
#     values[:] = sorted(new_group) + sorted(set(values) ^ set(new_group))


# OR
# def sort_priority(numbers, group):
#     numbers.sort(key=lambda x: (x not in group, x))
# OR
# def sort_priority(values, group):
#     values.sort()
#     values.sort(key=lambda x: not x in group)

# data = list(range(0, 100, 5))
# sort_priority(data, {1, 90, 95, 25, 55, 64})
#
# print(data)

# ФУНКЦИЯ get_digits()

# def get_digits(number: int | float) -> list[int]:
#     """Возвращает список чисел"""

# return [int(i) for i in str(number) if i.isdigit()]


# print(get_digits(13.909934))


# ФУНКЦИЯ top_grade()

# def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
#     res = {}
#     res['name'] = grades['name']
#     res['top_grade'] = max(list(grades.items())[1][1])
#     return res
# OR
# def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
#     grades['top_grade'] = max(grades.pop('grades'))
# return grades

# print(top_grade({'name': 'Ruslan', 'grades': [19, 48, 86, 45, 32]}))


# ФУНКЦИЯ cyclic_shift()

# from collections import deque
#
#
# def cyclic_shift(numbers: list[int | float], step: int) -> None:
#     new_numbers = deque(numbers)
#     new_numbers.rotate(step)
#     numbers[:] = [i for i in new_numbers]
#
#
# numbers = [1, 2, 3, 4, 5]
# cyclic_shift(numbers, 1)
#
# print(numbers)
# OR
# def cyclic_shift(numbers: list[int | float], step: int) -> None:
#     if step >= 0:
#         for i in range(step):
#             c = numbers.pop()
#             numbers.insert(0, c)
#     elif step < 0:
#         for i in range(abs(step)):
#             c = numbers.pop(0)
#             numbers.append(c)
#
#
# numbers = [1, 2, 3, 4, 5]
# cyclic_shift(numbers, -2)
#
# print(numbers)

#
# ФУНКЦИЯ matrix_to_dict()

# def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
#     res = {k: v for k, v in enumerate(matrix, 1)}
#     return res
#
# matrix = [[5, 6, 7], [8, 3, 2], [4, 9, 8]]
#
#
# print(*matrix_to_dict.__annotations__.values())


# ДЕКОРАТОР sandwich

# def sandwich(func):
#     first = '---- Верхний ломтик хлеба ----'
#     second = '---- Нижний ломтик хлеба ----'
#     print(first)
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         print(second)
#         return res
#
#     return wrapper
#
# OR
#
# def sandwich(func):
#     def wrapper(*args, **kwargs):
#         print('---- Верхний ломтик хлеба ----')
#         result = func(*args, **kwargs)
#         print('---- Нижний ломтик хлеба ----')
#         return result
#     return wrapper
#
# @sandwich
# def add_ingredients(ingredients):
#     print(' | '.join(ingredients))
#
#
# add_ingredients(['томат', 'салат', 'сыр', 'бекон'])


# НОВЫЙ print

# def decorator_print(func):
#     def wrapper(*args, **kwargs):
#         args = [str(i).upper() for i in args]
#         kwargs = {k: v.upper() for k, v in kwargs.items()}
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# print = decorator_print(print)
#
# print('hi', 'there', 2, end='12')
# OR
# def decorator(func):
#     def wrapper(*args, sep=' ', end='\n'):
#         args = (i.upper() if isinstance(i, str) else i for i in args)
#         return func(*args, sep=sep.upper(), end=end.upper())
#     return wrapper
#
# print = decorator(print)


# ДЕКОРАТОР do_twice

# def do_twice(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         res = func(*args, **kwargs)
#
#         return res
#
#     return wrapper
#
#
# @do_twice
# def beegeek():
#     print('beegeek')
#
#
# print(beegeek())


# ФУНКЦИЯ reverse_args

# def reverse_args(func):
#     def wrapper(*args, **kwargs):
#         # args = [i for i in args[::-1]]
#         args = reversed(args)
#         res = func(*args, **kwargs)
#         return res
#
#     return wrapper
#
#
# @reverse_args
# def concat(a, b, c):
#     return a + b + c
#
#
# print(concat('apple', 'cherry', 'melon'))


# ФУНКЦИЯ exception_decorator

# def exception_decorator(func):
#     def wrapper(*args, **kwargs):
#         try:
#             res = func(*args, **kwargs)
#             return res, 'Функция выполнилась без ошибок'
#         except:
#             return None, 'При вызове функции произошла ошибка'
#
#     return wrapper
#
#
# sum = exception_decorator(sum)
#
# print(sum(['199', '1', 187]))


# ФУНКЦИЯ takes_positive

# def takes_positive(func):
#     def wrapper(*args, **kwargs):
#         kwargs_ = [isinstance(v, int) for v in kwargs.values()]
#         args_ = [isinstance(i, int) for i in args]
#
#         args_plus = [i for i in args if i <= 0]
#         kwargs_plus = [v for v in kwargs.values() if v <= 0]
#
#         if all(args_) is False:
#             raise TypeError
#         elif args_plus:
#             raise ValueError
#
#         if len(kwargs) == 0:
#             res = func(*args, **kwargs)
#             return res
#
#         elif all(kwargs_) is False:
#             raise TypeError
#         elif kwargs_plus:
#             raise ValueError
#         res = func(*args, **kwargs)
#         return res
#
#     return wrapper
#
#
# @takes_positive
# def positive_sum(*args):
#     return sum(args)
#
#
# try:
#     print(positive_sum(11, 20.7, 10))
# except Exception as err:
#     print(type(err))
# OR
# def takes_positive(func):
#     def dec(*args, **kwargs):
#         for i in [*kwargs.values()] + [*args]:
#             if not isinstance(i, int):
#                 return TypeError
#             elif i < 1:
#                 return ValueError
#         return func(*args, **kwargs)
#     return dec


# ДЕКОРАТОР square

# import functools
#
#
# def square(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs) ** 2
#         return res
#
#     return wrapper
#
#
# @square
# def add(a, b):
#     '''прекрасная функция'''
#     return a + b
#
#
# print(add(1, 1))
# print(add.__name__)
# print(add.__doc__)


# ДЕКОРАТОР returns_string

# from functools import wraps
#
#
# def returns_string(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         if not isinstance(res, str):
#             raise TypeError
#         return res
#
#     return wrapper
#
#
# @returns_string
# def add(a, b):
#     return a + b
#
# try:
#     print(add(3, 7))
# except TypeError as e:
#     print(type(e))


# ДЕКОРАТОР trace

# from functools import wraps
#
#
# def trace(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f'TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}')
#         print(f'TRACE: возвращаемое значение {func.__name__}(): {repr(func(*args, **kwargs))}')
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @trace
# def add(a, b, c):
#     '''docs'''
#     return a + b + c
#
#
# print(add(1, 2, 3))
# print(add.__name__)
# print(add.__doc__)


# ДЕКОРАТОР prefix

# import functools
#
#
# def prefix(string: str, to_the_end: bool = False):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             val = func(*args, **kwargs)
#             if to_the_end:
#                 return val + string
#             return string + val
#         return wrapper
#     return decorator
#
#
# @prefix('$$$', to_the_end=True)
# def get_bonus():
#     return '2000'
#
#
# print(get_bonus())


# ДЕКОРАТОР make_html

# from functools import wraps
#
#
# def make_html(tag: str):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             return f'<{tag}>{func(*args, **kwargs)}</{tag}>'
#
#         return wrapper
#
#     return decorator
#
# @make_html('i')
# @make_html('del')
# def get_text(text):
#     return text
#
#
# print(get_text('Python'))


# ДЕКОРАТОР repeat

# from functools import wraps
#
#
# def repeat(times: int):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range(times):
#                 val = func(*args, **kwargs)
#             return val
#
#         return wrapper
#
#     return decorator
#
#
# @repeat(4)
# def say_beegeek():
#     '''documentation'''
#     print('beegeek')
#
#
# print(say_beegeek.__name__)
# print(say_beegeek.__doc__)


# ДЕКОРАТОР srip_range

# from functools import wraps
#
#
# def strip_range(start: int, end: int, char: str = '.'):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             val = func(*args, **kwargs)
#             return val[:start] + char * (min(end, len(val)) - start) + val[end + 1:]
#             # OR
#             # val = [char if start <= i < end else j for i, j in enumerate(val)]
#             # return ''.join(val)
#         return wrapper
#
#     return decorator
#
#
# @strip_range(3, 20, '_')
# def beegeek():
#     return 'beegeek'
#
#
# print(beegeek())


# ДЕКОРАТОР returns

# from functools import wraps
#
#
# def returns(check_type):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             val = func(*args, **kwargs)
#             if isinstance(val, check_type):
#                 return val
#             raise TypeError
#
#         return wrapper
#
#     return decorator
#
#
# @returns(int)
# def add(a, b):
#     return a + b
#
#
# try:
#     print(add('199', '1'))
# except TypeError as e:
#     print(type(e))


# ДЕКОРАТОР takes

# from functools import wraps
#
#
# def takes(*args_type):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             over = list(kwargs.values()) + list(args)
#             flag = [True if isinstance(i, args_type) else False for i in over]
#             if not all(flag):
#                 raise TypeError
#             return func(*args, **kwargs)
#
#
#         return wrapper
#
#     return decorator
#
#
# @takes(int, str)
# def repeat_string(string, times):
#     return string * times
#
# print(repeat_string('bee', 3))


# ДЕКОРАТОР add_attrs

# def add_attrs(**kwargs_add):
#     def decorator(func):
#         func.__dict__.update(kwargs_add)
#         return func
#
#     return decorator
#
#
# @add_attrs(at1=10, at2=20, at3=30, at4=40, atf=50)
# def add(a, b):
#     '''add docs'''
#     return a + b
#
#
# print(add.at1)
# print(add.at2)
# print(add.at3)
# print(add.__name__)
# print(add.__doc__)
# print(add(1, 2))
# print(add(b=12, a=13))
# print(add.at4)
# print(add.atf)


# ДЕКОРАТОР ignore_exception

# from functools import wraps
#
#
# def ignore_exception(*args_type):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             try:
#                 return func(*args, **kwargs)
#             except args_type as e:
#                 print(f'Исключение {e.__class__.__name__} обработано')
#
#         return wrapper
#
#     return decorator
#
#
# @ignore_exception()
# def func():
#     '''func docs'''
#     raise ValueError
#
#
# try:
#     func()
# except Exception as e:
#     print(type(e))


# ДЕКОРАТОР retry

# from functools import wraps
#
#
# class MaxRetriesException(Exception):
#     pass
#
#
# def retry(times):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range(times):
#                 try:
#                     return func(*args, **kwargs)
#                 except:
#                     pass
#
#             raise MaxRetriesException
#
#         return wrapper
#
#     return decorator
#
#
# @retry(3)
# def no_way():
#     raise ValueError
#
#
# try:
#     no_way()
# except Exception as e:
#     print(type(e))


# ДВЕ ФУНКЦИИ

# from functools import partial
#
# name = 'Тимур'
# email_address = 'timyrik20@beegeek.ru'
# text = 'Школа BEEGEEK приглашает Вас на новый курс по программированию на языке Python. тутут....'
#
#
# def send_email(name, email_address, text):
#     return f'В письме для {name} на адрес {email_address} сказано следующее: {text}'
#
#
# to_Timur = partial(send_email, name, email_address)
# send_an_invitation = partial(send_email, text=text)
#
# print(send_an_invitation("Тимур", "timyrik20@beegeek.ru"))


# ПРОСТО ДИМА 🙂

# import sys
# from functools import lru_cache
#
#
# @lru_cache()
# def words(word):
#     return ''.join(sorted(word))
#
#
# check_words = [i.strip() for i in sys.stdin]
# for i in check_words:
#     print(words(i))


# ПРОСТО ДИМА 🙃

# from functools import lru_cache
#
#
# @lru_cache()
# def ways(num):
#     if num == 1:
#         return 1
#     elif num == 0:
#         return 0
#
#     if num > 4:
#         return ways(num - 1) + ways(num - 3) + ways(num - 4)
#     elif num > 3:
#         return ways(num - 1) + ways(num - 3)
#     elif num > 1:
#         return ways(num - 1)
#
#
# print(ways(50))


# EPISODE 10 ^_^
# ______________