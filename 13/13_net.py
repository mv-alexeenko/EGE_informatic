# ------------------------------ №13 Компьютерные сети -----------------------------------

# ++/Компьютерная (вычислительная) сеть - набор взаимосвязанных автономных вычислительных
# устройств./++

# Связь между узлами сети осуществляется по средствам различных протоколов
# ++/Протокол TCP/IP является основным протоколом передачи данных в сети Интернет. Он
# состоит из двух основных протоколов: TCP (Transmission Control Protocol) и IP (Internet
# Protocol):
#          -- Протокол TCP отвечает за установление соединения между устройствами, надежную
#             передачу данных, управление потоком данных и обеспечение доставки данных в
#             правильном порядке.
#          -- Протокол IP отвечает за маршрутизацию данных в сети, преобразование адресов
#            узлов в сети, фрагментацию и сборку пакетов данных.

# ++/Вместе TCP и IP обеспечивают надежную и эффективную передачу данных в сети Интернет./
# Выделяют три основных параметра:
#          -- IP адрес сети - идентификатор сети. Адрес оканчивающийся в двоичном виде на
#          все 0 - адрес сети
#          -- IP адрес узла - идентификатор компьютера в сети. Не может быть равен адресу
#          сети и широковещательному адресу.

# ++/Маска определяет, какая часть IP-адреса узла сети относится к адресу сети, а какая -
# к адресу самого узла в сети.
# Маска имеет вид: 255.255.255.0 или 11111111.11111111.11100000.00000000, или 192.168.0.49/23
# (где через "/" указано количество единиц в маске) при этом нужно отметить то, что перед 1
# не может быть нулей, а после 0 не может быть единиц.

# Начальная часть IP адресов в подсети совпадает (адрес сети), и определяется поразрядной
# конъюнкцией IP-адреса узла и маской сети.

# Адрес оканчивающийся в двоичном виде на все 1 - широковещательный
# Если IP адреса находятся в одной сети, то начальная часть после поразрядной конъюнкции
# всегда одинакова:

# msk = ["255", "255", "255", "240"]
# print(".".join(msk), "".join([f"{int(x):08b}" for x in msk]))
# for x in range(16):
#     ip = f'192.168.0.{x}'
#     print(ip + " " * (len(".".join(msk)) - len(ip)), "".join([f"{int(x):08b}" for x in ip.split(".")]))

# Существуют две версии IP:
# IPv4 - содержит 4 294 967 296 адресов, которые полностью исчерпаны;
# IPv6 - 3,4028236692093846346337460743177 * 10 ** 38 на мой и ваш век хватит за глаза ;)))

# ++/IPv4 - это 32-х битное число, которое разбивается на 4 блока по 8 бит, каждый блок
# представлен числом от 0 до 255 в двоичном виде. В случае если при переводе блока в
# двоичный вид число занимает меньше 8 бит, слева дописываются незначащие нули. Пример
# адреса: 135.12.171.214 - 10000111.00001100.10101011.11010110

# ++/IPv6 - это 128-и битное число, отображающееся как восемь групп четырёхзначных 16-ых
# чисел разделённых двоеточием. Пример адреса: 2001:0db8:11a3:09d7:1f34:8a2e:07a0:765d

# --------------------------- Адрес сети по IP и маске -------------------------------
# /----------------------------------- Задача ----------------------------------------/
# По заданным IP-адресу узла сети и маске определите адрес сети:
# IP-адрес: 135.12.171.214
# Маска: 255.255.248.0
# При записи ответа выберите из приведенных в таблице чисел 4 фрагмента четыре
# элемента IP-адреса и запишите в нужном порядке соответствующие им буквы без точек.
# | A | B | C | D | E | F| G| H
# |170|168|160|135|132|16|12| 0

