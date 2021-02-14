class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def add_child(self,child):
        self.children.append(child)
        child.parent=self

    def print_tree(self):
        prefix=' '*self.get_level()*3 + '|--' if self.parent else ''
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
    def get_level(self):
        level=0
        while self.parent:
            level+=1
            self=self.parent
        return level

def build_product_tree():
    electronics=TreeNode('Electronics')

    laptops=TreeNode('Laptops')
    laptops.add_child(TreeNode('Macbook'))
    laptops.add_child(TreeNode('Microsoft Surface'))
    laptops.add_child(TreeNode('Thinkpad'))

    cellphones=TreeNode('Cellphones')
    cellphones.add_child(TreeNode('iPhone'))
    cellphones.add_child(TreeNode('Google Pixel'))
    cellphones.add_child(TreeNode('Vivo'))

    televisions=TreeNode('Televisions')
    televisions.add_child(TreeNode('Samsung'))
    televisions.add_child(TreeNode('LG'))

    electronics.add_child(laptops)
    electronics.add_child(cellphones)
    electronics.add_child(televisions)
    return electronics

if __name__=='__main__':
    tree_root=build_product_tree()
    tree_root.print_tree()
