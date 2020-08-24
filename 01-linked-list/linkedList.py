#!/usr/bin/env python3
class Node:
  def __init__(self, value=None, next=None):
    self.value = value
    self.next = next

class LinkedList(object):
  def __init__(self):
    self._head = None
    self._tail = None
    self._len = 0

       
  def prepend(self, value):

    node = Node(value)
    node.next = self._head
    self._head = node
    self._len += 1

    if not self._tail:
       self._tail = node


  def add(self, value):
    node = Node(value)
    self._len += 1
    
    if not self._head:
       self._head = node
       self._tail = node
    else:
       self._tail.next = node
       self._tail = node
    

  def includes(self, value):

    node = self._head

    while node and node.value != value:
       node = node.next

    return False if not node else True


  def delete(self, value):

    self._len -= 1
    if self._len < 0:
       self._len = 0
    
    if not self._head:
       return False

    node = self._head

    if node.value == value:
      if self._head == self._tail:
         self._head = None
         self._tail = None
      else:
         self._head = self._head.next

      return True

    while node.next and node.next.value != value:
      node =  node.next

    if node.next:
      if node.next == self._tail:
         self._tail = node
        
      node.next = node.next.next
      return True

    return False


  def head(self):
    return self._head.value


  def tail(self):
    return self._tail.value

    
  def __iter__(self):

    self._start = self._head
    return self


  def __next__(self):
    '''
      Traverse
    '''
    node = self._start

    if not node:
      raise StopIteration
    
    self._start = node.next
    
    while node:
      return node.value

      
  def __getitem__(self, item):
    
    node = self._head

    for key in range(0, item + 1):
      if key == item:
        return node.value

      node = node.next

     


  def __reversed__(self):
    for item in list(self):
      return item
        
     
  def __len__(self):
    return self._len
       
          
  def __str__(self):

    head = None
    tail = None
    leng = 0 

    if self._head and self._tail:
      head = self._head.value
      tail = self._tail.value
      leng = self._len
      
    return f'''(head: {head}, tail: {tail}): lenght {leng}'''


  def __list__(self):
    return [item for item in self]

          
if __name__ == '__main__':

  linkedList = LinkedList()
  linkedList.prepend(10)
  linkedList.add(11)

  assert (linkedList.head() == 10), 'Should be 10'
  assert (linkedList.tail() == 11), 'Should be 11'

  assert (linkedList.includes(10)), 'Should be True'
  assert (not linkedList.includes(12)), 'Should be False'


  linkedList = LinkedList()
  
  assert (not linkedList.includes(10)), 'Should be False'
  assert (not linkedList.delete(11)), 'Should be False'


  linkedList = LinkedList()
  linkedList.prepend(10)
  linkedList.add(11)

  assert (len(linkedList) == 2), 'Lenght Should be 2'
  assert (list(linkedList) == [10, 11]), 'Should return [10, 11]'
  
 
