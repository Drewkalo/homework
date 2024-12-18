class Segment_tree:
    def __init__(self):
        self.t = None

    def build_sum(self,a):
        self.t = 4*len(a)*[0]
        self.len = len(a)
        self.a = a
        self.__build(a,0,0,len(a)-1)

    def build_for_max(self,a):
        self.t = 4*len(a)*[0]
        self.len = len(a)
        self.a = a
        self.__build_for_max(a,0,0,len(a)-1)

    def build_for_min(self,a):
        self.t = 4*len(a)*[0]
        self.len = len(a)
        self.a = a
        self.__build_for_min(a,0,0,len(a)-1)

    def __build(self,a,v,tl,tr):
        if tl == tr:
            self.t[v] = a[tl]
        else:
            tm = (tl+tr)//2
            self.__build(a,v*2+1,tl,tm)
            self.__build(a,v*2+2,tm+1,tr)
            self.t[v] = self.t[v*2+1] + self.t[v*2+2]

    def __build_for_max(self,a,v,tl,tr):
        if tl == tr:
            self.t[v] = a[tl]
        else:
            tm = (tl+tr)//2
            self.__build_for_max(a,v*2+1,tl,tm)
            self.__build_for_max(a,v*2+2,tm+1,tr)
            self.t[v] = max(self.t[v*2+1], self.t[v*2+2])

    def __build_for_min(self,a,v,tl,tr):
        if tl == tr:
            self.t[v] = a[tl]
        else:
            tm = (tl+tr)//2
            self.__build_for_min(a,v*2+1,tl,tm)
            self.__build_for_min(a,v*2+2,tm+1,tr)
            self.t[v] = min(self.t[v*2+1], self.t[v*2+2])

    def sum(self,l,r):
        return self.__sum(0,0,self.len-1,l,r)
    
    def __sum(self,v,tl,tr,l,r):
        if l > r:
            return 0
        if(l == tl and r == tr):
            return self.t[v]
        tm = (tl+tr)//2
        return self.__sum(v*2+1,tl,tm,l,min(r,tm)) + self.__sum(v*2+2,tm+1,tr,max(l,tm+1),r)
    
    def maxis(self,l,r):
        return self.__maxis(0,0,self.len-1,l,r)
    
    def __maxis(self,v,tl,tr,l,r):
        if l > r:
            return 0
        if(l == tl and r == tr):
            return self.t[v]
        tm = (tl+tr)//2
        return max(self.__maxis(v*2+1,tl,tm,l,min(r,tm)), self.__maxis(v*2+2,tm+1,tr,max(l,tm+1),r))
    
    def minis(self,l,r):
        return self.__minis(0,0,self.len-1,l,r)
    
    def __minis(self,v,tl,tr,l,r):
        if l > r:
            return 0
        if(l == tl and r == tr):
            return self.t[v]
        tm = (tl+tr)//2
        return min(self.__minis(v*2+1,tl,tm,l,min(r,tm)), self.__minis(v*2+2,tm+1,tr,max(l,tm+1),r))
    
    def update(self,n,x):
        cur_l = 0
        cur_r = self.len - 1
        v = 0
        while cur_l != cur_r:
            cur_m = (cur_l + cur_r)//2
            if n <= cur_m:
                cur_r = cur_m
                v = v*2+1
            else:
                cur_l = cur_m+1
                v = v*2+2
        self.t[v] = x
        while v > 0:
            v = (v - 1) // 2
            self.t[v] = self.t[2*v+1]+self.t[2*v+2]

a = [1, 20, 3, 4, -99, 6, 7, 19, 9, -2, 11, 12]
tree_max = Segment_tree()
tree_min = Segment_tree()
tree_sum = Segment_tree()
tree_max.build_for_max(a)
tree_min.build_for_min(a)
tree_sum.build_sum(a)
print(tree_max.t)
print(tree_min.t)
print(tree_sum.t)
print(tree_sum.sum(0,11), f"current sum = {sum(a)}")
print(tree_min.minis(0, 11), f"current min = {min(a)}")
print(tree_max.maxis(0, 11), f"current max = {max(a)}")  
print(tree_min.minis(6, 9), f"current min a[6:9] = {min(a[6:10])}")
print(tree_max.maxis(6, 9), f"current max a[6:9] = {max(a[6:10])}")  


'''
class Fenwick_tree_sum:
    def __init__(self):
        self.t = None
    def update(self,i,a):
        while i < len(self.t):
            self.t[i] += a
            i = (i | (i+1))
    def build(self,a):
        self.t = [0]*len(a)
        for i in range(len(self.t)):
            self.update(i,a[i])
    def __maxis(self, r):
        res = -float("inf")
        while (r>=0):
            res = max(self.t[r], res)
            r = (r & (r+1)) - 1
        return res
    def __sum(self, r):
        res = 0
        while (r>=0):
            res += self.t[r]
            r = (r & (r+1)) - 1
        return res
    def __minis(self, r):
        res = +float("inf")
        while (r>=0):
            res = min(self.t[r], res)
            r = (r & (r+1)) - 1
        return res
    def maxis(self,l,r):
        return(max(self.__maxis(r), self.__maxis(l-1)))
    def minis(self,l,r):
        return(min(self.__minis(r), self.__minis(l-1)))
    def sum(self,l,r):
        return(self.__sum(r) - self.__sum(l-1))
    
tree = Fenwick_tree_sum()
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
tree.build(a)
print(tree.t)
print(tree.sum(0,4))
print(tree.minis(0,11))
print(tree.maxis(0,11))
print(tree.minis(6,9))
print(tree.maxis(6,9))
'''