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
# Выделяют четыре основных параметра:
#          -- IP адрес сети - идентификатор сети. Адрес оканчивающийся в двоичном виде на
#          все 0 - адрес сети
#          -- IP адрес узла - идентификатор компьютера в сети. Не может быть равен адресу
#          сети и широковещательному адресу.
#          -- Широковещательный адрес. При получении пакета, рассылает его на все узлы сети.
#          Адрес оканчивающийся в двоичном виде на все 1 - широковещательный.
#          -- Маска сети. Определяет, какая часть IP-адреса узла сети относится к адресу сети,
#          а какая к адресу самого узла в сети.
#          --- Маска имеет вид: 255.255.255.0 или 11111111.11111111.11100000.00000000, или
#          192.168.0.49/23 (где через "/" указано количество единиц в маске) при этом нужно
#          отметить то, что перед 1 не может быть нулей, а после 0 не может быть единиц.

# Начальная часть IP адресов в подсети совпадает (адрес сети), и определяется поразрядной
# конъюнкцией IP-адреса узла с маской сети.

# Если IP адреса находятся в одной сети, то начальная часть после поразрядной конъюнкции
# всегда одинакова:

# msk = ["255", "255", "255", "240"]
# print(".".join(msk), "".join([f"{int(x):08b}" for x in msk]))
# b - двоичная сс, 8 - количество разрядов, 0 - ведущие цифры, которые добиваются до 8,
# > - добавить слева, < - добавить справа
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
# /----------------------------------- Задача 1 ----------------------------------------/
# По заданным IP-адресу узла сети и маске определите адрес сети:
# IP-адрес: 135.12.171.214
# Маска: 255.255.248.0
# При записи ответа выберите из приведенных в таблице чисел 4 фрагмента четыре
# элемента IP-адреса и запишите в нужном порядке соответствующие им буквы без точек.
# Ответ: DGBH
# | A | B | C | D | E | F| G| H
# |170|168|160|135|132|16|12| 0

# И для программного, и для аналитического решения нам потребуются методы и функции
# стандартной библиотеки ipaddress, которую мы будем импортировать в начале каждой программы

# Для удобства решения аналитическим способом, все таки лучше кодом давать представление
# в двоичном виде
from ipaddress import *
# Все функции библиотеки возвращают объект формата ipaddress.IPv4Address, но они легко
# конвертируется в другие типы
print("--------------------- Задача 1 --------------------- ")
ip = ip_address("135.12.171.214")  # не сложно догадаться, что мы хотим получить
mask = ip_address("255.255.248.0")  # маску тоже можем преобразовать
print("IP   ", *[f"{ip:b}"[i - 8:i] for i in range(8, 33, 8)], sep=".")  # Обратите внимание, что
# в форматированную строку был передан ip адрес, который был преобразован в двоичный вид с
# автоматически добавленными слева незначащими нулями. Неудобство заключается в том, что
# результат дается одной строкой, но при помощи списочного выражения и срезов, создадим
# список восьмиразрядных двоичных чисел.
print("Mask ", *[f"{mask:b}"[i - 8:i] for i in range(8, 33, 8)], sep=".")
print("IPnet", *["________" for i in range(4)], sep=".")

# Программное решение
# from ipaddress import *
ip = ip_address("135.12.171.214")
mask = ip_address("255.255.248.0")
net = ip_network(f"{ip}/{mask}", False)  # для нахождения адреса сети используем функцию
# ip_network(), хотя её основное предназначение просто генерация адреса сети в виде
# объекта и в нее изначально нужно подавать сам адрес, но у функции есть дополнительный
# функционал (активируется при помощи аргумента - 0) в виде нестрогого режима, который
# при подаче ip адреса узла произведет поразрядную конъюнкцию за нас.
print(net)
input("Нажмите любую клавишу для продолжения")
# ---------------------------------- 3-й байт маски -------------------------------------
# Для решения данной задачи нам потребуется использовать метод netmask, который позволяет
# вытащить из сформированного объекта маску сети.
# ---------------------------------------------------------------------------------------
# /---------------------------------- Задача 2 ------------------------------------------/
# В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает,
# какая часть IP-адреса узла сети относится к адресу сети, а какая - к адресу узла в
# этой сети. Обычно маска записывается по тем же правилам, что и IP адрес в виде четырех
# байт, причем каждый байт это десятичное число. Адрес сети получается в результате
# применения поразрядной конъюнкции к заданному адресу узла и маске сети.
# Задание:
# Для узла с IP-адресом 220.128.112.42 адрес сети равен 220.128.96.0.
# Чему равен третий слева байт маски? Ответ напишите в виде десятичного числа.
# Ответ: 224
# from ipaddress import *
print("--------------------- Задача 2 --------------------- ")
# Аналитическое решение
ip = ip_address("220.128.112.142")
net = ip_address("220.128.96.0")
print("IP   ", *[f"{ip:b}"[i - 8:i] for i in range(8, 33, 8)], sep=".")
print("Mask ", *["________" for i in range(4)], sep=".")
print("IPnet", *[f"{net:b}"[i - 8:i] for i in range(8, 33, 8)], sep=".")

