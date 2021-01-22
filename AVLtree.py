from BinarySearchTree import BST


class AVL(BST):
    """
    AVL trees are self balancing BSTs that balace themselves by performing
    some rotations on the nodes.

    All operations like searching, min, max, etc. are performed in O(logn) or O(self.h)
    time complexity.
    """
    def __init__(self,args=None, balancing_factor =1):

        self.k = balancing_factor
        self.rotations = 0
        super().__init__(args)

    @property
    def title(self):
        return f"Height : {self.height}     Rotations : {self.rotations}"

    def insert(self,data):
        new_node = super().insert(data)
        self.balance(new_node)

    def balance(self, curr):
        """
        Balancing the AVL tree is done by calculating the balancing factors for 
        each node from the bottom up starting from the given node. By doing this we 
        find a critical node(z).

        Balance factor of a node is absolute difference of height of node's 
        right subtree and left subtree

        A node is critical node(z) if its balance factor is greater than 'self.k'
        In such case we take two nodes we encountered before 'z' from the path up to 'z'
        the child of 'z' is 'y' and child of 'y' is 'x'
        
        The position of these three nodes give us four combinations.
        1)'y' is LEFT child of 'z' and 'x' is LEFT child of 'y'
            - RIGHT ROTATE 'z' 

        2)'y' is RIGHT child of 'z' and 'x' is RIGHT child of 'y'
            - LEFT ROTATE 'z'

        3)'y' is LEFT child of 'z' and 'x' is RIGHT child of 'y'
            - LEFT ROTATE 'y'
            - RIGHT ROTATE 'z'

        4)'y' is RIGHT child of 'z' and 'x' is LEFT child of 'y'
            - RIGHT ROTATE 'y'
            - LEFT ROTATE 'z'
        
        """

        if not curr or curr.val not in self:
            raise ValueError("No such node exists")
        

        node_list = self.path_to(curr)
        
        for i in range(len(node_list)-1, -1, -1):
            node = node_list[i]
            

            balance_factor = abs(self.getHeight(node.left) - self.getHeight(node.right))

            if balance_factor > self.k :
                self.rotations+=1
                z = node
                y = node_list[i+1] if (i+1 < len(node_list))  else z.left or z.right
                x = node_list[i+2] if (i+2 < len(node_list))  else y.left or y.right

                if z.left == y and y.left == x:
                    # self.right_rot(z)
                    z.right_rot()

                if z.left == y and y.right == x:
                    # self.left_rot(y)
                    # self.right_rot(z)
                    y.left_rot()
                    z.right_rot()
                    
                if z.right == y and y.left == x:
                    # self.right_rot(y)
                    # self.left_rot(z)
                    y.right_rot()
                    z.left_rot()

                if z.right == y and y.right == x:
                    # self.left_rot(z)
                    z.left_rot()
                self.height = AVL.getHeight(self.root)
                
    def delete(self, data):
        curr = self.get_parent(self.find(data))
        super().delete(data)
        self.balance(curr)

    def left_rot(self, z):
        """
            Rotate left the given node 
        """
        # Assign z's position to x 
        # Set z.right = x.left and x.left = z
        x = z.right
        z_parent = self.get_parent(z)
        if z_parent:
            if z_parent.left == z:
                z_parent.left = x
            else:
                z_parent.right = x
        else:
            self.root = x 
        z.right = x.left
        x.left = z

        self.height = AVL.getHeight(self.root)

    def right_rot(self, z):
        """
            Rotate right the given node 
        """
        # Assign z's position to x 
        # Set z.left = x.right and x.right = z
        x = z.left
        z_parent = self.get_parent(z)
        if z_parent:
            if z_parent.left == z:
                z_parent.left = x
            else:
                z_parent.right = x
        else:
            self.root = x 
        z.left = x.right
        x.right = z

        

    