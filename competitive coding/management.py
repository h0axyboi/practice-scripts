class Company:
    def __init__(self,name,designation):
        self.name=name
        self.designation=designation
        self.children=[]
        self.parent=None

    def add_child(self,child):
        self.children.append(child)
        child.parent=self

    def to_print(self,cue):
        if cue=='name':
            return self.name
        elif cue=='designation':
            return self.designation
        elif cue=='both':
            return '{} ({})'.format(self.name,self.designation)

    def get_level(self):
        level=0
        while self.parent:
            level+=1
            self=self.parent
        return level

    def print_tree(self,cue):
        prefix=' '*self.get_level()*3+'|---' if self.parent else ''
        print(prefix+self.to_print(cue))
        if self.children:
            for child in self.children:
                child.print_tree(cue)


def build_management_tree():
    cloud_manager=Company('Dhaval','Cloud Manager')
    app_manager=Company('Abhijit','App Manager')

    infrastructure_head=Company('Vishwa','Infrastrcture Head')
    application_head=Company('Aamir','Application Head')
    recruitment_manager=Company('Peter','Recruitment Manager')
    policy_manager=Company('Waqas','Policy Manager')
    infrastructure_head.add_child(cloud_manager)
    infrastructure_head.add_child(app_manager)

    cto=Company('Chinmay','CTO')
    hr_head=Company('Gels','HR Head')
    cto.add_child(infrastructure_head)
    cto.add_child(application_head)
    hr_head.add_child(recruitment_manager)
    hr_head.add_child(policy_manager)

    ceo=Company('Nilupul','CEO')
    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo


if __name__=='__main__':
    root_node=build_management_tree()
    root_node.print_tree('name')
    root_node.print_tree('designation')
    root_node.print_tree('both')