# Для удобства решения аналитическим способом, все таки лучше кодом давать представление
# в двоичном виде
from ipaddress import *
# ip = "135.12.171.214"
# mask = "255.255.248.0"
# print(".".join([f"{int(x):>08b}" for x in ip.split(".")]))
# print(".".join([f"{int(x):>08b}" for x in mask.split(".")]))
# b - двоичная сс, 8 - количество разрядов, 0 - ведущие цифры, которые добиваются до 8,
# > - добавить слева, < - добавить справа

# Для программного решения нам потребуются методы и функции стандартной библиотеки ipaddress,
# которую мы будем импортировать в начале каждой программы
# # Программное решение
# from ipaddress import *
# ip = "135.12.171.214"
# mask = "255.255.248.0"
# net = ip_network(f"{ip}/{mask}", 0)  # используем функцию ip_adress(), сюда
# нужно подать адрес сети, но мы будем подавать ip адрес, а чтобы функция не
# дала нам ошибку, установим нестрогий режим при помощи нуля и функция произведет
# поразрядную конъюнкцию за нас
# print(net)

# ---------------------------------- 3-й байт маски ----------------------------------
# Для решения данной задачи нам потребуется использовать метод netmask
# /---------------------------------- Задача 1 ---------------------------------------/
# В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает,
# какая часть IP-адреса узла сети относится к адресу сети, а какая - к адресу узла в
# этой сети. Обычно маска записывается по тем же правилам, что и IP адрес в виде четырех
# байт, причем каждый байт это десятичное число. Адрес сети получается в результате
# применения поразрядной конъюнкции к заданному адресу узла и маске сети.
# Задание:
# Для узла с IP-адресом 220.128.112.42 адрес сети равен 220.128.96.0.
# Чему равен третий слева байт маски? Ответ напишите в виде десятичного числа.

# Аналитическое решение
# ipadr = "220.128.112.142"
# netadr = "220.128.96.0"
# print(".".join([f"{int(x):08b}" for x in ipadr.split(".")]))
# print(".".join([f"{int(x):08b}" for x in netadr.split(".")]))

# Решение кодом
# from ipaddress import *
# ipadr = "220.128.112.142"
# netadr = "220.128.96.0"
# for mask in range(33):
#     net = ip_network(f"{ipadr}/{mask}", 0)
#     if netadr in str(net):
#         print(net, net.netmask)
# /---------------------------------- Задача 2 ---------------------------------------/
# В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает,
# какая часть IP-адреса узла сети относится к адресу сети, а какая - к адресу узла в
# этой сети. Обычно маска записывается по тем же правилам, что и IP адрес в виде четырех
# байт, причем каждый байт это десятичное число. Адрес сети получается в результате
# применения поразрядной конъюнкции к заданному адресу узла и маске сети.
# Задание:
# Для узла с IP-адресом 111.81.208.27 адрес сети равен 111.81.192.0.
# Чему равно наименьшее возможное значение третьего слева байта маски? Ответ напишите
# в виде десятичного числа.

# Аналитическое решение
# ipadr = "111.81.208.27"
# netadr = "111.81.192.0"
# print(".".join([f"{int(x):08b}" for x in ipadr.split(".")]))
# print(".".join([f"{int(x):08b}" for x in netadr.split(".")]))

# Решение кодом
# from ipaddress import *
# ipadr = "111.81.208.27"
# netadr = "111.81.192.0"
# for mask in range(33):
#     net = ip_network(f"{ipadr}/{mask}", 0)
#     if netadr in str(net):
#         print(net, net.netmask)

# --------------------------- Количество единиц в маске -------------------------------
# /----------------------------------- Задача ----------------------------------------/
# В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает,
# какая часть IP-адреса узла сети относится к адресу сети, а какая - к адресу узла в
# этой сети. Обычно маска записывается по тем же правилам, что и IP адрес в виде четырех
# байт, причем каждый байт это десятичное число. Адрес сети получается в результате
# применения поразрядной конъюнкции к заданному адресу узла и маске сети.  Например, если
# IP адрес узла равен 131.32.255.131, а маска равна 255.255.240.0, то адрес сети равен
# 131.32.240.0
# Задание:
# Для узла с IP-адресом 148.195.140.28 адрес сети равен 148.195.140.0.
# Найдите наименьшее возможное количество единиц в двоичной записи маски? Ответ напишите
# в виде десятичного числа.

