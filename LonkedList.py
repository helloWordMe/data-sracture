from abc import ABC , abstractmethod
import weakref 
from typing import TypeVar , Generic

T = TypeVar('T')

#و نوشتن تابع سورت بیرون کلاس xor linked list پیاده سازی 
# we can xor to variable using ^ in python 
class XORLinkedListInterface(ABC, Generic[T]):

    @abstractmethod
    def insert_front(self, value : T):
        pass
    
    @abstractmethod
    def insert_back(self, value : T):
        pass
    
    @abstractmethod
    def remove_front(self):
        pass
    
    @abstractmethod
    def remove_back(self):
        pass


class Node:
    
    def __init__(self, data):
        self.data = data
        self.xor_pointer = 0  


class XORLinkedListClass(XORLinkedListInterface[T]):  
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
        self._nodes = weakref.WeakSet()
        #inmanagement languge becase we cant use address this make to not lost ower data

    

    def _xor(self, head, tail):
        return head ^ tail if head and tail else head or tail

    def _drefrence_pointer(self, id_node)-> Node:
        for node in self._nodes:
            if id(node) == id_node:
                return node
        return None        



    def insert_front(self, value : T):
        new_node = Node(value)

        if self.head is None:
            self.head = self.tail = new_node
        
        else:
            new_node.xor_pointer = id(self.head)
            self.head.xor_pointer = self._xor(id(new_node),self.head.xor_pointer)
            self.head = new_node
        self.size += 1
        self._nodes.add(new_node)

        
    
    def insert_back(self, value : T):
        
        new_node = Node(value)
        if self.tail is None : 
            self.tail = new_node

        else : 
            new_node.xor_pointer = id(self.tail)
            self.tail.xor_pointer = self._xor(id(new_node), self.tail.xor_pointer)
            self.tail = new_node

        self.size += 1
        self._nodes.add(new_node)    
    
    def remove_front(self):
        if self.head is None : 
            raise Exception('this list is empty  !')
        
        if self.head == self.tail : 
            self.head = self.tail = None
        
        else:
            next_node_id = self.head.xor_pointer
            next_node = self._drefrence_pointer(next_node_id)
            next_node.xor_pointer = self._xor(id(self.head), next_node.xor_pointer)
            self.head = next_node

        self.size -= 1    
    
    def remove_back(self):
        if self.tail is None:
            raise Exception ('this list is empty')
        
        if self.tail == self.head : 
            self.head = self.tail = None

        else:
            prev_node_id = self.tail.xor_pointer
            prev_node = self._drefrence_pointer(prev_node_id)
            prev_node.xor_pointer = self._xor_address(id(self.tail), prev_node.xor_pointer)
            self.tail = prev_node

        self.size -= 1    
        
    
def sort_linked_lit():
    pass     