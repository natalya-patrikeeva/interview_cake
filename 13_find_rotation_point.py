# Write a function for finding the index of the "rotation point," which is
 # where I started working from the beginning of the dictionary.

 # O(lg(n)) time - Binary search
 # O(1) - constant space complexity
def find_rotation_point(input_list) :

    if not input_list :
        raise Exception("Input list must not be empty")

    if len(input_list) == 1:
        raise Exception("Input list contains only one word")

    floor_index = 0
    ceiling_index = len(input_list) - 1

    if input_list[floor_index] < input_list[ceiling_index] :
        # fully sorted already
        return 0

    while floor_index + 1 != ceiling_index :
        guess = ( floor_index + ceiling_index ) / 2

        if input_list[guess] < input_list[ceiling_index] :
            # list is increasing monotonically.
            # the rotation point is to the left of guess index
            ceiling_index = guess

        else:
            # guess > ceiling
            # rotaion point is to the right of guess index
            floor_index = guess

    return ceiling_index

# Test
# should return 4
print(find_rotation_point( [10, 11, 12, 13, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9] ))

# should return 0
print(find_rotation_point( [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] ))

# test with strings
words = ['ptolemaic', 'retrograde', 'supplant', 'undulate', 'xenoepist', \
         'asymptote', 'babka', 'banoffee', 'engender', 'karpatka', \
         'othellolagkage']
print(find_rotation_point(words))

# end cases:
# empty list
print(find_rotation_point([]))
# one word
print(find_rotation_point([1]))
