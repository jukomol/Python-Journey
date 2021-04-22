import array as arr
#integer array
def create_int_array():
    a=arr.array('i',[5,10,11,20])
    print("the int array is: ", end=" ")
    for i in range(0,4):
        print(a[i], end=" ")
    print()
#decimal array
def create_dec_array():
    a=arr.array('d',[5.0,10.1,11.2,20.3])
    print("the dec array is: ", end=" ")
    for i in range(0,4):
        print(a[i], end=" ")
    print()
#reverse array
def reverse_array():
    a=arr.array('i',[5,10,11,20])
    print("the reverse array is: ", end=" ")
    for i in range(0,4):
        print(a[len(a)-(i+1)], end=" ")#you can use reverse()/reversed()/flip()/flipud()/slicing
    print()
#adding elements to array
def insert_array(i,j):#i is index and j is value
    a=arr.array('d',[5.0,10.1,11.2,20.3])
    a.insert(i,j)#you can use append() method
    print("array after insertion: ", end=" ")
    for i in range(0,len(a)):
        print(a[i], end=" ")
    print()
#removing elements from array
def pop_array(i):
    create_dec_array()
    a=arr.array('d',[5.0,10.1,11.2,20.3])
    a.pop(i)#you can use remove() method or slicing technique
    print("array after removing items: ", end=" ")
    for i in range(0,len(a)):
        print(a[i], end=" ")
    print()
#data accessing in array
def access_array(i):
    a=arr.array('d',[5.0,10.1,11.2,20.3])
    print("You are looking for: ", a[i])
#updating value in array
def update_array(i,j):#i is index and j is value
    create_dec_array()
    a=arr.array('d',[5.0,10.1,11.2,20.3])
    a[i]=j
    print("array after updating: ", end=" ")
    for i in range(0,len(a)):
        print(a[i], end=" ")
    print()
#array concatenation
def concat_array():
    a=arr.array('d',[5.0,10.1,11.2,20.3])
    b=arr.array('d',[5,10,11,20])
    c=arr.array('d')
    c=a+b
    print("array after concatenation: ", end=" ")
    for i in range(0,len(c)):
        print(c[i], end=" ")
    print()

create_int_array()
create_dec_array()
reverse_array()
insert_array(1,22)
pop_array(2)
access_array(2)
update_array(3,43)
concat_array()
