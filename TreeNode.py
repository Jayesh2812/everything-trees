class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data
        self.level = None

    def __str__(self):
        return f"<TreeNode {str(self.val)}>"

    def is_leaf(self):
        """
            Returns True if both the left and right pointer of given node are NULL
        """
        if self.left or self.right:
            return False
        return True
            
    def swap(self,other):
        self.val, other.val = other.val, self.val