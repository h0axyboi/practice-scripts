class PartyAnimal:
    x=0
    name=""
    def __init__(self,n):
        self.name=n
        print(self.name,'constructed')

    def party(self):
        self.x+=1
        print('So far,',self.x)

    def __del__(self):
        print(self.name,'destructed')

j=PartyAnimal('Jim')
j.party()
j.party()
s=PartyAnimal('Sally')
s.party()
