import unittest
from random import *
def merge(left, right):  
    res = []
    left_cnt = right_cnt = 0


    for i in range(len(left) + len(right)):
        if left_cnt < len(left) and right_cnt < len(right):
            if left[left_cnt] <= right[right_cnt]:
                res.append(left[left_cnt])
                left_cnt += 1

            else:
                res.append(right[right_cnt])
                right_cnt += 1

        elif left_cnt == len(left):
            res.append(right[right_cnt])
            right_cnt += 1

        elif right_cnt == len(right):
            res.append(left[left_cnt])
            left_cnt += 1

    return res

def merge_sort(arry):  
    if len(arry) <= 1:
        return arry

    left = merge_sort(arry[:len(arry)//2])
    right = merge_sort(arry[len(arry)//2:])

    return merge(left, right)

s = [89,0,0,3,3,56,76,87,90]  
a = sorted(s)
print(merge_sort(s))
print(a)

class TestSorting(unittest.TestCase):
    def test_Sort(self):
        self.assertEqual(merge_sort([10,9,8,7,6,5,4,3,2,1]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "1")
        self.assertEqual(merge_sort([-10,6,-11,6, 55, 100]), [-11,-10,6,6,55,100] , "3")
        self.assertEqual(merge_sort([]), [], "1")
        self.assertEqual(merge_sort([1,2,3,2,3,4,2,5,6,7,5,8,99]), [1,2,2,2,3,3,4,5,5,6,7,8,99] , "3")


unittest.main()