# Write a function merge_ranges() that takes a list of meeting time ranges and
# returns a list of condensed ranges. a meeting is stored as tuples of integers
# (start_time, end_time). These integers represent the number of 30-minute
# blocks past 9:00 am.

# Brute force. Compare every meeting to every other meeting. O(n^2) time.

# Efficient approach.

def merge_ranges(input_list):

    # Sort first by start time
    # Soring in place O(n log n) time
    input_list.sort(key=lambda tup: tup[0])

    output_list = []

    # Merge
    # Go through the list once merging adjacent tuples

    tmp = [input_list[0][0], input_list[0][1]]

    for i, tup in enumerate(input_list[:-1]) :

        # if start of second tuple is between start and end of the first tuple
        if input_list[i + 1][0] >= tmp[0] and input_list[i + 1][0] <= tmp[1] :
            # then merge
            start = min(tmp[0], input_list[i + 1][0])
            # end time is bigger of the two
            end = max(input_list[i][1], input_list[i + 1][1])

            # keep tmp to merge other overlapping ranges
            tmp = [start, end]

        else:

            # no more merging, write out into the output list
            output_list.append( ( tmp[0], tmp[1] ))
            tmp = [input_list[i + 1][0], input_list[i + 1][1]]

    output_list.append( (tmp[0], tmp[1] ))
    return output_list


# Even cleaner approach. Time efficiency O(n log n) and space O(n)
def merge_ranges_clean(meetings):

    # Sort
    sorted_meetings = sorted(meetings)

    # initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:

        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # if the current and last meetings overlap, use the latest end time
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start, max(last_merged_meeting_end, current_meeting_end))


        # add the current meeting since it doesn't overlap
        else:
            merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings





# Test
print(merge_ranges([(1, 5), (2, 3)]))
print(merge_ranges_clean([(1, 5), (2, 3)]))
# Should return [(0, 1), (3, 8), (9, 12)]
print(merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))
print(merge_ranges_clean([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))
