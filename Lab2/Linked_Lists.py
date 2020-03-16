class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class List(object):
    def __init__(self):
        self.head = None
        self.tail = None


def Append(L, x):
    if L.head is None:
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next


def Print(L):
    t = L.head
    while t is not None:
        print(t.data, end=' ')
        t = t.next
    print()

def copyList(L):
    newL = []
    temp = L.head
    while temp is not None:
        newL.append(temp.data)
        temp = temp.next
    return newL

def itemAt(L,pos):
    temp = L.head
    countpos = -1
    while temp is not None:
        countpos += 1
        if countpos == pos:
            return temp.data
        temp = temp.next
    return None

def count(L, x):
    temp = L.head
    count = 0
    while temp is not None:
        if temp.data == x:
            count += 1
        temp = temp.next
    return count

def index(L,x):
    ind = -1
    temp = L.head
    while temp is not None:
        ind += 1
        if temp.data == x:
            return ind
        temp = temp.next
    return None

def clear(L):
    while L.head is not None:
        L.head.head = None
        L.head = L.head.next
    return L

def createSublist(L,start,end):
    newL = []
    temp = L.head
    countstart = -1
    while temp is not None:
        countstart += 1
        if countstart >= start and countstart <= end:
            newL.append(temp.data)
        temp = temp.next
    return newL

def reverse(L):
    temp = L.head
    while temp is not None:
        temp = L.tail
        print(temp.data, end=' ')
        temp = temp.next

def insertAfter(L,x,w):
    temp = L.head
    while temp is not None:
        if temp.data == w:
            nextOne = temp.next
            node = Node(x)
            temp.next = node
            node.next = nextOne
        temp = temp.next
    return L

def remove(L, x):
    temp = L.head
    if temp is not None:
        if temp.data == x:
            L.head = temp.next
            temp = None
    while temp is not None:
        if temp.data == x:
            break
        prevOne = temp
        temp = temp.next
    if temp == None:
        return None
    prevOne.next = temp.next
    remove(L,x)
    return L

def GetLength(L):
    lenght = 0
    temp = L.head
    while temp is not None:
        lenght += 1
        temp = temp.next
    return lenght

def isEmpty(L):
    if L.head is None:
        return True
    return False