# Ручное решение
# ipadr = "148.195.140.28"
# netadr = "148.195.140.0"
# print(".".join([f"{int(x):08b}" for x in ipadr.split(".")]))
# print(".".join([f"{int(x):08b}" for x in netadr.split(".")]))

# Решение кодом
# from ipaddress import *
# ipadr = "148.195.140.28"
# netadr = "148.195.140.0"
# min_c1 = float("inf")
# for mask in range(33):
#     net = ip_network(f"{ipadr}/{mask}", 0)
#     if netadr in str(net):
#         if mask < min_c1:
#             min_c1 = mask
# print(min_c1)

# --------------------------- Количество нулей в маске -------------------------------
# /----------------------------------- Задача ----------------------------------------/
# В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает,
# какая часть IP-адреса узла сети относится к адресу сети, а какая - к адресу узла в
# этой сети. Обычно маска записывается по тем же правилам, что и IP адрес в виде четырех
# байт, причем каждый байт это десятичное число. Адрес сети получается в результате
# применения поразрядной конъюнкции к заданному адресу узла и маске сети.
# Задание:
# Для узла с IP-адресом 241.185.253.57 адрес сети равен 241.185.252.0.
# Найдите наименьшее возможное количество нулей в двоичной записи маски? Ответ напишите
# в виде десятичного числа.

# Ручное решение
# ipadr = "241.185.253.57"
# netadr = "241.185.252.0"
# print(".".join([f"{int(x):08b}" for x in ipadr.split(".")]))
# print(".".join([f"{int(x):08b}" for x in netadr.split(".")]))

# Решение кодом
# from ipaddress import *
# ipadr = "241.185.253.57"
# netadr = "241.185.252.0"
# min_c0 = float("inf")
# for mask in range(33):
#     net = ip_network(f"{ipadr}/{mask}", 0)
#     c0 = 32 - mask
#     if netadr in str(net):
#         if c0 < min_c0:
#             min_c0 = c0
# print(min_c0)

# -------------------------- Количество вариантов маски ------------------------------
# /----------------------------------- Задача ----------------------------------------/
# В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает,
# какая часть IP-адреса узла сети относится к адресу сети, а какая - к адресу узла в
# этой сети. Обычно маска записывается по тем же правилам, что и IP адрес в виде четырех
# байт, причем каждый байт это десятичное число. Адрес сети получается в результате
# применения поразрядной конъюнкции к заданному адресу узла и маске сети.
# Задание:
# Для узла с IP-адресом 76.155.48.2 адрес сети равен 76.155.48.0.
# Для скольких различных значений маски это возможно? Ответ напишите в виде десятичного
# числа.

# Ручное решение
# ipadr = "76.155.48.2"
# netadr = "76.155.48.0"
# print(".".join([f"{int(x):08b}" for x in ipadr.split(".")]))
# print(".".join([f"{int(x):08b}" for x in netadr.split(".")]))

# Решение кодом
# from ipaddress import *
# ipadr = "76.155.48.2"
# netadr = "76.155.48.0"
# # msk = []
# msk = 0
# for mask in range(33):
#     net = ip_network(f"{ipadr}/{mask}", 0)
#     if netadr in str(net):
#         # msk += [mask]
#         msk += 1
# # print(len(msk))
# print(msk)