# Программное решение
# from ipaddress import *
ip = ip_address("220.128.112.142")
net = ip_address("220.128.96.0")
for mask in range(31):
    net_ = ip_network(f"{ip}/{mask}", False)
    if (net_[0] < ip < net_[-1]) and str(net) in str(net_):  # первым выражением проверяем,
        # что IP не является адресом сети и широковещательным адресом, вторым чтобы объект
        # содержал заданную сеть
        print(net_, str(net_.netmask).split(".")[2])
input("Нажмите любую клавишу для продолжения")
# /---------------------------------- Задача 3 ---------------------------------------/
# В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает,
# какая часть IP-адреса узла сети относится к адресу сети, а какая - к адресу узла в
# этой сети. Обычно маска записывается по тем же правилам, что и IP адрес в виде четырех
# байт, причем каждый байт это десятичное число. Адрес сети получается в результате
# применения поразрядной конъюнкции к заданному адресу узла и маске сети.
# Задание:
# Для узла с IP-адресом 111.81.208.27 адрес сети равен 111.81.192.0.
# Чему равно наименьшее возможное значение третьего слева байта маски? Ответ напишите
# в виде десятичного числа.
# Ответ: 192
# from ipaddress import *
# Аналитическое решение
print("--------------------- Задача 3 --------------------- ")
ip = ip_address("111.81.208.27")
net = ip_address("111.81.192.0")
print("IP   ", *[f"{ip:b}"[i - 8:i] for i in range(8, 33, 8)], sep=".")
print("Mask ", *["________" for i in range(4)], sep=".")
print("IPnet", *[f"{net:b}"[i - 8:i] for i in range(8, 33, 8)], sep=".")

# Программное решение
# from ipaddress import *
ip = ip_address("111.81.208.27")
net = ip_address("111.81.192.0")
for mask in range(33):
    net_ = ip_network(f"{ip}/{mask}", False)
    if (net_[0] < ip < net_[-1]) and str(net) in str(net_):
        print(net_, str(net_.netmask).split(".")[2])
input("Нажмите любую клавишу для продолжения")
# --------------------------- Количество единиц в маске -------------------------------
# /----------------------------------- Задача 4 ----------------------------------------/
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
# Ответ: 22
# from ipaddress import *
# Аналитическое решение
print("--------------------- Задача 4 --------------------- ")
ip = ip_address("148.195.140.28")
net = ip_address("148.195.140.0")
print("IP   ", *[f"{ip:b}"[i - 8:i] for i in range(8, 33, 8)], sep=".")
print("Mask ", *["________" for i in range(4)], sep=".")
print("IPnet", *[f"{net:b}"[i - 8:i] for i in range(8, 33, 8)], sep=".")

# Программное решение
# from ipaddress import *
ip = ip_address("148.195.140.28")
net = ip_address("148.195.140.0")
min_c1 = float("inf")  # положим в переменную самое большое положительное число
for mask in range(31):
    net_ = ip_network(f"{ip}/{mask}", False)
    if (net_[0] < ip < net_[-1]) and str(net) in str(net_):
        if mask < min_c1:
            min_c1 = mask
