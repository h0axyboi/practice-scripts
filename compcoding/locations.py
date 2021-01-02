class Locations:
    def __init__(self,data):
        self.data=data
        self.parent=None
        self.children=[]

    def add_child(self,child):
        self.children.append(child)
        child.parent=self

    def get_level(self):
        level=0
        while self.parent:
            level+=1
            self=self.parent
        return level

    def print_tree(self,num):
        prefix=' '*self.get_level()*3+'|__' if self.parent else ''
        if self.get_level()>num:
            return
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree(num)

def build_location_tree():
    ahmedabad=Locations('Ahmedabad')
    baroda=Locations('Baroda')
    bengaluru=Locations('Bengaluru')
    mysore=Locations('Mysore')
    princeton=Locations('Princeton')
    trenton=Locations('Trenton')
    sanfransisco=Locations('San Fransisco')
    mountainview=Locations('Mountain view')
    paloalto=Locations('Palo Alto')

    gujarat=Locations('Gujarat')
    karnataka=Locations('Karnataka')
    newjersey=Locations('New Jersey')
    california=Locations('California')
    gujarat.add_child(ahmedabad)
    gujarat.add_child(baroda)
    karnataka.add_child(bengaluru)
    karnataka.add_child(mysore)
    newjersey.add_child(princeton)
    newjersey.add_child(trenton)
    california.add_child(sanfransisco)
    california.add_child(mountainview)
    california.add_child(paloalto)

    india=Locations('India')
    usa=Locations('USA')
    india.add_child(gujarat)
    india.add_child(karnataka)
    usa.add_child(newjersey)
    usa.add_child(california)

    root=Locations('Global')
    root.add_child(india)
    root.add_child(usa)

    return root

if __name__=='__main__':
    root_node=build_location_tree()
    root_node.print_tree(0)
    root_node.print_tree(1)
    root_node.print_tree(2)
    root_node.print_tree(3)
