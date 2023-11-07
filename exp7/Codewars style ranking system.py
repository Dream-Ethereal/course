dic={-8:0,-7:1,-6:2,-5:3,-4:4,-3:5,-2:6,-1:7,1:8,2:9,3:10,4:11,5:12,6:13,7:14,8:15}

class User:
    def __init__(self):
        self.rank=-8
        self.RANKS = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
        self.index=0
        self.progress=0
        
    def check(self):
        while self.progress>=100:
            self.progress-=100
            self.index+=1
            self.rank = self.RANKS[self.index]
            if self.rank>=8:
                self.rank=8
                self.progress=0
                return
        
            
    
    def inc_progress(self,testRank):
        rank_index = self.RANKS.index(testRank)
        if rank_index==self.index:
            self.progress+=3
            
        if rank_index==self.index-1:
            self.progress+=1
            
        if rank_index>self.index:
            sub = rank_index-self.index
            self.progress+=10*sub*sub
            
        self.check()
        if self.rank>=8:
            self.rank=8
            self.progress=0
        