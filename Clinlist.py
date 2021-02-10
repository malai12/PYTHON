class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Cirsinlinlis:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def createCSLL(self,nodValue):
        node = Node(nodValue)
        node.next = node
        self.head = node
        self.tail = node
        return "The CSS has been created"
    
    def insertion(self,value,location):
        if self.head is None:
            return "The cirucular list is empty"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                temp = self.head
                index = 0
                while index > location -1:
                    temp = temp.next
                    index+=1
                nextnode = temp.next
                temp.next = newNode
                newNode.next = nextnode
            return "Node could be inserted"
    def traverse(self):
        if self.head is None:
            return "This list is empty"
        else:
            temp = self.head
            while temp:
                print(temp.value,end=" ")
                temp = temp.next
                if temp == self.tail.next:
                    break
    def search(self,value):
        if self.head is None:
            return "The list does not exist"
        else:
            temp = self.head
            while temp:
                if temp.value == value:
                    return temp.value
                temp = temp.next
                if temp == self.tail.next:
                    return "The value does not exists in the list"
    def deletion(self,location):
        if self.head is None:
            return "The list does not exist"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                temp = self.head
                index = 0
                while index<location-1:
                    temp = temp.next
                    index+=1
                nextnode = temp.next
                temp.next = nextnode.next
    def deleteentire(self):
        self.head = None
        self.tail.next = None
        self.tail = None



circularSLL = Cirsinlinlis()
circularSLL.createCSLL(1)
circularSLL.insertion(1,1)
circularSLL.insertion(2,0)
circularSLL.insertion(3,3)
circularSLL.insertion(4,4)
circularSLL.insertion(5,5)

# print(circularSLL.search(5))
# circularSLL.traverse()
print([node.value for node in circularSLL])
circularSLL.deletion(0)
print([node.value for node in circularSLL])
circularSLL.deleteentire()
print([node.value for node in circularSLL])


