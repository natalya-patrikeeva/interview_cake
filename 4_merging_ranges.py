# Write a function merge_ranges() that takes a list of meeting time ranges and
# returns a list of condensed ranges. a meeting is stored as tuples of integers
# (start_time, end_time). These integers represent the number of 30-minute
# blocks past 9:00 am.

def merge_ranges(input_list):

    output = []
    start = input_list[0][0]
    end = input_list[0][1]
    output.append( [start, end ])

    for index, tup in enumerate( input_list[1:] ):
        print tup
        if tup[0] > start and tup[0] < end :
            output[1][1] = tup[1]

        elif tup[1] >= start and tup[1] <= end :
            output[2][0] = tup[0]

        else:
            output.append([tup[0], tup[1]])
            print "out", output
            start = tup[0]
            end = tup[1]

    print "OUT: ", output




# Test
# Should return [(0, 1), (3, 8), (9, 12)]
merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
