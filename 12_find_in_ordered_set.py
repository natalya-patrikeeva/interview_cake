# Suppose we had a list of n integers sorted in ascending order.
# How quickly could we check if a given integer is in the list?

# Use binary search to find the item in O(lg(n)) time and O(1) additional space.
def binary_search(target, nums):

    floor = -1
    ceiling = len(nums)

    while floor + 1 < ceiling :
        guess_index = ( floor + ceiling ) / 2

        if target == nums[guess_index]:
            return True

        # target is larger than the middle number so the target must be
        # in the right half
        # move floor to the right
        if target > nums[guess_index] :
            floor = guess_index

        # target is to the left
        else:
            ceiling = guess_index

    return False

# Test
nums = [1, 7, 10, 90]
print(binary_search(1, nums))
