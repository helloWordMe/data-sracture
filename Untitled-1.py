my_list_address = [1,2,3,4,5,6,7,8,9]

print(id(my_list_address[0]))
print(id(my_list_address[1]))
print(id(my_list_address[2]))

from ctypes import addressof, c_int, create_string_buffer

hello = 'hello'
one = 1
# id return the exact address of vaariable

def get_str_address(my_string : str):
    c_string = create_string_buffer(my_string.encode('utf-8'))
    return c_string


print(f'address hello : {addressof(get_str_address(hello))}')
print(f'address hello : {id(hello)}')
print(f'address one : {addressof(c_int(one))}')


from abc import ABC , abstractmethod


class MyInterface(ABC):

    @abstractmethod
    def hello(self):
        pass


class MyClass(MyInterface):
    def __init__(self, name):
        self.name = name

    def hello(self):
        return f'hello {self.name}'


my_class = MyClass('Alireza')

hello = my_class.hello()      

print(hello)






