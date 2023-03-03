class BinaryTree():
    def __init__(self,root) -> None:
        self.start = root
        self.leftchild = None
        self.rightchild = None

    def ins_left(self,new_node):
        if self.leftchild == None:
            self.leftchild = BinaryTree(new_node)
        else:
            temp = BinaryTree(new_node)
            temp.leftchild = self.leftchild
            self.leftchild = temp

    def ins_right(self,new_node):
        if self.rightchild == None:
            self.rightchild = BinaryTree(new_node)
        else:
            temp = BinaryTree(new_node)
            temp.rightchild = self.rightchild
            self.rightchild = temp

    def perorder(self):
        print(self.start)
        if self.leftchild:
            self.leftchild.perorder()
        if self.rightchild:
            self.rightchild.perorder()

    def inorder(self):
        self.leftchild.inorder()
        print(self.get_root_val())
        self.rightchild.inorder()


    def postorder(self):
        self.leftchild.postorder()
        self.rightchild.postorder()
        print(self.get_root_val())

    def get_right_child(self):
        return self.rightchild

    def get_left_child(self):
        return self.leftchild

    def set_root_val(self,val):
        self.start = val

    def get_root_val(self):
        return self.start
    

a_t = BinaryTree('test')
a_t.ins_left('test_1')
a_t.ins_right('test_2')
r = BinaryTree('a')
print(r.get_root_val())
r.ins_left(a_t)
print(a_t.get_left_child().get_root_val())
print(a_t.get_right_child().get_root_val())