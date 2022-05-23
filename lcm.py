"""
find lcm
lcm(6,3)
cm(6)- 6,12,18,24
cm(3) - 3,6,9,12
lcm = 6
1. find greatest of 6,3
2. find if greater value divisible by both a, b
3. if true break the loop and return greater value,if not incr greater value


find hcf
hcf(6,3)
cf(6)- 1,3,6
cf(3) - 1, 3
hcf - 3

1. find minimum  of 6,3
2. find if a and b is divisible by the minimum value
3. if true  break the loop and return lesser value,if not decrement minimum value

lcm* hcf =a*b

"""


def least_common_multiple(a, b):
    greater = max(6, 3)
    while True:
        if (greater % a == 0) and (greater % b ==0):
            print(greater)
            return greater
        greater += 1


least_common_multiple(10, 12)


def highest_common_factor(a, b):
    lesser = min(6, 3)
    while True:
        if ( a % lesser == 0) and (b % lesser == 0):
            print(lesser)
            return lesser
        lesser -= 1


highest_common_factor(10, 12)

