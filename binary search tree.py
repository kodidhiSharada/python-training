class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Tree:
    def __init__(self):
        self.root=None
    def insertion(self,data):
         new_node=Node(data)
         if (self.root is None):
             self.root=new_node
         else:
             temp=self.root
         while True:
              if(data<temp.root):
                  if temp.left is None:
                      temp.left=new_node
                      break
                  else:
                      temp=temp.left
              else:
                  if temp.right is None:
                      temp.right=new_node
                      break
                  else:
                      temp=temp.right
    def inorder(self,root):
        if node:
            self.inorder(root.left)
        print(root.data,end=" " )
        self.inorder(root.right)
   x=Tree()
x.insertion(10)
x.insertion(20)
x.insertion(7)
x.insertion(12)
x.insertion(30)
x.insertion(13)
x.insertion(9)
x.insertion(6)
x.insertion(11)
x.insertion(41)
x.insertion(25)
x.insertion(5)
x.insertion(8)
x.inorder(x.root)
         
