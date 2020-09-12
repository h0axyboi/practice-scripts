class BinarySearchTreeNode():
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

    def add_child(self,val):
        if self.data==val:
            return
        elif self.data<val:
            if self.right:
                self.right.add_child(val)
            else:
                self.right=BinarySearchTreeNode(val)
        else:
            if self.left:
                self.left.add_child(val)
            else:
                self.left=BinarySearchTreeNode(val)

    def in_order_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements+=self.right.in_order_traversal()
        return elements

    def search(self,val):
        if self.data==val:
            return True
        elif val<self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False


def build_tree(arr):
    tree_root=BinarySearchTreeNode(arr[0])
    for i in range(1,len(arr)):
        tree_root.add_child(arr[i])
    return tree_root

if __name__=='__main__':
    numbers=[17,4,1,20,9,23,18,34]
    numbers_tree=build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(17))
