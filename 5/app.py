#!/usr/bin/env python

import sys

def solve1(file_name):

    with open(file_name) as f:
        rows = f.readlines()
        input_list = [int(x.strip()) for x in rows]

        cur = 0
        stop = len(input_list)
        count = 0
        while(cur < stop):
            jump_len = input_list[cur]
            input_list[cur] += 1
            count += 1
            cur += jump_len
            
        print("output 1:")
        print(count)

def solve2(file_name):

    with open(file_name) as f:
        rows = f.readlines()
        input_list = [int(x.strip()) for x in rows]

        cur = 0
        stop = len(input_list)
        count = 0
        while(cur < stop):
            jump_len = input_list[cur]

            if(jump_len > 2):
                input_list[cur] -= 1
            else:
                input_list[cur] += 1

            count += 1
            cur += jump_len
            
        print("output 2:")
        print(count)
    


if __name__ == "__main__":
    solve1(sys.argv[1])
    solve2(sys.argv[1])
