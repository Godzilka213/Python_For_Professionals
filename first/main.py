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

# def choose_plural(num, words):
#     suffixes = {
#         1: 0, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 0: 2,
#     }
#     if 11 <= num % 100 <= 14:
#         return f'{num} {words[2]}'
#     else:
#         return f'{num} {words[suffixes[num % 10]]}'


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
