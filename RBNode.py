from TreeNode import TreeNode
class RBNode(TreeNode):
    def __init__(self, data):
        super().__init__(data)
        self.color = True # True refers to as RED 

    def __str__(self):
        return f"<RBNode Data: {str(self.val)} Color: {'RED' if self.color else 'BLACK'}>"

    def recolor(self):
        self.color = not self.color