# ----------------------------- IP-адреса в одной сети --------------------------------
# /----------------------------------- Задача ----------------------------------------/
# В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает,
# какая часть IP-адреса узла сети относится к адресу сети, а какая - к адресу узла в
# этой сети. Обычно маска записывается по тем же правилам, что и IP адрес в виде четырех
# байт, причем каждый байт это десятичное число. Адрес сети получается в результате
# применения поразрядной конъюнкции к заданному адресу узла и маске сети.
# Задание:
# Два узла, находящиеся в одной сети, имеют IP-адреса 112.117.107.70 и 112.117.121.80
# Укажите наибольшее возможное значение третьего слева байта маски? Ответ напишите в виде
# десятичного числа.

# Ручное решение
# ipadr = "112.117.107.70"
# ipadr2 = "112.117.121.80"
# print(".".join([f"{int(x):08b}" for x in ipadr.split(".")]))
# print(".".join([f"{int(x):08b}" for x in ipadr2.split(".")]))

# Решение кодом
# from ipaddress import *
# ipadr = "112.117.107.70"
# ipadr2 = "112.117.121.80"
# msk = []
# for mask in range(33):
#     net = ip_network(f"{ipadr}/{mask}", 0)
#     net2 = ip_network(f"{ipadr2}/{mask}", 0)
#     if net != net2:
#         continue
#     msk += [str(net.netmask).split(".")[2]]
# print(msk)

# ---------------------------- IP-адреса в разных сетях -------------------------------
# /----------------------------------- Задача ----------------------------------------/
# В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает,
# какая часть IP-адреса узла сети относится к адресу сети, а какая - к адресу узла в
# этой сети. Обычно маска записывается по тем же правилам, что и IP адрес в виде четырех
# байт, причем каждый байт это десятичное число. Адрес сети получается в результате
# применения поразрядной конъюнкции к заданному адресу узла и маске сети.
# Задание:
# Два узла, находящиеся в разных сетях, имеют IP-адреса 157.127.182.76 и 157.127.190.80
# В масках обеих подсетей одинаковое количество единиц. Укажите наименьшее возможное
# количество единиц в масках этих подсетей? Ответ напишите в виде десятичного числа.

# Ручное решение
# ipadr = "157.127.182.76"
# ipadr2 = "157.127.190.80"
# print(".".join([f"{int(x):08b}" for x in ipadr.split(".")]))
# print(".".join([f"{int(x):08b}" for x in ipadr2.split(".")]))

# Решение кодом
# from ipaddress import *
# ipadr = "157.127.182.76"
# ipadr2 = "157.127.190.80"
# msk = []
# for mask in range(33):
#     net = ip_network(f"{ipadr}/{mask}", 0)
#     net2 = ip_network(f"{ipadr2}/{mask}", 0)
#     if net == net2:
#         continue
#     msk += [int(".".join(f"{int(x):08b}" for x in str(net.netmask).split(".")).count("1"))]
# print(min(msk))

# ------------------------------ Количество IP-адресов. -------------------------------
# Для решения данной задачи нам потребуется дополнительно использовать метод num_address
# /---------------------------------- Задача 1 ---------------------------------------/
# В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает,
# какая часть IP-адреса узла сети относится к адресу сети, а какая - к адресу узла в
# этой сети. Обычно маска записывается по тем же правилам, что и IP адрес в виде четырех
# байт, причем каждый байт это десятичное число. Адрес сети получается в результате
# применения поразрядной конъюнкции к заданному адресу узла и маске сети.
# Задание:
# Для некоторой подсети используется маска 255.255.254.0. Сколько различных адресов
# компьютеров теоретически допускает эта маска, если два адреса (адрес сети и широкове-
# щательный) не используют?
# Ручное решение
# print(".".join([f"{int(x):08b}" for x in msk.split(".")]))

