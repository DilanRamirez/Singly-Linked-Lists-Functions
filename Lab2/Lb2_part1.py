class Node(object):
    # Constructor
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class List(object):
    # Constructor
    def __init__(self):
        self.head = None
        self.tail = None

def Print(L):
    temp = L.head
    while temp is not None:
        print(temp.data, end=' ')
        temp = temp.next
    print("")

def isEmpty(L):
    return L.head == None


def Append(L,x):
    if isEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next

def Prepend(L,x):
    if isEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.head.next = Node(x)
        L.head = L.head.next

def insertAfter(L,w,x):
    if isEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    temp = L.head
    while temp is not None:
        if temp.data == w:
            temp.next = Node(x)
            temp = temp.next
        temp = temp.next
    return None


def Search(L,x):
    temp = L.head
    while temp is not None:
        if temp.data == x:
            return x
        temp = temp.next
    return None

# def Sort(L):
#     listLen = (getLenght(L))
#     for i in range(listLen-1):
#         t = L.head
#         if t.data > t.data.next:
#             t.next.data, t.data = t.data, t.next.data
#         t = t.next


# def buildList(plist):
#     L = List()
#     for i in plist:
#         Append(L,i)
#     return L
#
# def split(L):
#     L1 = List()
#     L2 = List()
#     temp = L.head
#     while temp is not None:
#         if temp.data < L.head.data:
#             Append(L1,temp.data)
#         else:
#             Append(L2, temp.data)
#         t = temp.next
#     return L1, L2

L = List()
plist = [1,2,3,4]
# for i in range(5):
#     Append(L,i)


Print(L)

