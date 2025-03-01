import timeit

def find_coins_greedy(amount, coins=None):
    if coins:
        coins = sorted(coins)
    else:
        coins = [1, 2, 5, 10, 25, 50]
    result = {}

    while amount > 0 and coins:
        denomination = coins.pop()
        coins_amount = amount // denomination
        if coins_amount:
            result[denomination] = coins_amount
            amount -= coins_amount * denomination

    return result

def find_min_coins(amount, coins=None):
    if not coins:
        coins = [1, 2, 5, 10, 25, 50]
    
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    return result


amounts = [2, 12, 23, 95, 113, 2414, 21938]
n = 1000
print("--------Test [1, 2, 5, 10, 25, 50]--------")
for amount in amounts:
    print("Кількість коштів:", amount)

    greedy_result = find_coins_greedy(amount)
    dynamic_result = find_min_coins(amount)

    print(f"Жадібний алгоритм: {greedy_result}")
    print(f"Динамічне програмування: {dynamic_result}")

    greedy_time = timeit.timeit(lambda money_amount=amount: find_coins_greedy(money_amount), number=n)
    print(f"Жадібний алгоритм: {greedy_time}")

    dynamic_time = timeit.timeit(lambda money_amount=amount: find_min_coins(money_amount), number=n)
    print(f"Динамічне програмування: {dynamic_time}")

    print()

print("--------Test [1, 6, 9, 15]--------")
amounts = [2, 12, 23, 95, 113, 2414, 21938]
n = 1000
coins = [1, 6, 9, 15]
for amount in amounts:
    print("Кількість коштів:", amount)

    greedy_result = find_coins_greedy(amount, coins)
    dynamic_result = find_min_coins(amount, coins)

    print(f"Жадібний алгоритм: {greedy_result}")
    print(f"Динамічне програмування: {dynamic_result}")

    greedy_time = timeit.timeit(lambda money_amount=amount, denomination=coins: find_coins_greedy(money_amount, denomination), number=n)
    print(f"Жадібний алгоритм: {greedy_time}")

    dynamic_time = timeit.timeit(lambda money_amount=amount, denomination=coins: find_min_coins(money_amount, denomination), number=n)
    print(f"Динамічне програмування: {dynamic_time}")

    print()