# Решение кодом
# from ipaddress import *
# adr = "0.0.0.0"  # с учетом того, что нет конкретики укажем любой адрес сети
# msk = "255.255.254.0"
# net = ip_network(f"{adr}/{msk}")
# print(net.num_addresses - 2)
# /---------------------------------- Задача 2 ---------------------------------------/
# В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает,
# какая часть IP-адреса узла сети относится к адресу сети, а какая - к адресу узла в
# этой сети. Обычно маска записывается по тем же правилам, что и IP адрес в виде четырех
# байт, причем каждый байт это десятичное число. Адрес сети получается в результате
# применения поразрядной конъюнкции к заданному адресу узла и маске сети.
# Задание:
# Для узла с IP адресом 108.133.75.91 адрес сети равен 108.133.75.64. Чему равно наибольшее
# количество возможных адресов в этой сети?
# Ручное решение
# ipadr = "108.133.75.91"
# adr = "108.133.75.64"
# print(".".join([f"{int(x):08b}" for x in ipadr.split(".")]))
# print(".".join([f"{int(x):08b}" for x in adr.split(".")]))

# Решение кодом
# from ipaddress import *
# ipadr = "108.133.75.91"
# adr = "108.133.75.64"
# c_adr = []
# for mask in range(33):
#     net = ip_network(f"{ipadr}/{mask}", 0)
#     if adr in str(net):
#         c_adr += [net.num_addresses]
# print(max(c_adr))
# /---------------------------------- Задача 3 ---------------------------------------/
# В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает,
# какая часть IP-адреса узла сети относится к адресу сети, а какая - к адресу узла в
# этой сети. Обычно маска записывается по тем же правилам, что и IP адрес в виде четырех
# байт, причем каждый байт это десятичное число. Адрес сети получается в результате
# применения поразрядной конъюнкции к заданному адресу узла и маске сети.
# Задание:
# Для узла с IP адресом 175.122.80.13 адрес сети равен 175.122.80.0. Сколько существует
# различных значений маски, если известно, что в этой сети не менее 60 узлов? Ответ
# запишите в виде десятичного числа.

# Ручное решение
# ipadr = "175.122.80.13"
# adr = "175.122.80.0"
# print(".".join([f"{int(x):08b}" for x in ipadr.split(".")]))
# print(".".join([f"{int(x):08b}" for x in adr.split(".")]))

# Решение кодом
# from ipaddress import *
# ipadr = "175.122.80.13"
# adr = "175.122.80.0"
# msk = []
# for mask in range(33):
#     net = ip_network(f"{ipadr}/{mask}", 0)
#     if adr in str(net) and net.num_addresses >= 60:
#         msk += [mask]
# print(len(msk))

# -------------------------------- Перебор IP-адресов. -------------------------------
# /---------------------------------- Задача 1 ---------------------------------------/
# В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает,
# какая часть IP-адреса узла сети относится к адресу сети, а какая - к адресу узла в
# этой сети. Обычно маска записывается по тем же правилам, что и IP адрес в виде четырех
# байт, причем каждый байт это десятичное число. Адрес сети получается в результате
# применения поразрядной конъюнкции к заданному адресу узла и маске сети.
# Задание:
# Сеть задана IP адресом 184.178.54.144 и маской сети 255.255.255.240. Сколько в этой
# сети IP-адресов, у которых в двоичной записи имеется сочетание трех подряд идущих
# единиц? Ответ запишите в виде десятичного числа.

# Ручное решение
# ipadr = "184.178.54.144"
# msk = "255.255.255.240"
# print(".".join([f"{int(x):08b}" for x in ipadr.split(".")]))
# print(".".join([f"{int(x):08b}" for x in msk.split(".")]))