print(min_c1)
input("Нажмите любую клавишу для продолжения")
# --------------------------- Количество нулей в маске -------------------------------
# /----------------------------------- Задача 5 ----------------------------------------/
# В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает,
# какая часть IP-адреса узла сети относится к адресу сети, а какая - к адресу узла в
# этой сети. Обычно маска записывается по тем же правилам, что и IP адрес в виде четырех
# байт, причем каждый байт это десятичное число. Адрес сети получается в результате
# применения поразрядной конъюнкции к заданному адресу узла и маске сети.
# Задание:
# Для узла с IP-адресом 241.185.253.57 адрес сети равен 241.185.252.0.
# Найдите наименьшее возможное количество нулей в двоичной записи маски? Ответ напишите
# в виде десятичного числа.
# Ответ: 9
# from ipaddress import *
# Аналитическое решение
print("--------------------- Задача 5 --------------------- ")
ip = ip_address("241.185.253.57")
net = ip_address("241.185.252.0")
print("IP   ", *[f"{ip:b}"[i - 8:i] for i in range(8, 33, 8)], sep=".")
print("Mask ", *["________" for i in range(4)], sep=".")
print("IPnet", *[f"{net:b}"[i - 8:i] for i in range(8, 33, 8)], sep=".")

# Программное решение
# from ipaddress import *
ip = ip_address("241.185.253.57")
net = ip_address("241.185.252.0")
min_c0 = float("inf")
for mask in range(31):
    net_ = ip_network(f"{ip}/{mask}", False)
    c0 = 32 - mask  # 32 - это количество возможных нулей
    if (net_[0] < ip < net_[-1]) and str(net) in str(net_):
        if c0 < min_c0:
            min_c0 = c0
print(min_c0)
input("Нажмите любую клавишу для продолжения")
# -------------------------- Количество вариантов маски ------------------------------
# /----------------------------------- Задача 6 ----------------------------------------/
# В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает,
# какая часть IP-адреса узла сети относится к адресу сети, а какая - к адресу узла в
# этой сети. Обычно маска записывается по тем же правилам, что и IP адрес в виде четырех
# байт, причем каждый байт это десятичное число. Адрес сети получается в результате
# применения поразрядной конъюнкции к заданному адресу узла и маске сети.
# Задание:
# Для узла с IP-адресом 76.155.48.2 адрес сети равен 76.155.48.0.
# Для скольких различных значений маски это возможно? Ответ напишите в виде десятичного
# числа.
# Ответ: 11
# from ipaddress import *
# Аналитическое решение
print("--------------------- Задача 6 --------------------- ")
ip = ip_address("76.155.48.2")
net = ip_address("76.155.48.0")
print("IP   ", *[f"{ip:b}"[i - 8:i] for i in range(8, 33, 8)], sep=".")
print("Mask ", *["________" for i in range(4)], sep=".")
print("IPnet", *[f"{net:b}"[i - 8:i] for i in range(8, 33, 8)], sep=".")

# Программное решение
# from ipaddress import *
ip = ip_address("76.155.48.2")
net = ip_address("76.155.48.0")
msk_ = []
msk = 0
for mask in range(31):
    net_ = ip_network(f"{ip}/{mask}", False)
    if (net_[0] < ip < net_[-1]) and str(net) in str(net_):
        msk_ += [mask]
        msk += 1
print(len(msk_))
print(msk)
input("Нажмите любую клавишу для продолжения")
# ----------------------------- IP-адреса в одной сети --------------------------------
# /----------------------------------- Задача 7 ----------------------------------------/
# В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает,
# какая часть IP-адреса узла сети относится к адресу сети, а какая - к адресу узла в
# этой сети. Обычно маска записывается по тем же правилам, что и IP адрес в виде четырех
# байт, причем каждый байт это десятичное число. Адрес сети получается в результате
# применения поразрядной конъюнкции к заданному адресу узла и маске сети.
# Задание:
# Два узла, находящиеся в одной сети, имеют IP-адреса 112.117.107.70 и 112.117.121.80
# Укажите наибольшее возможное значение третьего слева байта маски? Ответ напишите в виде
# десятичного числа.
# Ответ: 224
# from ipaddress import *
# Аналитическое решение
print("--------------------- Задача 7 --------------------- ")
ip = ip_address("112.117.107.70")
ip2 = ip_address("112.117.121.80")
print("IP   ", *[f"{ip:b}"[i - 8:i] for i in range(8, 33, 8)], sep=".")
print("IP2  ", *[f"{ip2:b}"[i - 8:i] for i in range(8, 33, 8)], sep=".")
print("Mask ", *["________" for i in range(4)], sep=".")

# Программное решение
# from ipaddress import *
ip = ip_address("112.117.107.70")
ip2 = ip_address("112.117.121.80")
msk = []
for mask in range(31):
    net = ip_network(f"{ip}/{mask}", False)
    net2 = ip_network(f"{ip2}/{mask}", False)
    if net != net2:
        continue
    msk += [int(str(net.netmask).split(".")[2])]
