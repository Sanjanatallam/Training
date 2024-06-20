class Node:
    def __init__(self,u):
        self.data=u
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def addback(self,x):
        if(self.head==None):
            self.head=Node(x)
            self.tail=self.head
        else:
            self.tail.next=Node(x)
            self.tail.next.prev=self.tail
            self.tail=self.tail.next
    def addbeg(self,x):
        if(self.head==None):
            self.head=Node(x)
            self.tail=self.head
        else:
            self.head.prev=Node(x)
            self.head.prev.next=self.head
            self.head=self.head.prev
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.next
        t=self.tail
        print()
        while(t!=None):
            print(t.data,end="->")
            t=t.prev
        print()
    def search(self,x):
        t=self.head
        t1=self.tail
        while (t!=t1 and t!=t1.next):
            if t.data==x or t1.data==x:
                return 1
            t=t.next
            t1=t1.prev
        if(t.data==x):
            return "found"
        else:
            return "not found"
        print()
    def checklen(self):
        t=self.head
        t1=self.tail
        while(t!=t1 and t!=t1.next):
            t=t.next
            t1=t1.prev
        if(t==t1):
            return "odd"
        else:
            return "even"
    def palindrome(self):
        t=self.head
        t1=self.tail
        while(t!=t1):
            if(t.data!=t1.data):
                return False
            t=t.next
            t1=t1.prev
        return True
    def swaphalf(self):
        t=self.head
        t1=self.tail
        while(t.next!=t1):
            t=t.next
            t1=t1.prev
        self.tail.next=self.head
        self.head.prev=self.tail
        t.next=None
        t1.prev=None
        self.head=t1
        self.tail=t
        while(t1!=None):
             print(t1.data,end="->")
             t1=t1.next
        print()
    def swapsides(self):
        t=self.head
        t1=self.head.next
        t3=None
        while(t!=None):
            if(t==self.head):
                t.next=t1.next
                t1.next=t
                t1.prev=t3
                t.prev=t1
                self.head=t1
            else:
                
                t,t1=t1,t
                t3=t1
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.next
        print()
    def validparanthesis(self):
        s=[]
        tp=self.head
        c=0
        while tp:
            if tp.data in '([{':
                s.append(tp.data)
            elif tp.data==')' and s[-1]=='(' or tp.data==']' and s[-1]=='['  or tp.data=='}' and s[-1]=='{':
                s.pop()
            else:
                return c
            tp=tp.next
            c+=1
        if len(s)==0:
            return -1
    print()
    def evenoddsum(self,t,es,os):
        if(t==None):
            return abs(es-os)
        if (t.data%2==0):
            es=es+t.data
        else:
            os=os+t.data
        return self.evenoddsum(t.next,es,os)
    def primecount(self,t,count):
        if (t==None):
            return count
        def prime(s,n):
            if(s>(n//2)+1):
                return 1
            if(n%s==0):
                return 0
            return prime(s+1,n)
        if(prime(2,t.data)):
            count=count+1
        return self.primecount(t.next,count)
            
l1=dll()
l1.addback(1)
l1.addback(2)
l1.addback(3)
l1.addback(4)
l1.addback(5)
l1.addback(7)
l1.display()
print(l1.search(200))
print(l1.checklen()) 
print(l1.palindrome())
l1.swaphalf()
#print(l1.evenoddsum())
#print(l1.validparanthesis())
print(l1.evenoddsum(l1.head,0,0))
print(l1.primecount(l1.head,0))