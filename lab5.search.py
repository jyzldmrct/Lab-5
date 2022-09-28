class Node:
  def __init__(self, dataval=None):
    self.dataval = dataval
    self.nextval = None


class SLinkedList:
  def __init__(self):
    self.headval = None

  def push_back(self, newElement):
    newNode = Node(newElement)
    if(self.headval == None):
      self.headval = newNode
      return
    else:
      temp = self.headval
      while(temp.nextval != None):
        temp = temp.nextval
      temp.nextval = newNode

  def SearchElement(self, searchValue):
    temp = self.headval
    found = 0
    i = 0 

    if(temp != None):
      while (temp != None):
        i += 1
        if(temp.dataval == searchValue):
          found += 1
          break
        temp = temp.nextval
      if(found == 1):
        print(searchValue,"is at index =", i)
      else:
        print(searchValue,"is not found.")
    else:
      print("The list is empty.")

  def PrintList(self):
    temp = self.headval
    if(temp != None):
      print("List:", end=" ")
      while (temp != None):
        print(temp.dataval, end=", ")
        temp = temp.nextval
      print()
    else:
      print("The list is empty.")

list = SLinkedList()

list.push_back("Nicole")
list.push_back("Jema")
list.push_back("Andree")
list.push_back("Hailee")
list.push_back("Elizabeth")
list.push_back("Billie")
list.push_back("Sadie")
list.push_back("Tokyo")

list.SearchElement("Nicole")
list.SearchElement("Col")
list.SearchElement("Nikol")

list.PrintList()
