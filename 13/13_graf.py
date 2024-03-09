# s = "АБВГ БД ВБГДЕЗЖ ГЖ ДЕ ЕЗ ЖЗ"
# d = {c[0]: c[1:] for c in.txt s.split()}
#
#
# def f(s, e):
#     if s[-1] == e:
#         print(s)
#         return 1
#     return sum(f(s + c, e) for c in.txt d[s[-1]] if c not in.txt s)
#
#
# print(f("А", "З"))
#
# s = "АБГДЕ БВ ВЖИ ГДЖВБ ДЖЗ ЕДЗК ЖЛ ЗЖЛ ИЖЛ КЗЛМ МЛ"
# d = {c[0]: c[1:] for c in.txt s.split()}
#
#
# def f(s, e):
#     if s[-1] == e:
#         print(s)
#         return "Ж" in.txt s and "З" not in.txt s
#     return sum(f(s + c, e) for c in.txt d[s[-1]] if c not in.txt s)
#
#
# print(f("А", "Л"))
#
# s = "АБГД БВГ ВЗКЕ ГВЕЖ ДГ ЕКИ ЖЕИ ЗЛК ИМ КЛМН ЛН МН"
# d = {c[0]: c[1:] for c in.txt s.split()}
#
#
# def f(s, e):
#     if s[-1] == e:
#         print(s)
#         return ("Г" in.txt s and "Е" not in.txt s) or ("Г" not in.txt s and "Е" in.txt s)
#     return sum(f(s + c, e) for c in.txt d[s[-1]] if c not in.txt s)
#
#
# print(f("А", "Н"))

# s = "АБВГД БЕВ ВЖ ГВЖ ДГЖЗ ЕЖИ ЖИ ЗЖИ ИКЛ КМ ЛКМ"
# d = {c[0]: c[1:] for c in.txt s.split()}
#
# def f(s, e):
#     if s[-1] == e:
#         return len(s) - 1
#     return max(f(s + c, e) for c in.txt d[s[-1]] if c not in.txt s)
#
#
# print(f("А", "М"))

# s = "АБГД БГВ ВЕИГ ГЕЖД ДЖ ЕИМК ЖЕК ИМ КМ"
# d = {c[0]: c[1:] for c in.txt s.split()}
#
#
# def f(s, e):
#     if s[-1] == e:
#         return len(s) == 7
#     return sum(f(s + c, e) for c in.txt d[s[-1]])
#
#
# print(f("А", "М"))

# s = "АБГД БВГ ВЕКЗ ГВЕЖ ДГ ЕЖИМК ЖИ ЗЛК ИМ КЛМН ЛН МН"
# d = {c[0]: c[1:] for c in.txt s.split()}
# s1 = []
#
# def f(s, e):
#     if s[-1] == e:
#         if len(s) == 8:
#             s1.append(s)
#             # print(s)
#         return 1
#     return sum(f(s + c, e) for c in.txt d[s[-1]] if c not in.txt s)
#
#
# f("А", "Н")
# s1.sort()
# print(s1[0])

# s = "АЗВ БГА ВБЕКЗ ГА ДГА ЕБ ЖИ ЗИЖК ИД КЕЖ"
# d = {c[0]: c[1:] for c in.txt s.split()}
#
#
# def f(s, e):
#     if s[-1] == e:
#         return 1
#     return sum(f(s + c, e) for c in.txt d[s[-1]] if c not in.txt s)
#
#
# print(f("В", "А") + f("З", "А"))

# for n in.txt range(11, 50):
#     s = '3' + '5' * n
#     while "25" in.txt s or "355" in.txt s or "555" in.txt s:
#         if "25" in.txt s:
#             s = s.replace("25", "32", 1)
#         if "355" in.txt s:
#             s = s.replace("355", "25", 1)
#         if "555" in.txt s:
#             s = s.replace("555", "3", 1)
#     s = sum(list(map(int, list(s))))
#     if s % 25 == 0:
#         print(n)
#         break
# s = "4" * 60 + "6" * 60 + "8" * 60
#
# while "46" in.txt s or "84" in.txt s or "86" in.txt s:
#     if "46" in.txt s:
#         s = s.replace("46", "64", 1)
#     if "84" in.txt s:
#         s = s.replace("84", "48", 1)
#     if "86" in.txt s:
#         s = s.replace("86", "68", 1)
#
# print(s[24], s[74], s[149], sep="")

