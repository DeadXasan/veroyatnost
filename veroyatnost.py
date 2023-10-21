# Задание №1. Из колоды в 52 карты извлекаются случайным образом 4 карты.
#     a) Найти вероятность того, что все карты – крести.
#     б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.

import math

# Общее количество карт и количество карт в одной масти
total_cards = 52
cards_per_suit = 13

# Количество извлеченных карт
drawn_cards = 4

# a) Вероятность того, что все карты – крести
probability_all_spades = math.comb(cards_per_suit, drawn_cards) / math.comb(total_cards, drawn_cards)

# b) Вероятность, что среди 4-х карт окажется хотя бы один туз
probability_no_aces = math.comb(total_cards - 4, drawn_cards) / math.comb(total_cards, drawn_cards)
probability_at_least_one_ace = 1 - probability_no_aces

print("a) Вероятность, что все карты – крести:", probability_all_spades)
print("b) Вероятность, что среди 4-х карт окажется хотя бы один туз:", probability_at_least_one_ace)


# # Задание №2. На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9.
# #     Код содержит три цифры, которые нужно нажать одновременно.
# #     Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?

# import math

# # Вычисляем количество способов выбрать 3 цифры из 10
# total_ways = math.comb(10, 3)

# # Вероятность открыть дверь с первой попытки
# probability = 1 / total_ways

# print(f"Вероятность открыть дверь с первой попытки: {probability:.5f}")


# # Задание №3. В ящике имеется 15 деталей, из которых 9 окрашены.
# #     Рабочий случайным образом извлекает 3 детали.
# #     Какова вероятность того, что все извлеченные детали окрашены?

# import math

# # Функция для вычисления комбинаторного числа C(n, k)
# def combinations(n, k):
#     return math.comb(n, k)

# # Количество способов выбрать 3 окрашенные детали из 9
# ways_to_choose_3_painted = combinations(9, 3)

# # Количество способов выбрать 3 детали из 15
# total_ways_to_choose_3 = combinations(15, 3)

# # Вычисление вероятности
# probability = ways_to_choose_3_painted / total_ways_to_choose_3

# print(f"Вероятность, что все извлеченные детали окрашены: {probability:.4f}")


# # Задание №4. В лотерее 100 билетов. Из них 2 выигрышных.
# #     Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?

# # Вероятность выигрыша первого билета
# prob_first_ticket = 2/100

# # Вероятность выигрыша второго билета после выигрыша первого
# prob_second_ticket = 1/99

# # Вычисление общей вероятности
# probability = prob_first_ticket * prob_second_ticket

# print(f"Вероятность, что оба билета окажутся выигрышными: {probability:.4f}")
