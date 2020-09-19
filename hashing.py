class Hashtable:
    def __init__(self):
        self.max=100
        self.arr=[[] for _ in range(self.max)]

    def get_hash(self,key):
        h=0
        for c in key:
            h+=ord(c)
        return h%self.max

    def __setitem__(self,key,val):
        h=self.get_hash(key)
        for idx,element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx]=(key,val)
                return
        self.arr[h].append((key,val))

    def __getitem__(self,key):
        h=self.get_hash(key)
        for element in self.arr[h]:
            if element[0]==key:
                return element[1]

    def __delitem__(self,key):
        h=self.get_hash(key)
        for idx,element in enumerate(self.arr[h]):
            if element[0]==key:
                del self.arr[h][idx]

t=Hashtable()
t['march 66']=440
t['march 7']=123
print(t.arr)
t['march 66']=400
print(t.arr)
t['march 57']=321
print(t.arr)
print(t['march 57'])
