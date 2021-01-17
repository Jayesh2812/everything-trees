from BinarySearchTree import BST


class AVL(BST):
    def __init__(self,args=None, balancing_factor =1):

        self.k = balancing_factor
        super().__init__(args)

    def insert(self,data):
        new_node = super().insert(data)
        self.balance(new_node)

    def balance(self, curr):
        print(curr) 
        if not curr or curr.val not in self:
            return
        node_list = self.path_to(curr)
        for i in range(len(node_list)-1, -1, -1):
            node = node_list[i]
            balance_factor = abs(self.getHeight(node.left) - self.getHeight(node.right))

            if balance_factor > self.k :
                print(node, [node.val for node in node_list])
                z = node
                y = node_list[i+1] if (i+1 < len(node_list))  else z.left or z.right
                x = node_list[i+2] if (i+2 < len(node_list))  else y.left or y.right

                if z.left == y and y.left == x:
                    self.right_rot(z)

                if z.left == y and y.right == x:
                    self.left_rot(y)
                    self.right_rot(z)
                    
                if z.right == y and y.left == x:
                    self.right_rot(y)
                    self.left_rot(z)

                if z.right == y and y.right == x:
                    self.left_rot(z)
                
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

    def balance_levels(self):
        Q = [self.root]
        while Q:
            # print(Q)
            curr = Q.pop(0)
            if curr is not None:
                curr.level = self.getHeight(curr)
                Q.append(curr.left)
                Q.append(curr.right)

        


if __name__ == "__main__":
    import random
    a=[4,2,1,3,7,6,8]
    a=[1,2,3,4]
    a=range(10)
    a=[random.randint(1, 20) for _ in range(10)]
    a=[21,26,30,9,4,14,28,18,15,10,2,3,7]
    avl = AVL()
    for i in a:
        avl.insert(i)
        avl.show_tree()

    