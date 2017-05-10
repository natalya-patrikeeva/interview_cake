# Write a function to find the rectangular intersection of two
# given love rectangles.

# Love rectangles are defined as dictionaries:

# my_rectangle = {
#
#     # coordinates of bottom-left corner
#     'left_x': 1,
#     'bottom_y': 5,
#
#     # width and height
#     'width': 10,
#     'height': 4,
#
# }

# helper function to find overlap in x and y directions
def find_overlap(p1, length1, p2, length2) :

    # find the highest start point and lowest end point.
    # the highest ("rightmost" or "upmost") start point is
    # the start point of the overlap.
    # the lowest end point is the end point of the overlap.
    start = max(p1, p2)
    end = min(p1 + length1, p2 + length2)

    # no overlap
    if end <= start :
        return (None, None)

    overlap_length =  end - start

    return (start, overlap_length)

# O(1) time and O(1)O(1) space complexity
def intersection(rectangle_1, rectangle_2):

    my_rectangle = {}
    my_rectangle['left_x'], my_rectangle['width'] = find_overlap(rectangle_1['left_x'], rectangle_1['width'], rectangle_2['left_x'], rectangle_2['width'])
    my_rectangle['bottom_y'], my_rectangle['height'] = find_overlap(rectangle_1['bottom_y'], rectangle_1['height'], rectangle_2['bottom_y'], rectangle_2['height'])

    if not my_rectangle['width'] or not my_rectangle['height']:
        print "Two rectangles do not overlap. No love!"
        return None


    return my_rectangle

# Should return {'left_x':7, 'bottom_y':7, 'width':2, 'height':2}
print(intersection(rectangle_1={'left_x' : 1, 'bottom_y' : 5,
                                'width' : 10, 'height' : 4},
                   rectangle_2={'left_x' : 7, 'bottom_y' : 7,
                                'width' : 2, 'height' : 6} ))
# Should return {'left_x':1, 'bottom_y':5, 'width':10, 'height':4}
print(intersection(rectangle_1={'left_x' : 1, 'bottom_y' : 5,
                                'width' : 10, 'height' : 4},
                   rectangle_2={'left_x' : 1, 'bottom_y' : 5,
                                'width' : 10, 'height' : 4}) )
# Should return {'left_x':8, 'bottom_y':5, 'width':3, 'height':4}
print(intersection(rectangle_1={'left_x' : 1, 'bottom_y' : 5,
                                'width' : 10, 'height' : 4},
                   rectangle_2={'left_x' : 8, 'bottom_y' : 3,
                                'width' : 6, 'height' : 10}) )
# No overlap
# Should return None
print(intersection(rectangle_1={'left_x' : 1, 'bottom_y' : 5,
                                'width' : 10, 'height' : 4},
                   rectangle_2={'left_x' : 13, 'bottom_y' : 8,
                                'width' : 5, 'height' : 3}) )
