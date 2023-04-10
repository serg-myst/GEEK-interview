'''
Написать программу "Банковский депозит".
Клиент банка делает депозит на определенный срок. В зависимости от суммы и срока вклада определяется
процентная ставка:
1000-10000 руб. (6 месяцев - 5% годовых, год - 6% годовых, 2 и более года - 5% годовых).
10000-100000 руб. (6 месяцев - 6% годовых, год - 7% годовых, 2 и более года - 6,5% годовых).
100000-1000000 руб. (6 месяцев - 7% годовых, год - 8% годовых, 2 и более года - 7,5% годовых).

Необходимо написать функцию, в которую будут будут передаваться параметры: сумма вклада и срок вклада (в месяцах),
а на выходе возвращать сумму вклада на конец срока
'''

# Для красоты выносим в отдельный файл
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
def get_deposit_sum(deposit_sum, months):
    perсents = get_percents(deposit_sum, BANK_DEPOSIT)
    if len(perсents) == 0:
        print('Извините, нет подходящих вкладов (')
        return []
    percent = get_percent(months, perсents)
    if percent == 0:
        print('Извините, нет подходящих вкладов (')
        return 0
    profit = 0
    for m in range(months):
        profit += deposit_sum * (percent / 100 / 12)
    return deposit_sum + profit


if __name__ == '__main__':
    months = 26
    deposit_sum = 10000
    total = get_deposit_sum(deposit_sum, months)
    if total > 0:
        print(f'Сумма депозита {deposit_sum} на {months} месяцев. Доход = {round(total, 2)}')
