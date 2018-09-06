# Node of Singly Linked List of consisting of
#   - Data as string
#   - Next(Pointer, pointer is point to next node) as Node

class Node:
    
    def __init__(self, Data, Next):
        self.Data = Data
        self.Next = Next

# Singly Linked list consisting of
# - head as Node

class SinglyLinkedList:
    
    def __init__(self):
        self.head = None

    def add(self, Data):
        newNode = Node(Data, None)
        # linked list is empty
        if self.head == None:
            self.head = newNode
        else:
            newNode.Next = self.head
            self.head = newNode
            
    def search(self, value):
        
        currentPointer = self.head
        boolFound = False
        while currentPointer != None :
            
            if currentPointer.Data == value:
                boolFound = True
                return boolFound
                
            currentPointer = currentPointer.Next

        return boolFound

    def delete(self, value): # BUG : if value not in this Linked list will be error
        currentPointer = self.head
        prevPointer = None
        while currentPointer != None:
            if currentPointer.Data == value:
                break
                
            #prevPointer is pre value currentPointer so when next value is continue that prevPointer equal currentPointer
            prevPointer = currentPointer
            currentPointer = currentPointer.Next
            
        if prevPointer == None: # delete the first Node
            self.head = currentPointer.Next
            
        elif currentPointer.Next == None: # delte the last Node
            prevPointer.Next = None
            
        else:
            prevPointer.Next = currentPointer.Next

    def insert(self, index, value):
        # First
        # Mid
        # Last
        NewNode = Node(value, None)
        curIndex = 0
        currentPointer = self.head
        prevPointer = None
        check = False
        
        while currentPointer != None:
            curIndex += 1
            if index == 1 and check == False: # insert the first Node
                self.add(value)
                check = True
                
                
            if index == curIndex and check == False: # insert the mid Node
                prevPointer.Next = NewNode
                NewNode.Next = currentPointer
                check = True

            prevPointer = currentPointer
            currentPointer = currentPointer.Next
            
        if check == False: # insert the last Node
                prevPointer.Next = NewNode


        
    def show(self):
        currentPointer = self.head
        st = ""
        while currentPointer != None:
            #print(currentPointer.Data, ">>")

            st += currentPointer.Data + " --> "
            currentPointer = currentPointer.Next
        print(st + "None")

        
    def AddTxt(self, IDmember):
        filename = "MemberBorrowDetail.txt"
        currentPointer = self.head
        counter = 0
        with open(filename, 'w') as data:
            
            while currentPointer != None:
                Value = currentPointer.Data
                
                if len(Value) > 8:
                    data.write(Value + " ")
                    
                else:
                    if counter == 0:
                        data.write(Value + " ")
                        counter = 1
                    else:
                        data.write("\n")
                        data.write(Value + " ")
                currentPointer = currentPointer.Next
                
    def AddTxtWhoOverDeadLine(self, IDmember):
        filename = "WhoOverDeadLine.txt"
        currentPointer = self.head
        counter = 0
        with open(filename, 'w') as data:
            
            while currentPointer != None:
                Value = currentPointer.Data
                
                if len(Value) > 8:
                    data.write(Value + " ")
                    
                else:
                    if counter == 0:
                        data.write(Value + " ")
                        counter = 1
                    else:
                        data.write("\n")
                        data.write(Value + " ")
                currentPointer = currentPointer.Next

    def AddTxtMEM(self):
        filename = "MemberDetail.txt"
        currentPointer = self.head
        counter = 0
        with open(filename, 'a') as data:
            data.write("\n")
            while currentPointer != None:
                Value = currentPointer.Data
                data.write(Value + " ")

                currentPointer = currentPointer.Next
    def AddTxtBOOK(self):
        filename = "BooksDetail.txt"
        currentPointer = self.head
        counter = 0
        with open(filename, 'a') as data:
            data.write("\n")
            while currentPointer != None:
                Value = currentPointer.Data
                data.write(Value + " ")

                currentPointer = currentPointer.Next
            
                
##node = Node("A", None)
##print(node.Data)

##MyLinkedList = SinglyLinkedList()
##MyLinkedList.add("1")
##MyLinkedList.add("B")
##MyLinkedList.add("C")
##MyLinkedList.insert(4,"X")
###k = MyLinkedList.delete("O")
##MyLinkedList.show()

