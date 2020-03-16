"""
CS 2302 - Data Structures
Instructor: Dr. Olac Fuentes
TA: Ismael Villanueva-Miranda
Laboratory 2 - singly-linked lists
Author: Dilan Ramirez
Description:
1. Implement all the functions described in Table 4.1.1. in the textbook.
2. Implement the following functions:
    (a) Copy(list) Builds and returns a copy of list.
    (b) ItemAt(list,i) Returns the data item at position i in list.
    (c) Pop(list,i=0) Remove item at position i in list. If i is not specified, it removes the first item in list.
    (d) Count(list,x) Returns the number of times x appears in list.
    (e) Index(list,x) Returns the index of the first item whose value is equal to x list.
    (f) Clear(list) Removes all items from list.
    (g) Sublist(list,start=0,end=GetLength(list)) Builds and returns a sublist of list, from element start to
    element end (not inclusive).
    (h) Reverse(list) Reverses the elements in list (in place)
Last Modification: Jun 17, 2019
Lab Report Link: https://drive.google.com/open?id=17jI8BDV5ergss1CHbZKM0JT2uipgACHF
"""

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class List(object):
    def __init__(self):
        self.head = None
        self.tail = None

# Table 4.1.1
def Append(L, x):
    if L.head is None: #It creates a Node if L is None
        L.head = Node(x)
        L.tail = L.head
    else: # If L is not None, it add a new Node after the first one starting by the tail
        L.tail.next = Node(x)
        L.tail = L.tail.next

def Prepend(L,x):
    if L.head is None: #It creates a Node if L is None
        L.head = Node(x)
        L.head = L.tail
    else: # If L is not None, it add a new Node after the first one starting by the head
        node = Node(x)
        node.next = L.head
        L.head = node
    print("Prepends item: ", end=' ')
    Print(L)

def insertAfter(L,w,x):
    if L.head is None: #It creates a Node if L is None
        L.head = Node(x)
        L.tail = L.head
    temp = L.head
    if x == 0: #if the position is 0, the Node is Prepended
        Prepend(L,x)
    node = Node(x)
    while temp is not None: #if not, the value is searched until it is found, so a new node is added after it.
        if temp.data == w:
            node.next = temp.next
            temp.next = node
        temp = temp.next
    Print(L)

def Remove(L,x):
    if L.head == None: #It creates a Node if L is None
        return None
    if L.head.data == x: #if the first element is x, so it is deleted
        if L.head == L.tail: 
            L.head = None
            L.tail = None
        else:
            L.head = L.head.next
    else:   #if not, the elements is searched hutil it is found, and then deleted
        
         temp = L.head
         while temp.next != None and temp.next.data != x:
             temp = temp.next
         if temp.next != None:
             if temp.next == L.tail:
                 L.tail = temp
                 L.tail.next = None
             else:
                 temp.next = temp.next.next
    Print(L)

def Search(L,x):
    if L.head is None: #It creates a Node if L is None
        return False
    temp = L.head
    while temp is not None:  #the element is searched until it is found
        if temp.data == x:
            return True #if it is found, a True statement is returned
        temp = temp.next
    return False #if it is not found, a False statement is returned

def Print(L):
    t = L.head
    while t is not None:
        print(t.data, end=' ')
        t = t.next
    print()

def IsEmpty(L):
    return L.head == None

def PrintReverse(L):
    if L.head is None:  #It creates a Node if L is None
        return None
    prev = None #A new pointer is created to then connect them
    temp = L.head
    while temp is not None: #all the nodes are connected in reverse order
        next = temp.next
        temp.next = prev
        prev = temp
        temp = next
    L.head = prev
    Print(L)

def Sort(L):
    state = True
    while state:
        state = False
        temp = L.head
        while temp.next is not None:
            if temp.data > temp.next.data: #the elementes are switched until the condition is not true
                currentnode = temp.data
                temp.data = temp.next.data
                temp.next.data = currentnode
                state = True
            temp = temp.next
    Print(L)


