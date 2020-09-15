class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev

class LinkedList:
    def __init__(self):
        self.head=None

    def push(self,data):
        node=Node(data,self.head,None)
        self.head=node

    def add_on(self,data):
        if self.head is None:
            self.head=Node(data,None,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None,itr)

    def insert_values(self,data_list):
        self.head=None
        for thing in data_list:
            self.add_on(thing)

    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count

    def remove_at(self,pos):
        if pos<0 or pos>=self.get_length():
            raise Exception('Invalid Index')
        if pos==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        last=itr
        while itr:
            if count==pos-1:
                itr.next=itr.next.next
                if itr.next:
                    itr.next.prev=itr
                break
            itr=itr.next
            count+=1

    def insert_at(self,pos,data):
        if pos<0 or pos>=self.get_length():
            raise Exception('Invalid index')
        if pos==0:
            self.push(data)
            return
        count=0
        itr=self.head
        while itr:
            if count==pos-1:
                node=Node(data,itr.next,itr)
                itr.next=node
                break
            count+=1
            itr=itr.next

    def insert_after_value(self,data,data_to_insert):
        itr=self.head
        while itr:
            if itr.data==data:
                node=Node(data_to_insert,itr.next,itr)
                itr.next=node
                return
            itr=itr.next
        raise Exception('Invalid data')

    def remove_by_value(self,data):
        itr=self.head
        if itr.data==data:
            self.remove_at(0)
            return
        while itr.next:
            if itr.next.data==data:
                itr.next=itr.next.next
                if itr.next:
                    itr.next.prev=itr
                return
            itr=itr.next

    def print_forward(self):
        if self.head is None:
            print('Linked list is empty')
            return
        itr=self.head
        output=''
        while itr:
            output+=str(itr.data)+('-->' if itr.next else '')
            itr=itr.next
        print(output)

    def print_reverse(self):
        output=''
        if self.head is None:
            print('Linked list is empty')
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        while itr:
            output+=str(itr.data)+('<--' if itr.prev else '')
            itr=itr.prev
        print(output)

if __name__=='__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_reverse()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print_forward()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print_forward()
    ll.remove_by_value("figs")
    ll.print_forward()
    ll.print_reverse()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print_forward()
