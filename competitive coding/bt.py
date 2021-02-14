class BinarySearchTreeNode:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

    def add_child(self,data):
        if data==self.data:
            return
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements+=self.right.in_order_traversal()
        return elements

    def post_order_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.post_order_traversal()
        if self.right:
            elements+=self.right.post_order_traversal()
        elements.append(self.data)
        return elements

    def pre_order_traversal(self):
        elements=[]
        elements.append(self.data)
        if self.left:
            elements+=self.left.pre_order_traversal()
        if self.right:
            elements+=self.right.pre_order_traversal()
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
        return False

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def find_sum(self):
        sum=0
        if self.left:
            sum+=self.left.find_sum()
        sum+=self.data
        if self.right:
            sum+=self.right.find_sum()
        return sum

    def delete(self,val):
        if val<self.data:
            if self.left:
                self.left=self.left.delete(val)
        elif val>self.data:
            if self.right:
                self.right=self.right.delete(val)
        else:
            if self.right is None and self.left is None:
                return None
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
            max_val=self.left.find_max()
            self.data=max_val
            self.left=self.left.delete(max_val)
        return self



def build_tree(elements):
    root=BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

if __name__=='__main__':
    numbers=[40,30,32,35,80,90,100,120]
    numbers_tree=build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    numbers_tree.delete(100)
    print(numbers_tree.in_order_traversal())
