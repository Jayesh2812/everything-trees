import random

from TreeNode import TreeNode as Node
class BST:
    """
        Binary Search tree implementation 
    """
    def __init__(self,args=None):
        self.root = None
        self.height = -1
        if args:
            for i in args:
                self.insert(i)
        
    def __str__(self):
        return f"<BST with root value {self.root}>"

    def  insert(self, data):
        '''
            Insert into the BST, duplicate values are ignored
        '''
        new_node = Node(data)
        new_node.level = 0
        if self.root is None:
            self.root = new_node
        else:
            curr = self.root
            while True:
                new_node.level+=1
                if curr.val > new_node.val:
                    if curr.left is None:
                        curr.left = new_node
                        break
                    else:
                        curr = curr.left
                elif curr.val < new_node.val:
                    if curr.right is None:
                        curr.right = new_node
                        break
                    else:
                        curr = curr.right
                else:
                    break
        self.height = BST.getHeight(self.root)
        return new_node  

    def delete(self,data):
        """
            Delete the node specified  value if present
        """

        if data not in self:
            return
        # Locate the necessary node
        curr = self.find(data)


        # If node is leaf node
            # get the parent and set the parent's pointer to current node as None
        if curr.is_leaf():
            parent = self.get_parent(curr)
            if parent :
                if parent.left:
                    if parent.left.val == curr.val:
                        parent.left = None
                
                if parent.right:
                    if parent.right.val == curr.val:
                        parent.right = None
            else:
                self.root = None
        # Else if the node has both childs
            # find inorder successor of the node 
            # replace the the node to be deleted with inorder successor
            # delete the node to be deleted



        elif curr.left and curr.right :

            successor = self.get_successor(curr)
            successor_parent = self.get_parent(successor)

            # if successor_parent is the node to be deleted then
            if successor.is_leaf():
                if successor_parent.left == successor:
                    successor_parent.left = None
                else:
                    successor_parent.right = None
                curr.swap(successor)


            elif successor_parent == curr:
                successor.left = curr.left
                curr.left = None
                if curr == self.root:
                    self.root = successor
                else:
                    print(self.get_parent(curr))
                    self.get_parent(curr).right = successor
                

            
        # The node to be deleted has a single child
        else : 
            parent = self.get_parent(curr)
            child = curr.right if curr.right else curr.left
            if parent :
                if parent.left == curr:
                    parent.left = child
                else :
                    parent.right = child
            else :
                self.root = child
        del curr
        self.height = BST.getHeight(self.root)


    def get_successor(self, node):
        """ 
            Get the inorder successor of the given node
        """
        if node.val not in self:
            return None
        inorder = self.inorderTraversal()
        print(inorder)
        try :
            curr_index = inorder.index(node.val)
            curr = self.find(inorder[curr_index + 1])
            return curr
        except IndexError:
            return None
            
    def get_parent(self, node):
        """
            Returns the parent node if found else return None
        """
        if not node or node.val not in self:
            return
        path = self.path_to(node)
        if len(path) < 2:
            return None
        return path[-2]

    def get_grandparent(self, node):
        """
            Returns the grandparent node if found else return None
        """
        if node not in self:
            return
        path = self.path_to(node)
        if len(path) < 3:
            return None
        return path[-3]
      
    def __contains__(self, data):
        """
            Check if any node in the tree has the specified value
        """
        if not isinstance(data, int):
            if not isinstance(data, Node):
                return False
            data = data.val

        curr = self.root
        while curr:
            if curr.val < data:
                curr = curr.right
            elif curr.val > data:
                curr = curr.left
            elif curr.val == data:
                return True
        return False
            
    def find(self, data):
        """
            Returns node metadata of given data value
        """
        if data not in self:
            return None
        curr = self.root
        while curr:
            if curr.val < data:
                curr = curr.right
            elif curr.val > data:
                curr = curr.left
            elif curr.val == data:
                return curr
 
    def path_to(self,node):
        """
            Returns a list of nodes on path from root to the given node including the 
            root and the given node
        """
        path=[]
        if not node:
            return
        if node.val not in self:
            return path
        curr = self.root
        while curr:
            path.append(curr)
            if curr.val < node.val:
                curr = curr.right
            elif curr.val > node.val:
                curr = curr.left
            elif curr.val == node.val:
                break
        return path

    @staticmethod
    def getHeight(root):
        if root is None:
            return -1
        curr = root
        return 1 + max(BST.getHeight(curr.left), BST.getHeight(curr.right))
    
    def show_tree(self):
        import networkx as nx
        import matplotlib.pyplot as plt
        """
            Show tree representation on matplotlib
        """
        fig, ax = plt.subplots()

###############################################

        def onclick(event):
            # print(event.button)
            x = int(round(event.xdata))
            y = int(round(event.ydata))
                # print(f'x={x}, y={y}' )
            try:
                p = dict(zip(pos.values(),pos.keys()))[(x,y)]
                if event.dblclick:
                    self.delete(p)

                    colors = ["white" for i in range(len(pos))]
                    colors[list(pos.keys()).index(p)]= "#ff000080"

                    nx.draw(G,pos,node_size=700, node_color=colors,edgecolors="#000000", 
                    linewidths=1)
                    

                else:
                    print(p,self.get_successor(self.find(p)))
                    return
                fig.canvas.draw()
                self.show_tree()
            except KeyError:
                # data = int(input("Enter Data"))
                pass
                # self.insert(data)
            
        cid = fig.canvas.mpl_connect('button_press_event', onclick)

