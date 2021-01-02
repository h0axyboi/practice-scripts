class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_end(self,nextNode):
        if self.head is None:
            self.head=nextNode
        else:
            currentNode=self.head
            while True:
                if currentNode.next is None:
                    break
                currentNode=currentNode.next
            currentNode.next=nextNode

    def insert_head(self,new_head):
        temp_node=self.head
        self.head=new_head
        new_head.next=temp_node

    def len_list(self):
        if self.head:
            answer=1
        else:
            return 0
        curr_node=self.head
        while curr_node.next:
            answer+=1
            curr_node=curr_node.next
        return answer

    def insert_at(self,new_node,pos):
        if pos<0 or pos>=self.len_list():
            print('invalid insertion index')
            return
        if pos==0:
            self.insert_head(new_node)
            return
        curr_node=self.head
        curr_pos=0
        while True:
            if curr_pos==pos:
                prev_node.next=new_node
                new_node.next=curr_node
                break
            else:
                prev_node=curr_node
                curr_node=curr_node.next
                curr_pos+=1

    def delete_end(self):
        last_node=self.head
        while last_node.next:
            prev_node=last_node
            last_node=last_node.next
        prev_node.next=None

    def delete_head(self):
        if self.len_list()==0:
            print('List empty')
            return
        else:
            prev_head=self.head
            self.head=self.head.next
            prev_head.next=None

    def delete_at(self,pos):
        if pos==0:
            self.delete_head()
            return
        if pos>=self.len_list() or pos<0:
            print('Invalid deletion index')
            return
        curr_node=self.head
        curr_pos=0
        while True:
            if curr_pos==pos:
                prev_node.next=curr_node.next
                break
            else:
                prev_node=curr_node
                curr_node=curr_node.next
                curr_pos+=1

    def print_list(self):
        if self.head is None:
            print('The linked list is empty!')
            return
        currentNode=self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode=currentNode.next

if __name__=='__main__':
    first_node=Node(10)
    second_node=Node(20)
    third_node=Node(15)
    linkedList=LinkedList()
    linkedList.insert_end(first_node)
    linkedList.insert_end(second_node)
    linkedList.insert_at(third_node,1)
    linkedList.print_list()
    print(' ')
    linkedList.delete_at(2)
    linkedList.print_list()
