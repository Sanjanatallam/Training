from collections import deque
class Node:
    def __init__(self, u):
        self.data = u
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.root = None
    def create(self, root, x):
        if root is None:
            self.root = Node(x)
        elif root.data > x:
            if root.left is None:
                root.left = Node(x)
            else:
                self.create(root.left, x)
        else:
            if root.right is None:
                root.right = Node(x)
            else:
                self.create(root.right, x)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end="->")
            self.inorder(root.right)
    def preorder(self,root):
        if root:
            print(root.data,end="->")
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end="->")
    def count(self,root):
        if root==None:
            return 0
        l=self.count(root.left)
        r=self.count(root.right)
        return 1+l+r
    def add(self,root):
        if root==None:
            return 0
        l=self.add(root.left)
        r=self.add(root.right)
        return root.data+l+r
    def evensum(self,root):
        if root==None:
            return 0
        if root.data%2==0:
            return root.data+self.evensum(root.left)+self.evensum(root.right)
        else:
            return self.evensum(root.left)+self.evensum(root.right)
    def oddsum(self,root):
        if root==None:
            return 0
        if root.data%2!=0:
            return root.data+self.oddsum(root.left)+self.oddsum(root.right)
        else:
            return self.oddsum(root.left)+self.oddsum(root.right)
    def diff_even_odd(self,root):
        if root==None:
            return 0
        if root.data%2==0:
            return root.data+self.diff_even_odd(root.left)+self.diff_even_odd(root.right)
        else:
            return self.diff_even_odd(root.left)+self.diff_even_odd(root.right)-root.data
    def height(self,root):
        if root==None:
            return -1
        l=self.height(root.left)
        r=self.height(root.right)
        return max(l,r)+1
    def fun(self,root):
        if root==None:
            return -1
        l=self.fun(root.left)
        r=self.fun(root.right)
        return max(l,r)+1
        def bal(root):
            return abs(fun(root.left)-fun(root.right))<=1
        if(bal(root)):
            print("balanced")
        else:
            print("not balanced")
    def count_leaf(self,root):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return 1
        l=self.count_leaf(root.left)
        r=self.count_leaf(root.right)
        return l+r
    def leafsum(self,root):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return root.data+self.leafsum(root.left)+self.leafsum(root.right)
        else:
            return self.leafsum(root.left)+self.leafsum(root.right)
    def search(self,root,x):
        if root==None:
            return "not found"
        if root.data==x:
            return  "found"
        elif root.data>x:
            return self.search(root.left,x)
        else:
            return self.search(root.right,x)
    def depth(self,root,y,c):
        if root==None:
            return -1
        if root.data==y:
            return c
        if root.data>y:
            return self.depth(root.left,y,c+1)
        else:
            return self.depth(root.right,y,c+1)
    def leftview(self,root,c,q):
        if root==None:
            return
        if c==len(q):
            q.append(root.data)
            print(root.data)
        self.leftview(root.left,c+1,q)
        self.leftview(root.right,c+1,q)
    def rightview(self,root,c,p):
        if root==None:
            return
        if c==len(p):
            p.append(root.data)
            print(root.data)
        self.rightview(root.right,c+1,p)
        self.rightview(root.left,c+1,p)
    def topview(self,root):
        q=deque()
        q.append((root,0))
        d={}
        while(q):
            node,num=q.popleft()
            d[num]=d.get(num,node.data)
            if node.left:
                q.append((node.left,num-1))
            if node.right:
                q.append((node.right,num+1))
        ans=[]
        for i in (list(d.keys())):
            ans.append(d[i])
        print(ans)
    def bottomview(self,root):
        q=[]
        q.append((root,0))
        d={}
        while(q):
            root=q[0][0]
            if root.left:
                q.append((root.left,q[0][1]-1))
            if root.right:
                q.append((root.right,q[0][1]+1))
            d[q[0][1]]=root.data
            q.pop(0)
        ans=[]
        for i in sorted(list(d.keys())):
            ans.append(d[i])
        print(ans)
t1 = Tree()
t1.create(t1.root, 10)
t1.create(t1.root, 5)
t1.create(t1.root, 20)
t1.create(t1.root, 7)
t1.create(t1.root, 1)
t1.inorder(t1.root)
print()
t1.preorder(t1.root)
print()
t1.postorder(t1.root)
print()
print(t1.count(t1.root))
print(t1.add(t1.root))
print(t1.add(t1.root.left))
print(t1.add(t1.root.right))
print(t1.add(t1.root.left)-t1.add(t1.root.right))
print(t1.evensum(t1.root))
print(t1.oddsum(t1.root))
print(t1.diff_even_odd(t1.root))
print(t1.height(t1.root))
# print(t1.balance(t1.root))
print(t1.count_leaf(t1.root))
print(t1.leafsum(t1.root))
print(t1.search(t1.root,7))
print(t1.depth(t1.root,20,0))
q=[]
t1.leftview(t1.root,0,q)
p=[]
t1.rightview(t1.root,0,p)
t1.topview(t1.root)
t1.bottomview(t1.root)
