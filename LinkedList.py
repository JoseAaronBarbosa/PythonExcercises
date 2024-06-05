import operator
ops = {'+': operator.add, '-': operator.sub, '*':operator.mul, '/':operator.truediv, '^':operator.pow}

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
 
            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")
 
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
 
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
 
        current_node.next = new_node

    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while(current_node != None and position != index):
                position = position+1
                current_node = current_node.next
 
            if current_node != None:
                current_node.data = val
            else:
                print("Index not present")
 
    def remove_first_node(self):
        if(self.head == None):
            return
 
        self.head = self.head.next
 
    def remove_last_node(self):
 
        if self.head is None:
            return
        current_node = self.head
        if current_node.next is None:
            val = current_node.data
            self.head = None
            return val
        while(current_node.next.next):
            current_node = current_node.next
        val = current_node.next.data
        current_node.next = None
        return val
 
    def remove_at_index(self, index):
        if self.head == None:
            return
 
        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
 
            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")
 
    def remove_node(self, data):
        current_node = self.head
 
        if current_node.data == data:
            self.remove_first_node()
            return
 
        while(current_node != None and current_node.next.data != data):
            current_node = current_node.next
 
        if current_node == None:
            return
        else:
            current_node.next = current_node.next.next
 
    def sizeOfLL(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size+1
                current_node = current_node.next
            return size
        else:
            return 0
        
    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next

    def returnAtIndex(self,index):
        if self.head == None:
            return None
        
        current_node = self.head
        position = 0
        while(current_node != None and position != index):
            current_node = current_node.next
            position += 1
        if current_node != None:
            return current_node.data
        else:
            print("Index not present")
            return None
LL = LinkedList()        

postfix_exp = '5379++'
try:
    for i in range(len(postfix_exp)):
        if postfix_exp[i].isnumeric():
            LL.insertAtEnd(postfix_exp[i])
        else:
            a = LL.remove_last_node()
            b = LL.remove_last_node()
            if postfix_exp[i] == '-' or postfix_exp[i] == '/' or postfix_exp[i] == '^':
                c = ops[postfix_exp[i]](int(b),int(a))
            else:
                c = ops[postfix_exp[i]](int(a),int(b))
            LL.insertAtEnd(str(c))
    if LL.sizeOfLL() > 1:
        print('Wrong balance of numbers and operands')
    else:     
        print(f'The result is {LL.remove_last_node()}')
except:
    print('Wrong balance of numbers and operands')



            
