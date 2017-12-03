#!/usr/bin/env python

import sys

def solve1(number):

    number = int(number)
    # 1. Determine which radis the number have. area grows: 1-> 1. 2-3^2-> 2 10-5^2 -> 7^2-> 3 

    i=1
    layer = 1
    while(True):
        if(number <= i*i):
            break
        i += 2
        layer += 1

    # 2. For this particular radis we know the start-index
    section_len = i*i - (i-2)*(i-2)

    # 3. Determine the relative index for the number.

    first_number_on_layer = (i-2)*(i-2) + 1
    index_on_layer = number - first_number_on_layer

    # 4. Given the index, the position relative the index can be known by a relate distance to the closest number with minimal distance.
    number_with_min_distance = first_number_on_layer + (layer-2)

    numbers_with_min_distance = []
    for i in range(4):
        numbers_with_min_distance.append(number_with_min_distance + int((i*section_len/4)))

    delta = []
    for i in numbers_with_min_distance:
        delta.append(abs(i-number))

    manhattan_distance = layer-1 + min(delta)

    print("output 1:")
    print(manhattan_distance)


class square():

    x = None
    y = None
    val = 0
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.val = s

def get_neighbour_val(storage, x,y):

    sum = 0;

    for i in storage:
        if(abs(i.x - x) <= 1):
            if(abs(i.y - y) <= 1):
                sum +=i.val
    return sum


def solve2_wrap(number):

    s = solve2(number)
    print("Output 2:")
    print(s)

def solve2(number):

    print("output 2:")

    number = int(number)

    squares = []
    first_square = square(0,0,1)

    squares.append(first_square)

    # First level:
    x_max = 1
    x_min = -1
    y_max = 1
    y_min = -1
    y_start = 0

    result = 0

    while(True):

        for y in range(y_start, y_max+1):
            #print("(%d, %d)" % (x_max, y))
            s = get_neighbour_val(squares, x_max, y)
            squares.append(square(x_max,y, s))
            print("(%d, %d) = %d" % (x_max, y, s))
            if(s > number):
                return s

        # Fixed y:
        for x in range(x_max-1, x_min-1, -1):
            s = get_neighbour_val(squares, x, y_max)
            squares.append(square(x,y_max, s))
            print("(%d, %d) = %d" % (x, y_max, s))
            if(s > number):
                return s

        for y in range(y_max-1, y_min-1, -1):
            s = get_neighbour_val(squares, x_min, y)
            squares.append(square(x_min,y, s))
            print("(%d, %d) = %d" % (x_min, y, s))
            if(s > number):
                return s

         # Fixed y:
        for x in range(x_min+1, x_max+1):
            s = get_neighbour_val(squares, x, y_min)
            squares.append(square(x,y_min, s))
            print("(%d, %d) = %d" % (x, y_min, s))   
            if(s > number):
                return s

        y_start = y_min
        x_max +=1
        y_max +=1
        x_min -=1
        y_min -=1

 
    print(result)





if __name__ == "__main__":
    solve1(sys.argv[1])
    solve2_wrap(sys.argv[1])
