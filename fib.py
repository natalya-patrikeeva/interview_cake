def fib_recursive(n):

    if n < 0:
        raise IndexError('Index was negative. No such thing as a negative index in a series.')

    # base cases
    if n in [0, 1]:
        return n

    print "computing fib_recursive(%i)" % n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

print(fib_recursive(5))



# Memoization
class Fibber:

    def __init__(self):
        self.memo = {}

    def fib(self, n):
        if n < 0:
            raise IndexError('Index was negative. No such thing as a negative index in a series.')

        # base cases
        if n in [0, 1]:
            return n

        # see if we've already calculated this
        if n in self.memo:
            print "grabbing memo[%i]" % n
            return self.memo[n]

        print "computing fib(%i)" % n
        result = self.fib(n - 1) + self.fib(n - 2)

        # memoize
        self.memo[n] = result

        return result

print(Fibber().fib(4))
