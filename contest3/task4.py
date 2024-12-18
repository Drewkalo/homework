class Segment_tree:
    def __init__(self):
        self.t = None
        
    def most_common(lst):
        return max(set(lst), key=lst.count)
    
    def build(self,a):
        self.t = 4*len(a)*[0]
        self.len = len(a)
        self.a = a
        self.__build(a,0,0,len(a)-1)

    def __build(self,a,v,tl,tr):
        if tl == tr:
            self.t[v] = (a[tl], 1)
        else:
            tm = (tl+tr)//2
            self.__build(a,v*2+1,tl,tm)
            self.__build(a,v*2+2,tm+1,tr)
        if self.t[v*2+1][] and self.t[v*2+2][]

            self.t[v] = self.t[v*2+1] + self.t[v*2+2]

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
