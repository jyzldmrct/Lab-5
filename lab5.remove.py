class Node:
    def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
    def __init__(self):
      self.headval = None

    def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval
         
    def AtBeginning(self,newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode

    def RemoveNode(self, Removekey): 
        HeadVal = self.headval 
          
        if (HeadVal is not None): 
            if (HeadVal.dataval == Removekey): 
                self.headval = HeadVal.nextval 
                HeadVal = None 
                return 
             
        while (HeadVal is not None): 
            if HeadVal.dataval == Removekey: 
                break 
            prev = HeadVal 
            HeadVal = HeadVal.nextval 
 
        if (HeadVal == None): 
            return 
 
        prev.nextval = HeadVal.nextval 
        HeadVal = None

list = SLinkedList()
list.headval = Node("Jema")
e2 = Node("Andree")
e3 = Node("Hailee")
e4 = Node("Elizabeth")
e5 = Node("Billie")
e6 = Node("Sadie")
e7 = Node("Tokyo")


list.headval.nextval = e2
e2.nextval = e3
e3.nextval = e4
e4.nextval = e5
e5.nextval = e6
e6.nextval = e7

list.AtBeginning("Nicole")
list.RemoveNode("Sadie")
list.listprint()