# Решение кодом
# from ipaddress import *
# ipadr = "184.178.54.144"
# msk = "255.255.255.240"
# ip_c = []
# for ip in ip_network(f"{ipadr}/{msk}"):
#     b = f"{ip:b}"
#     if "111" in b:
#         ip_c += [b]
# print(len(ip_c))
# /---------------------------------- Задача 2 ---------------------------------------/
# В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает,
# какая часть IP-адреса узла сети относится к адресу сети, а какая - к адресу узла в
# этой сети. Обычно маска записывается по тем же правилам, что и IP адрес в виде четырех
# байт, причем каждый байт это десятичное число. Адрес сети получается в результате
# применения поразрядной конъюнкции к заданному адресу узла и маске сети.
# Задание:
# Сеть задана IP адресом 211.48.136.64 и маской сети 255.255.255.224. Сколько в этой
# сети IP-адресов которые в двоичной записи оканчиваются на две единицы? Ответ запишите
# в виде десятичного числа.

# Ручное решение
# ipadr = "211.48.136.64"
# msk = "255.255.255.224"
# print(".".join([f"{int(x):08b}" for x in ipadr.split(".")]))
# print(".".join([f"{int(x):08b}" for x in msk.split(".")]))

# Решение кодом
# from ipaddress import *
# ipadr = "211.48.136.64"
# msk = "255.255.255.224"
# ip_c = []
# for ip in ip_network(f"{ipadr}/{msk}"):
#     b = f"{ip:b}"
#     if b[-2:] == "11":
#         ip_c += [b]
# print(*ip_c,sep="\n")

# --------------------------- Номер компьютера в сети. ---------------------------------
# Для решения данной задачи нам потребуется функция ip_address(), которая преобразует
# строчную запись IP в формат IP адреса, который в свою очередь может быть преобразован
# с помощью int() в десятичное число.
# /---------------------------------- Задача ---------------------------------------/
# В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает,
# какая часть IP-адреса узла сети относится к адресу сети, а какая - к адресу узла в
# этой сети. Обычно маска записывается по тем же правилам, что и IP адрес в виде четырех
# байт, причем каждый байт это десятичное число. Адрес сети получается в результате
# применения поразрядной конъюнкции к заданному адресу узла и маске сети.
# Задание:
# IP адрес компьютера в сети 192.168.156.235, маска сети 255.255.255.240. Чему будет равен
# номер компьютера? Ответ запишите в виде десятичного числа.

# Ручное решение
# ipadr = 192.168.156.235"
# msk = "255.255.255.240"
# print(".".join([f"{int(x):08b}" for x in ipadr.split(".")]))
# print(".".join([f"{int(x):08b}" for x in msk.split(".")]))

# Решение кодом
# from ipaddress import *
# ipadr = ip_address("192.168.156.235")
# msk = "255.255.255.240"
# net = str(ip_network(f"{ipadr}/{msk}", 0))
# net = ip_address(net[:net.index("/")])
# print(int(ipadr) - int(net))

# ----------------------- Числовое значение IP-адреса. -----------------------------
# /---------------------------------- Задача ---------------------------------------/
# В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает,
# какая часть IP-адреса узла сети относится к адресу сети, а какая - к адресу узла в
# этой сети. Обычно маска записывается по тем же правилам, что и IP адрес в виде четырех
# байт, причем каждый байт это десятичное число. Адрес сети получается в результате
# применения поразрядной конъюнкции к заданному адресу узла и маске сети.
# Задание:
# Некоторая сеть имеет маску 255.255.128.0. Сколько в этой сети IP-адресов, для которых
# числовое значение четрёхбайтного IP-адреса кратно четырём? Ответ запишите в виде
# десятичного числа.

# Не знаю как вы, но я решаю эту задачку кодом)))
# from ipaddress import *
# net = "192.168.0.0"
# msk = "255.255.128.0"
# net = ip_network(f"{net}/{msk}", 0)
# c = 0
# for ip in net:  # ip_network хоть и возвращает правильный вид сети, позволяет в цикле пройтись
#     # по всем IP-адресам семи включая адрес сети и широковещательный, кстати извлекаемое значение
#     # имеет формат IP адреса и его не нужно дополнительно преобразовывать
#     if int(ip) % 4 == 0:
#         c += 1
# print(c)
