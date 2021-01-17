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
        """
        Swaps the two given nodes's values
        """
        self.val, other.val = other.val, self.val
    
    def __eq__(self, object) -> bool:
        """
        Check for node equality returns true if node have the same value
        """
        try:
            if self and object:
                return self.val == object.val
        except:
            return False

        return False
        
    def __getitem__(self, side):
        """
        TreeNode['right'] or TreeNode[1]
        """
        if side == "right" or side == 1:
            return self.right
        elif side == "left" or side == -1:
            return self.left
        raise KeyError
    
    def __setitem__(self, side, data):
        """
        TreeNode['right'] = something or TreeNode[1] = Something
        """
        if side == "right" or side == 1:
            self.right = data
        elif side == "left" or side == -1:
            self.left = data
        raise KeyError

    def __hash__(self):
        return self.val
