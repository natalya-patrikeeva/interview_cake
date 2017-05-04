# Given a list of integers, find the highest product you can get from three of
# the integers.
# Efficient solution uses O(n) time and O(1) space.

# def get_highest_product_from_three_ints(input_list):
#
#     max_int = max(input_list)
#     neg_product = float("-inf")
#     product = float("-inf")
#
#     # Find three positive ints besides max or three negative ints
#     product_so_far = input_list[:3]
#
#     if all(input_list) < 0 or all(input_list) >= 0:
#         for i in input_list[3:]:
#             if any(i > x for x in product_so_far) :
#
#                 # get the index of min value in the running 3 value list
#                 index_min = product_so_far.index(min(product_so_far))
#
#                 # save value at i to the min index
#                 product_so_far[index_min] = i
#
#
#         product = product_so_far[0] * product_so_far[1] * product_so_far[2]
#
#     # If input list has at least two negative numbers but not all of them are
#     # negative. We need to keep two most negative ints and max positive.
#     if any(x < 0 for x in input_list) and any(x >= 0 for x in input_list):
#
#         neg_min = min(input_list)
#         neg_two = float("inf")
#
#         for i, value in enumerate(input_list):
#
#             # find second negative value that is different from min negative
#             if value < 0 and value < neg_two and i != input_list.index(neg_min) :
#                 neg_two = value
#
#         if neg_two != float("inf") :
#             neg_product = neg_min * neg_two * max_int
#
#         if neg_product > product:
#             return neg_product
#
#     return product

def get_highest_product_from_three_ints(input_list):

    high_product_of_3 = input_list[0] * input_list[1] * input_list[2]
    high_product_of_2 = input_list[0] * input_list[1]
    low_product_of_2  = input_list[0] * input_list[1]
    highest = max(input_list[:2])
    lowest  = min(input_list[:2])

    for i in input_list[2:] :

        high_product_of_3 = max(high_product_of_3,
                                high_product_of_2 * i,
                                low_product_of_2  * i)

        high_product_of_2 = max(high_product_of_2,
                                highest * i,
                                lowest  * i )
        low_product_of_2 = min(low_product_of_2,
                               highest * i,
                               lowest  * i)

        highest = max( i, highest )
        lowest  = min( i, lowest  )

    return high_product_of_3


# Testing
# normal case
# should return 300
print(get_highest_product_from_three_ints([10, 5, 0, 1, 3, 6]))

# edge cases?
# negative numbers
# should return 900
print(get_highest_product_from_three_ints( [-6, -15, 1, -30, 2] ))

# all negative numbers
# should return -12
print(get_highest_product_from_three_ints( [-6, -15, -1, -30, -2] ))

# negative ints and zeros
# should return 0
print(get_highest_product_from_three_ints( [-6, -15, -5, -30, 0] ))
