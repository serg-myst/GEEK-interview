'''
Усовершенствовать программу «Банковский депозит». Третьим аргументом в функцию должна передаваться
фиксированная ежемесячная сумма пополнения вклада. Необходимо в главной функции реализовать вложенную
функцию подсчета процентов для пополняемой суммы. Примем, что клиент вносит средства в последний день
каждого месяца, кроме первого и последнего. Например, при сроке вклада в 6 месяцев пополнение происходит
в течение 4 месяцев. Вложенная функция возвращает сумму дополнительно внесенных средств (с процентами),
а главная функция — общую сумму по вкладу на конец периода.
'''

BANK_DEPOSIT = [
    {
        'start': 1000,
        'end': 10000,
        'value': [
            {'start': 6,
             'end': 6,
             'value': 5
             },
            {'start': 12,
             'end': 12,
             'value': 6
             },
            {'start': 24,
             'end': 999999,
             'value': 5
             }
        ]
    },
    {
        'start': 10000,
        'end': 100000,
        'value': [
            {'start': 6,
             'end': 6,
             'value': 6
             },
            {'start': 12,
             'end': 12,
             'value': 7
             },
            {'start': 24,
             'end': 999999,
             'value': 6.5
             }
        ]
    },
    {
        'start': 100000,
        'end': 1000000,
        'value': [
            {'start': 6,
             'end': 6,
             'value': 7
             },
            {'start': 12,
             'end': 12,
             'value': 8
             },
            {'start': 24,
             'end': 999999,
             'value': 7.5
             }
        ]
    }
]


# Функция возвращает список диапазонов процентных ставок по месяцам.
# Если не находим, то возвращаем пустой список
def get_percents(deposit_sum, bank_list):
    for rate in bank_list:
        if rate['start'] <= deposit_sum <= rate['end']:
            return rate['value']
    return []


# Если не находим, то возвращаем пустой список
def get_percent(month, bank_list):
    for rate in bank_list:
        if rate['start'] <= month <= rate['end']:
            return rate['value']
    return 0


# Без капитализации. От суммы вклада считаем годовой процент и в конце прибавляем прибыль
def get_deposit_sum(deposit_sum, months, add_sum=0):
    perсents = get_percents(deposit_sum, BANK_DEPOSIT)
    if len(perсents) == 0:
        print('Извините, нет подходящих вкладов (')
        return []
    percent = get_percent(months, perсents)
    if percent == 0:
        print('Извините, нет подходящих вкладов (')
        return 0

    def add_deposit():
        add_profit = 0
        for m in range(months):
            if m != 0 and m != months - 1:
                add_profit += add_sum * (percent / 100 / 12)
        return add_profit

    profit = 0
    for m in range(months):
        profit += deposit_sum * (percent / 100 / 12)
    return deposit_sum + profit + add_deposit()


if __name__ == '__main__':

    months = 26  # срок вклада
    deposit_sum = 10000  # сумма вклада
    add_sum = 1000  # сумма дополнительных вложений

    total = get_deposit_sum(deposit_sum, months, add_sum)
    if total > 0:
        print(f'Сумма депозита {deposit_sum} на {months} месяцев. Доход = {round(total, 2)}')
