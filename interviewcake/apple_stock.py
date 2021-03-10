# -*- coding: utf-8 -*-
"""
 Suppose we could access yesterday's stock prices as a list, where:

    The values are the price in dollars of Apple stock.
    A higher index indicates a later time.

So if the stock cost $500 at 10:30am and $550 at 11:00am, then:

stock_prices_yesterday[60] = 500

Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

For example:

  stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices_yesterday)
# returns 6 (buying for $5 and selling for $11)

No "shorting"—you must buy before you sell. You may not buy and sell in the same time step (at least 1 minute must pass).
"""


def get_max_profit(stock_prices_yesterday):
    """

    :param stock_prices_yesterday: list of stock prices. Must have at least 2 elements
    :return: best profit that could have been gained throughout the day
    """
    min_price = stock_prices_yesterday[0]
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

    for current_price in stock_prices_yesterday[1:]:
        # see what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)

        # update min_price so it's always
        # the lowest price we've seen so far
        min_price = min(min_price, current_price)

    return max_profit


def get_max_profit_brute(stock_prices_yesterday):
    """

    :param stock_prices_yesterday: list of stock prices. Must have at least 2 elements
    :return: best profit that could have been gained throughout the day
    """
    n = len(stock_prices_yesterday)
    return max([
        max([stock_prices_yesterday[j] - stock_prices_yesterday[i] for j in range(i + 1, n)])
        for i in range(n - 1)
    ])


assert get_max_profit([10, 7, 5, 8, 11, 9]) == 6
assert get_max_profit([10, 10, 9, 7]) == 0
assert get_max_profit([10, 10, 9, 7]) == 0
assert get_max_profit([10, 3, 1, 16]) == 15
assert get_max_profit([10, 1, 3, 16]) == 15


assert get_max_profit_brute([10, 7, 5, 8, 11, 9]) == 6
assert get_max_profit_brute([10, 10, 9, 7]) == 0
assert get_max_profit_brute([10, 10, 9, 7]) == 0
assert get_max_profit_brute([10, 3, 1, 16]) == 15
assert get_max_profit_brute([10, 1, 3, 16]) == 15




