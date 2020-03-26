#node class
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#linkedlist class
class LinkedList:
    def __init__(self):
        self.head=None
    #inserting nodes into linkedlist
    def insert(self,newnode):
        if self.head is None:
            self.head=newnode
        else:
            lastnode=self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode=lastnode.next
            lastnode.next=newnode
    #printing linkedlist elements
    def printllist(self):
        currentnode=self.head
        if currentnode is None:
            print("linkedlist is empty")
            return
        print("linkedlist elements")
        while True:
            if currentnode is None:
                break
            print(currentnode.data)
            currentnode=currentnode.next
    #finding length of linkedlist by iterative method
    def len_llist(self):
        len=0
        currentnode=self.head
        while True:
            if currentnode is None:
                break
            currentnode=currentnode.next
            len+=1
        return len

if __name__=='__main__':
    llist=LinkedList()
    firstnode=Node(1)
    secondtnode=Node(2)
    thirdnode=Node(3)
    fourthnode=Node(4)
    llist.insert(firstnode)
    llist.insert(secondtnode)
    llist.insert(thirdnode)
    llist.insert(fourthnode)
    llist.printllist()
    len=llist.len_llist()
    print("length of linkedlist is")
    print(len)







                

