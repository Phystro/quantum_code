#!/usr/bin/env python3
# O(N)
#

data = [2, 32, 10, 41, 8, 12, 67, 79, 14, 91, 19, 56, 88, 109]
target = 14
N = len(data)


def linear_search(data, x):
    # find length of data set
    N = len(data)
    for i in range(N):
        if x == data[i]:
            return i, i + 1     # return index and number of steps taken to find element target

    return -1, i + 1

x = 159
result, steps = linear_search(data, x)
print("Element index: %d, found in %d steps"%(result, steps))

