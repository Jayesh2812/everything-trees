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
    
    def __eq__(self, object) -> bool:
        if self and object:
            return self.val == object.val
        return False
        
    def __getitem__(self, side):
        if side == "right" or side == 1:
            return self.right
        elif side == "left" or side == -1:
            return self.left
        raise KeyError
    
    def __setitem__(self, side, data):
        if side == "right" or side == 1:
            self.right = data
        elif side == "left" or side == -1:
            self.left = data
        raise KeyError