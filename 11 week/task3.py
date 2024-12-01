
import unittest

def fast(arry: list):
    if len(arry) <= 1:
        return arry
    
    op = arry[len(arry)//2]
    lesseq = list(set([s for s in arry if s < op]))
    eq = list(set([s for s in arry if s == op]))
    more = list(set([s for s in arry if s > op]))

    return fast(lesseq) + eq + fast(more)

s = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(fast(s))


a = [2,2,2,2,2,2,2,2,2,2,2,2,2]
print(fast(a))



class TestSorting(unittest.TestCase):
    def test_Sort(self):
        self.assertEqual(fast([10,9,8,7,6,5,4,3,2,1]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "1")
        self.assertEqual(fast([-10,6,-11,6, 55, 100]), list(set([-10,6,-11,6, 55, 100])).sort() , "3")


unittest.main()