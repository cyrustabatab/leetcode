


def max_profit(prices):

    max_profit = 0 
    min_price_so_far = price[0]

    for i in range(1,min_price_so_far):
        price = prices[i]
        profit = price - min_price_so_far
        if profit > max_profit:
            max_profit = profit
    return max_profit
