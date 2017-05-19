# Write a function that takes an integer n and returns the nth fibonacci number.

# recursive
# Runtime is O(2^n) exponential!
def fib(n):

    if n in [0, 1] :
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(8))

# memoize
# store already calculated results in a dictionary
# O(n) time
# O(n) space for dictionary
# O(n) space for a call stack
class Fib:
    def __init__(self) :
        # initialize empty dictionary to store precomputed fib() for
        # lesser integers

        self.fib_seen = {}

    def fib_memoize(self, n):

        if n in [0, 1] :
            return n

        # check if we've already computed fib() for this integer
        if n in self.fib_seen :
            return self.fib_seen[n]


        result = self.fib_memoize(n - 1) + self.fib_memoize(n - 2)
        self.fib_seen[n] = result
        return result

# test
print(Fib().fib_memoize(7))


# Bottom-up solution
# O(n) time and O(1) space 
def fib_bottom_up(n):
    if n in [0, 1] :
        return n

    else :
        result = 1
        for i in range(2, n-1) :
            result += i
        return result

print(fib_bottom_up(8))
