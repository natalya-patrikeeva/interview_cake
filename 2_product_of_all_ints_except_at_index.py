# Write a function get_products_of_all_ints_except_at_index() that takes a list
# of integers and returns a list of the products.
# Do not use division in your solution.

# Brute force
# O(n^2) time and O(n) space
def get_products_of_all_ints_except_at_index(input_list):
    output_list = []

    for out_index, outer in enumerate(input_list):
        product = 1

        for in_index, inner in enumerate(input_list):
            if in_index != out_index:
                product *= inner

        output_list.append(product)
    return output_list

# Efficient approach
# O(n) time and O(n) space

def get_products_of_all_ints_except_at_index_efficient(input_list):

    if len(input_list) < 2:
        raise IndexError("The input list needs to contain at least 2 integers")

    output_list = [None] * len(input_list)

    # get the product of all integers before each index
    product_so_far = 1
    i = 0
    while i < len(input_list):
        output_list[i] = product_so_far
        product_so_far *= input_list[i]
        i += 1

    # reverse indices to get the product of all integers after each index
    product_so_far = 1

    i = len(input_list) - 1
    while i >= 0:
        output_list[i] *= product_so_far
        product_so_far *= input_list[i]
        i -= 1

    return output_list

# Testing
print(get_products_of_all_ints_except_at_index([1, 7, 3, 4]))
print(get_products_of_all_ints_except_at_index([1, 0, 3, 4]))
print(get_products_of_all_ints_except_at_index_efficient([1, 2, 6, 5, 9]))
print(get_products_of_all_ints_except_at_index_efficient([10]))
