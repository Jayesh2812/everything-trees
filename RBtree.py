from TreeNode import TreeNode
from BinarySearchTree import BST
from AVLtree import AVL

class RBNode(TreeNode):
    def __init__(self, data):
        super().__init(data)
        self.color = "red"

    def __str__(self):
        return f"<RBNode {str(self.val)}>"


class RB(BST):
    def __init__(self, args = None):
        super().__init__(args)
        self.b_height = -1
    
    def insert(self, data):
        new_node = super().insert(data)
        self.balance(new_node)
    
    def balance(self, node):

        if node is self.root:
            node.color = "black"
            return
        uncle = self.get_uncle(node)
        if not uncle :
            return

        if uncle.color == "red":
            gparent = self.get_grandparent(node)
            if gparent.val > node.val and gparent.left.val > node.val:
                # LL
                pass                
            elif gparent.val < node.val and gparent.right.val < node.val:
                # RR
                pass
            elif gparent.val > node.val and gparent.left.val < node.val:
                # LR
                pass
            else:
                # RL
                
                pass


        else:
            pass

    def get_uncle(self, node):
        path = self.path_to(node)
        if len(path) < 3:
            return None
        gparent = path[-2]
        parent = path[-3]
        
        if gparent.left == parent:
            return gparent.right
        else:
            return gparent.left

    def left_rot(self, node):
        AVL.left_rot()





if __name__ == "__main__":
    rb = RB([1,2,3,4,5,6,7])