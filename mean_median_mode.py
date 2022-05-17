import time
start_time = time.time()

# mean
"""
mean = total sum of elements in list / len(list)
 average value of all values in the list
"""


def mean(arr):
    return sum(arr)/len(arr)


# median
"""
 middle value among all the values in sorted order
 
 1. sort the list
 2. when len(list) = even then  ((n/2) term) + (n/2 + 1) term)/2
 3. when len(list) = odd then n/2 term
 
"""


def median(arr):
    arr.sort()
    len_arr = len(arr)

    if len_arr % 2 != 0:  # even
        med_val = arr[int(len_arr/2)]
    else:  # odd
        index1 = int(len_arr/2)
        index2 = index1 + 1
        med_val = (arr[index1] + arr[index2])/2
    return med_val


# mode

"""
mode is the Frequently occuring value in list 
"""


def mode(arr):
    return max(set(arr),key=arr.count)


arr1 = [2,3,3,5,6,8,7]
print("mean : ",  mean(arr1))
print("mode : ", mode(arr1))
print("median : ", median(arr1))

end_time = time.time()
total_time = end_time-start_time
print(total_time)