print(max(msk))
input("Нажмите любую клавишу для продолжения")
# ---------------------------- IP-адреса в разных сетях -------------------------------
# /----------------------------------- Задача 8 ----------------------------------------/
# В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает,
# какая часть IP-адреса узла сети относится к адресу сети, а какая - к адресу узла в
# этой сети. Обычно маска записывается по тем же правилам, что и IP адрес в виде четырех
# байт, причем каждый байт это десятичное число. Адрес сети получается в результате
# применения поразрядной конъюнкции к заданному адресу узла и маске сети.
# Задание:
# Два узла, находящиеся в разных сетях, имеют IP-адреса 157.127.182.76 и 157.127.190.80
# В масках обеих подсетей одинаковое количество единиц. Укажите наименьшее возможное
# количество единиц в масках этих подсетей? Ответ напишите в виде десятичного числа.
# Ответ: 21
# from ipaddress import *
# Аналитическое решение
print("--------------------- Задача 8 --------------------- ")
ip = ip_address("157.127.182.76")
ip2 = ip_address("157.127.190.80")
print("IP   ", *[f"{ip:b}"[i - 8:i] for i in range(8, 33, 8)], sep=".")
print("IP2  ", *[f"{ip2:b}"[i - 8:i] for i in range(8, 33, 8)], sep=".")
print("Mask ", *["________" for i in range(4)], sep=".")

# Программное решение
# from ipaddress import *
ip = ip_address("157.127.182.76")
ip2 = ip_address("157.127.190.80")
msk = []
for mask in range(31):
    net = ip_network(f"{ip}/{mask}", False)
    net2 = ip_network(f"{ip2}/{mask}", False)
    if net == net2:
        continue
    msk += [mask]
print(min(msk))
input("Нажмите любую клавишу для продолжения")
# ------------------------------ Количество IP-адресов. -------------------------------
# Для решения данной задачи нам потребуется дополнительно использовать метод num_address,
# который позволяет вернуть количество IP адресов в сети.
# /---------------------------------- Задача 9 ---------------------------------------/
# В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает,
# какая часть IP-адреса узла сети относится к адресу сети, а какая - к адресу узла в
# этой сети. Обычно маска записывается по тем же правилам, что и IP адрес в виде четырех
# байт, причем каждый байт это десятичное число. Адрес сети получается в результате
# применения поразрядной конъюнкции к заданному адресу узла и маске сети.
# Задание:
# Для некоторой подсети используется маска 255.255.254.0. Сколько различных адресов
# компьютеров теоретически допускает эта маска, если два адреса (адрес сети и широкове-
# щательный) не используют?
# Ответ: 510
# from ipaddress import *
# Аналитическое решение
print("--------------------- Задача 9 --------------------- ")
mask = ip_address("255.255.254.0")
print("Mask ", *[f"{mask:b}"[i - 8:i] for i in range(8, 33, 8)], sep=".")
print("IPnet", *["________" for i in range(4)], sep=".")

# Программное решение
# from ipaddress import *
net = ip_address("0.0.0.0")  # с учетом того, что нет конкретики укажем любой адрес сети
mask = ip_address("255.255.254.0")
net_ = ip_network(f"{net}/{mask}")
print(net_.num_addresses - 2)
input("Нажмите любую клавишу для продолжения")
# /---------------------------------- Задача 10 ---------------------------------------/
# В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает,
# какая часть IP-адреса узла сети относится к адресу сети, а какая - к адресу узла в
# этой сети. Обычно маска записывается по тем же правилам, что и IP адрес в виде четырех
# байт, причем каждый байт это десятичное число. Адрес сети получается в результате
# применения поразрядной конъюнкции к заданному адресу узла и маске сети.
# Задание:
# Для узла с IP адресом 108.133.75.91 адрес сети равен 108.133.75.64. Чему равно наибольшее
# количество возможных адресов в этой сети?
# Ответ: 64
# from ipaddress import *
# Аналитическое решение
print("--------------------- Задача 10 --------------------- ")
ip = ip_address("108.133.75.91")
net = ip_address("108.133.75.64")
print("IP   ", *[f"{ip:b}"[i - 8:i] for i in range(8, 33, 8)], sep=".")
print("Mask ", *["________" for i in range(4)], sep=".")
print("IPnet", *[f"{net:b}"[i - 8:i] for i in range(8, 33, 8)], sep=".")

