#!/usr/bin/env python

import sys

def solve1(file_name):

    with open(file_name) as f:
        rows = f.readlines()
        rows = [x.strip().split(" ") for x in rows]

        unique_count = []
        total_count = []
        for phrase in rows:

            # Duplicates are not allowed in set
            unique_count.append(len(set(phrase)))
            total_count.append(len(phrase))

        sum = 0
        for i in range(0,len(total_count)):
            if total_count[i] == unique_count[i]:
                sum += 1

        print("output 1:")
        print(sum)

def solve2(file_name):

    with open(file_name) as f:
        rows = f.readlines()
        rows = [x.strip().split(" ") for x in rows]

        unique_count = []
        total_count = []

        for phrase in rows:
            w_phrase = []
            for word in phrase:

                # Sort letters in words
                w_list = list(word)
                w_list.sort()

                # Convert to string again, list is not hashable and can not be inserted in set. 
                w_sorted = "".join(x for x in w_list)
                w_phrase.append(w_sorted)
                
            unique_count.append(len(set(w_phrase)))
            total_count.append(len(phrase))

        sum = 0
        for i in range(0,len(total_count)):
            if total_count[i] == unique_count[i]:
                sum += 1

    print("output 2:")
    print(sum)


if __name__ == "__main__":
    solve1(sys.argv[1])
    solve2(sys.argv[1])
