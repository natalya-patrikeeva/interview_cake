# Write a function that takes a list of cake type tuples (weight, value)
# and a weight capacity, and returns the maximum monetary value the duffel
# bag can hold.
def max_duffel_bag_value_with_capacity_1(cake_tuples) :

    max_value_at_capacity_1 = 0

    for cake_weight, cake_value in cake_tuples :
        if (cake_weight == 1) :
            max_value_at_capacity_1 = max(max_value_at_capacity_1, cake_value)

    return max_value_at_capacity_1

# O(n*k) time and O(k) space where n is the number of types of cake and
# k is the capacity of the bag
def max_duffel_bag_value(cake_tuples, capacity) :

    # make a list to hold max possible value at every capacity
    # indices are the capacities
    max_values_at_capacities = [0] * ( capacity + 1 )

    for current_capacity in xrange(capacity + 1) :

        # set to 0 for each capacity
        current_max_value = 0

        for cake_weight, cake_value in cake_tuples :

            # if the cake weighs as much or less than the current capacity
            # see what our max value could be if we took it
            if cake_weight <= current_capacity :
                # find max_value_using_cake
                # max_value_using_cake = max(cake_value, max_value_using_cake)
                max_value_using_cake = cake_value + \
                    max_values_at_capacities[current_capacity - cake_weight]

                current_max_value = max(max_value_using_cake, current_max_value)

            # fill up max_values_at_capacities list for this capacity
            max_values_at_capacities[current_capacity] = current_max_value

    return max_values_at_capacities[capacity]

# Test
# cake_tuples = [(3, 40), (5, 70)]
# capacity = 9

# cake type tuples (weight, value)
cake_tuples = [(7, 160), (3, 90), (2, 15)]

# weight capacity
capacity = 20

# Should return 555 (6 of the middle type of cake and 1 of the last type of cake)
print(max_duffel_bag_value(cake_tuples, capacity))