# Программное решение
# from ipaddress import *
ip = ip_address("108.133.75.91")
net = ip_address("108.133.75.64")
c_adr = []
for mask in range(31):
    net_ = ip_network(f"{ip}/{mask}", False)
    if net_[0] < ip < net_[-1] and str(net) in str(net_):
        c_adr += [net_.num_addresses]
print(max(c_adr))
input("Нажмите любую клавишу для продолжения")
# /---------------------------------- Задача 11 ---------------------------------------/
# В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает,
# какая часть IP-адреса узла сети относится к адресу сети, а какая - к адресу узла в
# этой сети. Обычно маска записывается по тем же правилам, что и IP адрес в виде четырех
# байт, причем каждый байт это десятичное число. Адрес сети получается в результате
# применения поразрядной конъюнкции к заданному адресу узла и маске сети.
# Задание:
# Для узла с IP адресом 175.122.80.13 адрес сети равен 175.122.80.0. Сколько существует
# различных значений маски, если известно, что в этой сети не менее 60 узлов? Ответ
# запишите в виде десятичного числа.
# Ответ: 7
# from ipaddress import *
# Аналитическое решение
print("--------------------- Задача 11 --------------------- ")
ip = ip_address("175.122.80.13")
net = ip_address("175.122.80.0")
print("IP   ", *[f"{ip:b}"[i - 8:i] for i in range(8, 33, 8)], sep=".")
print("Mask ", *["________" for i in range(4)], sep=".")
print("IPnet", *[f"{net:b}"[i - 8:i] for i in range(8, 33, 8)], sep=".")

# Программное решение
# from ipaddress import *
ip = ip_address("175.122.80.13")
net = ip_address("175.122.80.0")
msk = []
for mask in range(31):
    net_ = ip_network(f"{ip}/{mask}", False)
    if (net_[0] < ip < net_[-1]) and (str(net) in str(net_)) and net_.num_addresses >= 60:
        msk += [mask]
print(len(msk))
input("Нажмите любую клавишу для продолжения")
# -------------------------------- Перебор IP-адресов. -------------------------------
# /---------------------------------- Задача 12 ---------------------------------------/
# В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает,
# какая часть IP-адреса узла сети относится к адресу сети, а какая - к адресу узла в
# этой сети. Обычно маска записывается по тем же правилам, что и IP адрес в виде четырех
# байт, причем каждый байт это десятичное число. Адрес сети получается в результате
# применения поразрядной конъюнкции к заданному адресу узла и маске сети.
# Задание:
# Сеть задана IP адресом 184.178.54.144 и маской сети 255.255.255.240. Сколько в этой
# сети IP-адресов, у которых в двоичной записи имеется сочетание трех подряд идущих
# единиц? Ответ запишите в виде десятичного числа.
# Ответ: 16
# from ipaddress import *
# Аналитическое решение
print("--------------------- Задача 12 --------------------- ")
ip = ip_address("184.178.54.144")
mask = ip_address("255.255.255.240")
print("IP   ", *[f"{ip:b}"[i - 8:i] for i in range(8, 33, 8)], sep=".")
print("Mask ", *[f"{mask:b}"[i - 8:i] for i in range(8, 33, 8)], sep=".")
print("IPnet", *["________" for i in range(4)], sep=".")

# Программное решение
# from ipaddress import *
ip = ip_address("184.178.54.144")
mask = ip_address("255.255.255.240")
net = ip_network(f"{ip}/{mask}")
ip_c = []
for ip in net:
    b = f"{ip:b}"
    if "111" in b:
        ip_c += [b]
print(len(ip_c))
# Всё то же самое, но записано в одну строчку при помощи списочного выражения
print(len([f"{ip:b}" for ip in net if "111" in f"{ip:b}"]))
input("Нажмите любую клавишу для продолжения")
# /---------------------------------- Задача 13 ---------------------------------------/
# В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает,
# какая часть IP-адреса узла сети относится к адресу сети, а какая - к адресу узла в
# этой сети. Обычно маска записывается по тем же правилам, что и IP адрес в виде четырех
# байт, причем каждый байт это десятичное число. Адрес сети получается в результате
# применения поразрядной конъюнкции к заданному адресу узла и маске сети.
# Задание:
# Сеть задана IP адресом 211.48.136.64 и маской сети 255.255.255.224. Сколько в этой
# сети IP-адресов которые в двоичной записи оканчиваются на две единицы? Ответ запишите
# в виде десятичного числа.
# Ответ: 8
# from ipaddress import *
# Аналитическое решение
print("--------------------- Задача 13 --------------------- ")
ip = ip_address("211.48.136.64")
mask = ip_address("255.255.255.224")
print("IP   ", *[f"{ip:b}"[i - 8:i] for i in range(8, 33, 8)], sep=".")
print("Mask ", *[f"{mask:b}"[i - 8:i] for i in range(8, 33, 8)], sep=".")
print("IPnet", *["________" for i in range(4)], sep=".")

