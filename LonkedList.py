from abc import ABC , abstractmethod
from typing import TypeVar , Generic
import weakref 
import threading
from typing import Optional
import random

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
        self.lock = threading.Lock()
        self._nodes = weakref.WeakSet()
        #inmanagement languge becase we cant use address this make to not lost ower data

    

    def _xor(self, head, tail):
        return head ^ tail if head and tail else head or tail

    def _drefrence_pointer(self, id_node)->Optional[Node]:
        for node in self._nodes:
            if id(node) == id_node:
                return node
        return None        



    def insert_front(self, value : T):
        with self.lock : 
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
        with self.lock : 
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
        with self.lock: 
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
        with self.lock: 
            if self.tail is None:
                raise Exception ('this list is empty')
            
            if self.tail == self.head : 
                self.head = self.tail = None

            else:
                prev_node_id = self.tail.xor_pointer
                prev_node = self._drefrence_pointer(prev_node_id)
                prev_node.xor_pointer = self._xor(id(self.tail), prev_node.xor_pointer)
                self.tail = prev_node

            self.size -= 1    
        
    
def sort_linked_list(xor_linked_list : XORLinkedListClass):
    """
    we want to sort xor linked list by using just XORLinkedListClass methods... 
    """     

    if xor_linked_list is None :
        print("This xor linked class is empty !!")
        return

    for _ in range(xor_linked_list.size):
        current_value = xor_linked_list.tail.data
        xor_linked_list.remove_back()    

        if xor_linked_list.head is None or current_value <= xor_linked_list.head.data : 
            xor_linked_list.insert_front(current_value)
        
        else :
            prev = None
            next_node = xor_linked_list.head
            
            while next_node and next_node.data < current_value : 
                prev = next_node
                next_id = xor_linked_list._xor(id(prev), next_node.xor_pointer)
                next_node = xor_linked_list._drefrence_pointer(next_id)


            if next_node is None:  
                xor_linked_list.insert_back(current_value)
            else:  
                xor_linked_list.insert_front(current_value) 
    return xor_linked_list            


if __name__ == '__main__':
    xor_list = XORLinkedListClass[int]()
    for i in range(20):
        num = random.randint(0,100)
        if i/2==0 :
            xor_list.insert_front(num)
        else:
            xor_list.insert_back(num)
    xor_list.insert_front(1)

    print('لیست مرتب نشده')
    print(f'{xor_list}')
    sorted_list = sort_linked_list(xor_list)
    print('لیست مرتب شده')
    print(f'{sorted_list}')