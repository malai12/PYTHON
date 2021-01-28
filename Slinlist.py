#create a singly linked list

class node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class sinlinlis:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    #insert in ll
    def insert(self,value,location):
        newnode = node(value)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            if location == 0:
                newnode.next = self.head
                self.head = newnode
            elif location == 1:
                newnode.next = None
                self.tail.next = newnode
                self.tail = newnode
            else:
                tempnode = self.head
                index = 0
                while index<location-1:
                    tempnode = tempnode.next
                    index+=1
                nextnode = tempnode.next
                tempnode.next = newnode
                newnode.next = nextnode    
    # traverse linklist
    def traverse(self):
        if self.head is None:
            print("SSL does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    def search(self,nodvalue):
        if self.head is None:
            return "SSL does not exist"
        else:
            node = self.head
            while node is not None:
                if nodvalue == node.value:
                    return node.value
                node = node.next
            return "node value does not exist"

    def delete(self,location):
        if self.head is None:
            print("SSL does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:   
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempnode = self.head
                index = 0
                while index<location-1:
                    tempnode = tempnode.next
                    index+=1
                nextnode = tempnode.next
                tempnode.next = nextnode.next
    
    def deleteentireList(self):
        if self.head is None:
            print("SSL does not exist")
        else:
            self.head = None
            self.tail = None





    

singly = sinlinlis()
# node1 = node(1)
# node2 = node(2)

# sinlinlis.head = node1
# sinlinlis.head.next = node2
# sinlinlis.tail = node2

singly.insert(1,1)
singly.insert(2,1)
singly.insert(3,1)
singly.insert(4,1)
singly.insert(0,0)
singly.insert(17,2)

print([node.value for node in singly])

# singly.delete(0)
singly.deleteentireList()
print([node.value for node in singly])
# singly.traverse()
print(singly.search(3))