# Программное решение
# from ipaddress import *
ip = ip_address("211.48.136.64")
mask = ip_address("255.255.255.224")
ip_c = []
for ip in ip_network(f"{ip}/{mask}"):
    b = f"{ip:b}"
    if b[-2:] == "11":
        ip_c += [b]
print(*ip_c, sep="\n")
print(len(ip_c))
input("Нажмите любую клавишу для продолжения")
# --------------------------- Номер компьютера в сети. ---------------------------------
# Для решения данной задачи нам потребуется функция ip_address(), которая преобразует
# строчную запись IP в формат IP адреса, который в свою очередь может быть преобразован
# с помощью int() в десятичное число. Номер компьютера в сети - это разница между
# целочисленными значениями IP адреса узла и IP адреса сети.
# /---------------------------------- Задача 14 ---------------------------------------/
# В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает,
# какая часть IP-адреса узла сети относится к адресу сети, а какая - к адресу узла в
# этой сети. Обычно маска записывается по тем же правилам, что и IP адрес в виде четырех
# байт, причем каждый байт это десятичное число. Адрес сети получается в результате
# применения поразрядной конъюнкции к заданному адресу узла и маске сети.
# Задание:
# IP адрес компьютера в сети 192.168.156.235, маска сети 255.255.255.240. Чему будет равен
# номер компьютера? Ответ запишите в виде десятичного числа.
# Ответ: 11
# from ipaddress import *
# Аналитическое решение
print("--------------------- Задача 14 --------------------- ")
ip = ip_address("192.168.156.235")
mask = ip_address("255.255.255.240")
print("IP   ", *[f"{ip:b}"[i - 8:i] for i in range(8, 33, 8)], sep=".")
print("Mask ", *[f"{mask:b}"[i - 8:i] for i in range(8, 33, 8)], sep=".")
print("IPnet", *["________" for i in range(4)], sep=".")

# Программное решение
# from ipaddress import *
ip = ip_address("192.168.156.235")
mask = ip_address("255.255.255.240")
net = str(ip_network(f"{ip}/{mask}", False))
net = ip_address(net.split("/")[0])
print(int(ip) - int(net))
input("Нажмите любую клавишу для продолжения")
# ----------------------- Числовое значение IP-адреса. -----------------------------
# /---------------------------------- Задача 15 ---------------------------------------/
# В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает,
# какая часть IP-адреса узла сети относится к адресу сети, а какая - к адресу узла в
# этой сети. Обычно маска записывается по тем же правилам, что и IP адрес в виде четырех
# байт, причем каждый байт это десятичное число. Адрес сети получается в результате
# применения поразрядной конъюнкции к заданному адресу узла и маске сети.
# Задание:
# Некоторая сеть имеет маску 255.255.128.0. Сколько в этой сети IP-адресов, для которых
# числовое значение четырёхбайтного IP-адреса кратно четырём? Ответ запишите в виде
# десятичного числа.
# Ответ: 8192
# from ipaddress import *
# Не знаю как вы, но я решаю эту задачку кодом)))
print("--------------------- Задача 15 --------------------- ")
net = ip_address("0.0.0.0")  # Опять, адрес сети не задан, так что берём любой
mask = ip_address("255.255.128.0")
net = ip_network(f"{net}/{mask}")  # Вот здесь нолик не нужен в качестве дополнительного аргумента
c = 0
for ip in net:  # ip_network хоть и возвращает правильный вид сети, позволяет в цикле пройтись
    # по всем IP-адресам сети включая адрес сети и широковещательный, кстати извлекаемое значение
    # имеет формат IP адреса и его не нужно дополнительно преобразовывать
    if int(ip) % 4 == 0:
        c += 1
print(c)
