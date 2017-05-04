# Write an efficient function that takes stock_prices_yesterday and returns the
# best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.
stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

# Brute force
# O(n^2) time
def get_max_profit(stocks) :

    # report negative profit if all prices went down after the buy
    profit = float("-inf")

    for b, buy in enumerate(stocks):

        for sell in stocks[b+1:]:
            profit = max(profit, (sell - buy))


    print "profit ", profit
    return profit

# Efficient implementation: O(n) time and O(1) space
# Greedy approach - loop through the list once
def get_max_profit_efficient(stocks):
    ##### check inputs ######
    # list is not empty and contains at least 2 prices
    if len(stocks) < 2 :
        raise IndexError("Input stock list needs to contain at least 2 prices")

    # list contains all int's
    if not all( isinstance(stock, int) for stock in stocks ):
        raise TypeError("Input prices must be integers")

    min_price = stocks[0]
    profit = stocks[1] - stocks[0]

    for current_price in stocks[1:]:

        # keep track of the profit so far
        # if we bought at min price and sold at current price
        profit = max(profit, ( current_price - min_price ) )

        # keep track of the lowest price so far
        min_price = min(min_price, current_price)

    print "profit efficient", profit
    return profit

# Testing 
get_max_profit(stock_prices_yesterday)
get_max_profit_efficient(stock_prices_yesterday)
get_max_profit_efficient([10, 8, 5, 2])
get_max_profit_efficient([10, 3])
get_max_profit_efficient([])
get_max_profit_efficient(["0", "10"])
get_max_profit_efficient([0])
# returns 6 (buying for $5 and selling for $11)
