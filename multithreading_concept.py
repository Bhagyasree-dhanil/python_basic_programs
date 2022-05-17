"""
Multithreading - multitasking

for a given list of numbers ,create 2 threads
list=[2,3,8,9]
1.square no
2.cube no

calculate the time required to run with thread and not with thread

"""

import time
import threading


def square_no(list_nos):
    print("calculating square of nos")
    square_list = []
    for i in list_nos:
        time.sleep(0.2)
        square_list.append(i * i)
        print("square", i, i*i)
    print(square_list)
    return square_list


def cube_no(list_nos):
    print("calculating cube of nos")
    cube_list = []
    for i in list_nos:
        time.sleep(0.2)
        cube_list.append(i * i * i)
        print("cube", i, i*i*i)
    print(cube_list)
    return cube_list


# without threading

t = time.time()
my_list = [2, 3, 8, 9]
square_no(my_list)
cube_no(my_list)
no_thread_time = time.time() - t
print("time with no thread", no_thread_time)

# with threading
tt = time.time()
t1 = threading.Thread(target=square_no, args=(my_list,))
t2 = threading.Thread(target=cube_no, args=(my_list,))

# to execute two task in parallel
t1.start()
t2.start()

# wait to do other task done and join to main thread
t1.join()
t2.join()

thread_time = time.time() - tt
print("time with thread", thread_time)

# Difference in time

print("The time difference is ", no_thread_time-thread_time)