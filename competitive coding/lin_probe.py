class Hashtable:
    def __init__(self):
        self.max=10
        self.arr=[None for _ in range(self.max)]

    def get_hash(self,key):
        h=0
        for c in key:
            h+=ord(c)
        return h%self.max

    def __setitem__(self,key,val):
        h=self.get_hash(key)
        for i in range(self.max):
            if self.arr[h%self.max] is None or (len(self.arr[h%self.max])==2 and self.arr[h%self.max][0]==key):
                self.arr[h%self.max]=(key,val)
                return
            h+=1
        raise Exception('Hashtable is full')

    def __getitem__(self,key):
        h=self.gat_hash(key)
        if self.arr[h] is None:
            return
        for i in range(self.max):
            if self.arr[h%self.max][0]==key:
                return self.arr[h%self.max][1]
                break
            h+=1

    def __delitem__(self,key):
        h=self.get_hash(key)
        for i in range(self.max):
            if self.arr[h%self.max][0]==key:
                self.arr[h%self.max]=None
                break

t=Hashtable()
t['March 14']=120
t['March 10']=100
print(t.arr)
t['March 14']=140
print(t.arr)
t['March 23']=150
print(t.arr)
t['March 21']=100
print(t.arr)
t['March 32']=125
t['March 11']=10
t['March 22']=12
t['March 33']=120
t['March 34']=150
t['March 35']=180
t['March 36']=123
print(t.arr)
