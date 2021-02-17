from BinarySearchTree import BST
from RBNode import RBNode
from AVLtree import AVL


class RB(BST):
    def __init__(self, args = None):
        self.rotations = 0
        self.coloring = 0
        self.dblack = None
        super().__init__(args, RBNode)

    @property
    def title(self):
        return f"Height : {self.height}     Rotations : {self.rotations} \n Recoloring : {self.coloring}     Black Height : {self.b_height}"

    @property
    def b_height(self):
        curr = self.root
        bh = -1
        while(curr):
            bh += not curr.color
            curr = curr.left

        return bh
            
    def insert(self, data):
        new_node = super().insert(data)
        self.balance(new_node)
    
    def balance(self, node):
        """
            1. If node is root color it black EXIT
            2. If node's parent is black EXIT
            3. If node's uncle is red recolor parent, uncle, grandparent and recheck for grandparent
            4. If node's uncle is NULL or black do appropriate rotations 
                according to position of grandparent-parent and parent-node and recolor parent and grandparent
        """

        if node is self.root:
            node.color = False
            return
            
        uncle = self.get_uncle(node)
        parent = self.get_parent(node)

        if not parent.color: #If Parent is black return
            return

        gparent = self.get_grandparent(node)

        if uncle and uncle.color: #If uncle is RED
            self.coloring+=1   
            uncle.recolor()
            parent.recolor()
            gparent.recolor()
            self.balance(gparent)
        
        else: 
            self.rotations+=1
            self.coloring+=1   
            if gparent.val > node.val and gparent.left.val > node.val:
                # LL
                self.right_rot(gparent)
                parent.recolor()

            elif gparent.val < node.val and gparent.right.val < node.val:
                # RR
                self.left_rot(gparent)
                parent.recolor()

            elif gparent.val > node.val and gparent.left.val < node.val:
                # LR
                self.left_rot(parent)
                self.right_rot(gparent)
                node.recolor()

            else:
                # RL
                self.right_rot(parent)
                self.left_rot(gparent)
                node.recolor()


            gparent.recolor()

            self.height = self.getHeight(self.root)

    def delete(self, data):
        # Find node and its successor node and make double black if any
        node = self.find(data)
        self.dblack = None
        if node.is_leaf():
            # node has black color
            # Mark it as NULL node and make it double black
            if not node.color: 
                node.color = 2
                self.remove_double_black(node)

            super().delete(data)


        # if node has two childs
        elif node.left and node.right:
            successor = self.get_successor(node)
            self.delete(successor.val)
            node.swap(successor)

            # if successor.is_leaf():
            #     self.dblack = successor
            # else:
            #     self.dblack = successor.get_child()

            

        # Node has single child
        else:
            child = node.right if node.right else node.left
            # Either of child or node is black
            # Make child black
            super().delete(data)

            if child.color or node.color:
                child.color = False

            # If node and child are both black
            # make child double black
            else:
                child.color = 2
                self.remove_double_black(child)

    def remove_double_black(self, dblack ):
        '''
            Case 1: Double Black(DB) is the root 
        '''
        if not dblack or dblack.color!= 2:
            return

        if dblack == self.root:
            self.root = False
            return
        
        sibling = self.get_sibling(dblack)
        parent = self.get_parent(dblack)

        # print(sibling)
        if not sibling.color: # sibling is black

            # both child of sibling are black
                # If parent is black make it double black else make it black
                # Make sibling red
                # Recheck for parent
            left_c = False if not sibling.left else sibling.left.color
            right_c = False if not sibling.right else sibling.right.color
            print(f"Left : {left_c} Right: {right_c}")
            if left_c or right_c: # if any one of the child is red
                print("At least one child is red")

                if parent.left == sibling:
                    if not left_c: # left right case
                        sibling.color = True
                        sibling.right.color = False
                        red_child = sibling.right
                        self.left_rot(sibling)
                        sibling = red_child
                        

                    sibling.color , parent.color = parent.color , sibling.color
                    sibling.left.color = False
                    self.right_rot(parent)
                    dblack.color = False

                else:
                    if not right_c:
                        sibling.color = True
                        sibling.left.color = False
                        red_child = sibling.left
                        self.right_rot(sibling)
                        sibling = red_child

                    sibling.color , parent.color = parent.color , sibling.color
                    self.left_rot(parent)
                    dblack.color = False
                    sibling.left.color = False
                    
            else: #both sibling's child are black
                print("Both Sibling are black")
                sibling.color = True
                dblack.color = False
                if parent.color:
                    parent.color = False
                else:
                    parent.color = 2
                    self.remove_double_black(parent)                    
                
        else: #sibling is red
            print("Sibling is RED")
            parent.color = True
            sibling.color = False


            # Rotate in the diretion of double black

            # self.right_rot(parent) if parent.right == dblack else self.left_rot(parent)
            if parent.right == dblack:
                self.right_rot(parent)
            else:
                self.left_rot(parent)
            self.remove_double_black(dblack)


    def get_uncle(self, node):
        path = self.path_to(node)
        if len(path) < 3:
            return None
        gparent = path[-3]
        parent = path[-2]
        
        if gparent.left == parent:
            return gparent.right
        else:
            return gparent.left

    def get_sibling(self, node):
        parent = self.get_parent(node)
        if parent:
            if node == parent.left:
                return parent.right
            
            else:
                return parent.left

    def __draw__(self, pos, edges):
        import networkx as nx   
        # Delete the placeholder
        pos['X'] =''
        del pos['X']

        T = nx.DiGraph()
        T.add_nodes_from(pos)

        node_colors = ["#FF000078" if n.color else "#00000078" for n in T.nodes]
        node_colors = []
        for n in T.nodes:
            if n.color == 2:
                node_colors.append("#00000078")
            elif n.color:
                node_colors.append("#FF000078")
            else:
                node_colors.append("#00000078")

        edges_colors = ["#FF0000" if n.color else "#000000" for n in T.nodes]

        nx.draw(T,pos, node_size=700,
                node_color=node_colors, edgecolors=edges_colors, 
                linewidths=1)

        nx.draw_networkx_edges(T, pos, edges, min_target_margin=13, min_source_margin=13)
        nx.draw_networkx_labels(T, pos, { p : p.val for p in pos})

