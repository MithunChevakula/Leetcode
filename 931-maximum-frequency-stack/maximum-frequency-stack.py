class FreqStack:

    def __init__(self):
        self.freq={}
        self.group={}
        self.maxFreq=0

    def push(self, val: int) -> None:
        self.freq[val]=self.freq.get(val,0)+1
        temp=self.freq[val]
        self.maxFreq=max(temp,self.maxFreq)
        if temp not in self.group:
            self.group[temp]=[]
        self.group[temp].append(val)
        

    def pop(self) -> int:
        val=self.group[self.maxFreq].pop()
        self.freq[val]-=1
        if not self.group[self.maxFreq]:
            self.maxFreq-=1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()