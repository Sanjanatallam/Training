class node:
    def __init__(self,u):
        self.data=u
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.next
    def addback(self,x):
        t=self.head
        while(t.next!=None):
            t=t.next
        t.next=node(x)
    def addeven(self):
        t=self.head
        s=0
        while(t!=None):
            if(t.data%2==0):
                s=s+t.data
        return s
    def addbeg(self,x):
        t=node(x)
        t.next=self.head
        self.head=t
    def search(self,x):
        t=self.head
        while (t!=None):
            if t.data==x:
                return "found"
            t=t.next
        return"notfound"
    def findmiddle(self):
        t=self.head
        c=0
        while(t!=None):
            c=c+1
            t=t.next
        c=c//2
        t=self.head
        for i in range(c):
            t=t.next
        print(t.data)
        '''
        slow_ptr = self.head
        fast_ptr = self.head

        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        return slow_ptr.data
        '''
    def checklen(self):
        slow_ptr = self.head
        fast_ptr = self.head

        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        if (fast_ptr==None):
            print("even length")
        else:
            print("odd length")
    def substring(self):
        t=self.head
        c=0
        m=0
        while(t.next!=None):
            if (t.data)==((t.next.data)-1):
                c=c+1
            else:
                if(c>m):
                    m=c
                c=1
            t=t.next
        if(c>m):
            m=c
        print(m)
    def pairs(self):
        t=self.head
        t1=t.next
        while(t1.next!=None):
            while(t1!=None):
                print(t.data,t1.data)
                t1=t1.next
            t=t.next
            t1=t.next
    def bubble(self):
        t=self.head
        while(t.next!=None):
            t1=self.head
            while(t1.next!=None):
                if(t1.data>t1.next.data):
                    t1.data,t1.next.data=t1.next.data,t1.data
                t1=t1.next
        t=t.next
        t1=self.head
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.next
l1=sll()
l2=sll()
l1.head=node(10)
l1.addback(20)
l1.addback(30)
l1.addback(5)
l1.addback(90)
l1.addback(100)
l1.addbeg(9)
l1.display()
print()
print(l1.search(76))
print()
l1.findmiddle()
l1.checklen()
l1.substring()
l1.pairs()