#################################################
        G = nx.DiGraph()

        tree=[]
        curr = self.root
        Q=[self.root]
        for i in range(self.height+1):
            for j in range(2**i):
                curr = Q.pop(0)
                if curr:
                    Q.append(curr.left)
                    Q.append(curr.right)
                    tree.append(curr.val)
                else:
                    Q.append(None)
                    Q.append(None)
                    tree.append("X")

        pos = []
        x =-2*(2**(self.height-1) )
        for level in range(self.height+1):
            y = int(x - x//(2**level))
            pos.append([(i,-2* level) for i in range(y,-y+1,2**(self.height - level + 1))])

        pos = [x for y in pos for x in y]
        pos = dict(zip(tree,pos))
        pos = {i : pos[i] for i in pos if i!="X"}

        edges = []
        for i in range(int(2**self.height) - 1):
            n = tree[i]
            i+=1
            l = tree[2 * (i) - 1]
            r = tree[2 * (i)]
            if n != 'X':
                if l !='X':
                    edges.append((n,l))
                if r !='X':
                    edges.append((n,r))


        tree = [x for x in tree if x !='X']
        G.add_nodes_from(tree)
        nx.draw_networkx_edges(G, pos, edges, min_target_margin=13)
        nx.draw(G,pos,node_size=700, node_color="#ffffff",edgecolors="#000000", 
            linewidths=1)
        nx.draw_networkx_labels(G, pos)
        
        plt.show()
        
    def levelOrderTraversal(self):
        '''
            Returns a array of tuples , each containing node's value and its depth
            in Level order Fashion


        '''
        """
            Insert root node into queue Q
            While Q is not empty
                Dequeue element perform actions and enqueue its left and right nodes
                if any of them exists(not None) else ignore
        """

        if self.root is None:
            return "Insert Values"
        Q = [self.root]
        LoT =[] #Level order Traversal
        while Q:
            curr = Q.pop(0)
            if curr is not None:
                LoT.append((curr.val, curr.level))
                if curr.left or curr.right:
                    Q.append(curr.left)
                    Q.append(curr.right)
        return LoT

    def inorderTraversal(self):
        """
            Returns a array of node values travesed in Inorder Fashion (Left -> Node -> Right )
        """

        """
            1) Create empty stack S
            2) Make a new variable curr and assign it  root of tree
            3) Push curr into stack and assign curr = curr->left untill curr is NULL
            4) While curr is NULL and stack is not empty pop the element from the stack 
                print the element and set curr = curr -> right 
            5) If stack is not empty and curr is not NULL Goto step 3
        """
        if self.root is None:
            return "Insert Values"
        curr = self.root 
        S = []
        IoT =[]
        while True:
            if not curr and not S:
                break
            while curr :
                S.append(curr)
                curr = curr.left
            while not curr and S:
                temp = S.pop()
                IoT.append(temp.val)
                curr = temp.right
        return IoT

    def postorderTraversal(self):
        """
            Returns a array of node values travesed in PostOrder Fashion (Left -> Right -> Node)
        """
        """
            1) Initialize two stacks S1 and S2
            2) Push root into S1
            3) While S1 is not empty
                3.1) Pop element from S1 and push it in S2
                3.2) Push the left and right child of popped element in S1 if they are not NULL
            4) Traverse S2 and print the values

        """

        if self.root is None:
            return "Insert Values"
        curr = self.root 
        S1=[curr]
        S2=[]
        while S1:
            temp = S1.pop()
            S2.append(temp.val)
            if temp.left:
                S1.append(temp.left)
            if temp.right:
                S1.append(temp.right)
        return S2[::-1]
            
    def preorderTraversal(self):

        """
            Returns a array of node values travesed in PreOrder Fashion ( Node -> Left -> Right )
        """   
        """
            1) Create empty stack S
            2) Make a new variable curr and assign it  root of tree
            3) Print curr and push curr into stack and assign curr = curr->left untill curr is NULL
            4) While curr is NULL and stack is not empty pop the element from the stack 
                and set curr = curr -> right 
            5) If stack is not empty and curr is not NULL Goto step 3
        """
        if self.root is None:
            return "Insert Values"
        curr = self.root 
        S=[]
        PoT =[]
        while True:
            if not curr and not S:
                break
            while curr:
                S.append(curr)
                PoT.append(curr.val)
                curr = curr.left
            while not curr and S:
                temp = S.pop()
                curr = temp.right
        return PoT

    def orderTraversal(node, method="in"):
        """ 
            Tree Traversal methods in one function
            post -> Prints PostOrder traversal of the tree
            pre -> Prints PreOrder traversal of the tree
            in -> Prints InOrder traversal of the tree
        """

        if node:
            if method == "pre":
                print(node.val,end=" ") # for Preorder
            if node.left:
                BST.orderTraversal(node.left, method)
            if method == "in":
                print(node.val,end=" ") # for inorder
            if node.right:
                BST.orderTraversal(node.right, method)
            if method == "post":
                print(node.val,end=" ") # for PostOrder

if __name__ == "__main__":

    a=[4,2,1,3,7,6,8]
    # a=[4,1,3,2]
    a=[random.randint(1, 20) for _ in range(10)]
    a=[2,1,6,4,7,8,5]
    myBST = BST(a)
    print("Level Order Traversal :",myBST.levelOrderTraversal())
    print("Height :", myBST.height)
    print("Inorder Traversal :",myBST.inorderTraversal())
    print("Preorder Traversal :",myBST.preorderTraversal())
    print("Postorder Traversal :",myBST.postorderTraversal())
    print(1 in myBST)
    print(myBST.find(5) in myBST)
    myBST.show_tree()