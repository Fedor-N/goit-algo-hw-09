import time


def find_coins_greedy(amount):
    start_time = time.time()  # Фіксуємо час початку виконання функції
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount >= coin:
            num = amount // coin
            result[coin] = num
            amount -= num * coin
    end_time = time.time()  # Фіксуємо час завершення виконання функції
    execution_time = end_time - start_time  # Визначаємо час виконання функції
    return result, execution_time


def find_min_coins(amount):
    start_time = time.time()
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    last_coin = [-1] * (amount + 1)

    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                last_coin[x] = coin

    result = {}
    x = amount
    while x > 0:
        result[last_coin[x]] = result.get(last_coin[x], 0) + 1
        x -= last_coin[x]

    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time


# Приклад використання функцій та виведення часу виконання:
amount = 113
result_greedy, time_greedy = find_coins_greedy(amount)
result_dynamic, time_dynamic = find_min_coins(amount)

print("Greedy Algorithm:", result_greedy)
print("Execution Time (Greedy Algorithm):", time_greedy)

print("Dynamic Programming:", result_dynamic)
print("Execution Time (Dynamic Programming):", time_dynamic)
