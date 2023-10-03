class node:
    def __init__(self,z):
        self.data=z
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def create_add_back(self,x):  #O(n)
        if(self.head==None):
            self.head=node(x)
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=node(x)
    def add_front(self,x):  #O(1)
        temp=node(x)
        temp.next=self.head
        self.head=temp
    def add_at_middle(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            fastp=self.head
            slowp=self.head
            while fastp!=None and fastp.next!=None:
                fastp=fastp.next.next
                slowp=slowp.next
            t=self.head
            while t.next!=slowp:
                t=t.next
            temp=node(x)
            t.next=temp
            temp.next=slowp
    def add_at_specified(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            t=self.head
            count=1
            pos=int(input("Enter pos"))
            while(count<pos-1):
                t=t.next
                count+=1
            temp=node(x)
            temp.next=t.next
            t.next=temp
        
    def traversal(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,end=" -> ")
            temp=temp.next
        
obj=linkedlist()
print("How many elements are you willing to create:")
n=int(input())
for i in range(1,n+1):
    obj.create_add_back(int(input()))
print(obj.traversal())

print("\nHow many elements are you willing to add at front:")
n=int(input())
for i in range(1,n+1):
    obj.add_front(int(input()))
print(obj.traversal())
obj.add_at_middle(14)
print(obj.traversal())
obj.add_at_specified(5)
print(obj.traversal())
            