def GetLength(L):
    temp = L.head
    count = 0
    while temp is not None: #the counter is increased by one until next is None
        count +=1
        temp = temp.next
    return count

#Lab 2 Exercises
# Exercise A
def Copy(L):
    L2 = List()
    temp = L.head
    print("Copy: ",end='')
    while temp is not None: #the elements are Appended in a new list while temp is not None
        Append(L2, temp.data)
        print(temp.data, end=' ')
        temp = temp.next
    print()

#Exercise B
def ItemAt(L,i):
    temp = L.head
    if temp == None:
        return None
    if i == 0:  #if i is 0, the first element is returned
        return temp.data
    count = 0
    while temp is not None: #if the element is not the first, the counter is increasing by one.
        count += 1
        if i == count:  #if the counter is equal to i, the element is returned
            return temp.data
        temp = temp.next
    return False

#Exercise C
def Pop(L,i):
    if L.head == None:
        return
    if L.head.data == i:
        if L.head == L.tail:
            L.head = None
            L.tail = None
        else:
            L.head = L.head.next
    else:
         temp = L.head
         while temp.next is not None and temp.next.data != i:
             temp = temp.next
         if temp.next is not None:
             if temp.next == L.tail:
                 L.tail = temp
                 L.tail.next = None
             else:
                 temp.next = temp.next.next

#Exercise D
def Count(L, x):
    if L.head is None:
        return None
    times = 0
    temp = L.head
    while temp is not None:
        if temp.data == x: #if the element of thelist is equal to x, the counter is increased.
            times += 1
        temp = temp.next
    return times

#Exercise E
def Index(L, x):
    if L.head is None:
        return None
    temp = L.head
    count = 0
    while temp is not None:
        count += 1  #the counter is increased by one until x is found.
        if temp.data == x:
            return count
        temp = temp.next
    return count

#Exercise F
def Clear(L):
    temp = L.head
    while temp is not None:
        Pop(L,temp.data) #It deletes the elements of the list by one
        temp = temp.next

# Exercise G
def Sublist(L, start, end):
    if L.head is None:
        return None
    t = L.head
    count = 0
    stop = GetLength(L)
    while t is not None:
        if start == 1 and end == stop:
            Append(M,t.data)
        t = t.next
    return M

#Exercise H
def Reverse(L):
    if L.head is None:  #It creates a Node if L is None
        return None
    prev = None #A new pointer is created to then connect them
    temp = L.head
    while temp is not None: #all the nodes are oonected in reverse order
        next = temp.next
        temp.next = prev
        prev = temp
        temp = next
    L.head = prev



M = List()
L = List()
for i in range(5):
    Append(L,i*5)
Append(L,20)
print("Original List: ", end=' ')
Print(L)
print()
print("________Functions from Table 4.1.1________")
Prepend(L,100)
print("Inserts 90 after 10: ", end=' ')
insertAfter(L,10,90)
print("Removes 15: ", end=' ')
Remove(L,15)
print("Searchs for number 5: ", end=' ')
print(Search(L,5))
print("Searchs for number 200: ", end=' ')
print(Search(L,200))
print("Is the List Empty: ", IsEmpty(L))
print("Previous List: ", end=' ')
Print(L)
print("Reversed List: ", end=' ')
PrintReverse(L)
print("Sorted List: ", end=' ')
Sort(L)
print("Lenght of L: ",GetLength(L))
print("_______ Exercises from Lab 2________")
print("Elements copied to another List", end=' ')
Copy(L)
print("Item 5: ", ItemAt(L, 2))
print("Pop item 5: ",end=' ')
Pop(L,5)
Print(L)
print("Number of times 100 appears in L: ", Count(L, 100))
print("List: ", end=' ')
Print(L)
print("Index of the first item whose value is equal to 20:", Index(L, 20))
print("Reverse the List: ", end=' ')
Reverse(L)
Print(L)
print("Clear the List:")
Clear(L)
