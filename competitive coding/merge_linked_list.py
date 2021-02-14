class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_end(self,new_node):
        if self.head is None:
            self.head=new_node
        else:
            curr_node=self.head
            while True:
                if curr_node.next is None:
                    curr_node.next=new_node
                    break
                curr_node=curr_node.next

    def print_list(self):
        if self.head is None:
            print('List is empty!')
            return
        curr_node=self.head
        while True:
            print(curr_node.data)
            if curr_node.next is None:
                break
            else:
                curr_node=curr_node.next

    def delete_head(self):
        if self.head is None:
            print('List is empty!')
        temp=self.head
        self.head=self.head.next
        temp.next=None

def merge_list(a,b):
    new_list=LinkedList()
    while a.head and b.head:
        if a.head.data<=b.head.data:
            new_list.insert_end(Node(a.head.data))
            a.delete_head()
        else:
            new_list.insert_end(Node(b.head.data))
            b.delete_head()
    new_list.insert_end(a.head)
    new_list.insert_end(b.head)
    return new_list

if __name__=='__main__':

    list1=LinkedList()
    list1.insert_end(Node(5))
    list1.insert_end(Node(10))
    list1.insert_end(Node(15))

    list2=LinkedList()
    list2.insert_end(Node(2))
    list2.insert_end(Node(3))
    list2.insert_end(Node(20))

    list1.print_list()
    list2.print_list()
    list3=merge_list(list1,list2)
    list3.print_list()
