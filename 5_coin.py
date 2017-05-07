# Write a function that, given:
# - an amount of money
# - a list of coin denominations
# computes the number of ways to make the amount of money with coins of
# the available denominations.

# Recursive solution
def change_possibilities_top_down(amount_left, denominations, current_index=0):

    # base cases:
    # we hit the amount spot on. yes!
    if amount_left == 0: return 1

    # we overshot the amount left (used too many coins)
    if amount_left < 0: return 0

    # we're out of denominations
    if current_index == len(denominations): return 0

    print "checking ways to make %i with %s" % (amount_left, denominations[current_index:])

    # choose a current coin
    current_coin = denominations[current_index]

    # see how many possibilities we can get
    # for each number of times to use current_coin
    num_possibilities = 0
    while amount_left >= 0:
        num_possibilities += change_possibilities_top_down(amount_left, denominations, current_index + 1)
        print "num possibilities", num_possibilities
        amount_left -= current_coin
        print "amount left", amount_left

    return num_possibilities


# Memoize to avoid repeating calls
# O(n * m) time and O(n * m) space where n is the size of amount and m is the number of items in
# denominations. The recursive function will build a large call stack of size
# O(m)
class Change:
    def __init__(self):
        self.memo = {}

    def change_possibilities_memoize(self, amount_left, denominations, current_index=0):

        # check our memo and short-circuit if we've already solved this one
        memo_key = str((amount_left, current_index))
        if memo_key in self.memo:
            print "grabbing memo[%s]" % memo_key
            return self.memo[memo_key]

        # base cases:
        # we hit the amount spot on
        if amount_left == 0: return 1

        # we overshot the amount left (used too many coins)
        if amount_left < 0: return 0

        # we're out of denominations
        if current_index == len(denominations): return 0

        print "checking ways to make %i with %s" % (amount_left, denominations[current_index:])

        # choose a current coin
        current_coin = denominations[current_index]

        # see how many possibilities we can get for each number of times
        # to use current coin
        num_possibilities = 0
        while amount_left >= 0:
            num_possibilities += self.change_possibilities_memoize(amount_left, denominations, current_index + 1)
            amount_left -= current_coin

        # save the answer in our memo so we don't compute it again
        self.memo[memo_key] = num_possibilities
        print "memo", self.memo
        return num_possibilities

# Efficient solution - O(n) space
# Bottom-up
def change_possibilities_bottom_up(amount, denominations, index=0):

    # num_possibilities = 0
    # for coin in denominations:
    #     print "using %i coin" % coin
    #
    #     if (amount % coin == 0) :
    #         num_possibilities += 1
    #
    #         max_number_times_to_use_coin = amount / coin
    #
    #         for i in range(1, max_number_times_to_use_coin):
    #             print "outer i", i
    #             leftover_coins = denominations[index + 1:]
    #
    #             for other_coin in leftover_coins:
    #                 print "other coin", other_coin
    #
    #                 if (i*coin + other_coin == amount):
    #                     num_possibilities += 1
    #                     print "num_possibilities", num_possibilities
    #
    #     else:
    #         max_number_times_to_use_coin = int(amount / coin)
    #
    #     index += 1
    #
    # return num_possibilities

# Test
# Should output 3
# print(change_possibilities_top_down(4, [1, 2]))

# Should output 4
# print(change_possibilities_top_down(4, [1, 2, 3]))

# print(Change().change_possibilities_memoize(4, [1, 2, 3]))

print(change_possibilities_bottom_up(5, [1, 2]))
