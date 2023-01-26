from typing import Optional


class BinaryTree:

    def __init__(self, root_obj) -> None:
        self.key: str = str(root_obj)
        self.left_child: Optional[BinaryTree] = None
        self.right_child: Optional[BinaryTree] = None

    def insert_left(self, new_node) -> None:
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node) -> None:
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def add_right_child_tree(self, tree: 'BinaryTree') -> None:
        if self.right_child is None:
            self.right_child = tree
        else:
            t = tree
            t.right_child = self.right_child
            self.right_child = t

    def add_left_child_tree(self, tree: 'BinaryTree') -> None:
        if self.left_child is None:
            self.left_child = tree
        else:
            t = tree
            t.left_child = self.left_child
            self.left_child = t

    def remove_right_child_tree(self) -> None:
        self.right_child = None
        return

    def remove_left_child_tree(self) -> None:
        self.left_child = None
        return

    def get_right_child(self) -> "Optional[BinaryTree]":
        return self.right_child

    def get_left_child(self) -> "Optional[BinaryTree]":
        return self.left_child

    def set_root_val(self, obj) -> None:
        self.key = obj

    def get_root_val(self) -> str:
        return self.key

    def __repr__(self) -> str:
        return f"BinaryTree: {self.key}"

    def pre_order(self) -> None:
        print(self.key)
        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()

    def post_order(self) -> None:
        if self.left_child:
            self.left_child.post_order()
        if self.right_child:
            self.right_child.post_order()
        print(self.key)

    def in_order(self) -> None:
        if self.left_child:
            self.left_child.in_order()
        print(self.get_root_val())
        if self.right_child:
            self.right_child.in_order()


if __name__ == "__main__":
    tr = BinaryTree('a')
    tr.insert_left('b')
    tr.insert_right('c')
    tr.pre_order()
    print("-----------------")
    tree1 = BinaryTree('add_right')
    tree1.insert_left('tree1_left_child')
    tr.add_right_child_tree(tree1)
    tr.pre_order()
    print("-----------------")
    tr.remove_right_child_tree()
    tr.pre_order()
    print("-----------------")
    tree2 = BinaryTree('add_left')
    tree2.insert_right('tree2_right_child')
    tr.add_left_child_tree(tree2)
    tr.pre_order()
    print("-----------------")
    tr.remove_left_child_tree()
    tr.pre_order()
