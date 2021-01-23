from TreeNode import TreeNode
class RBNode(TreeNode):
    def __init__(self, data):
        super().__init__(data)
        self.color = True # True refers to as RED 

    def __str__(self):
        return f"<RBNode {str(self.val)} Color: {'RED' if self.color else 'BLACK'}>"

    def swap(self, other):
        super().swap(other)
        self.color, other.color = other.color, self.color