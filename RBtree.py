from TreeNode import TreeNode
from BinarySearchTree import BST
from AVLtree import AVL
import random
class RBNode(TreeNode):
    def __init__(self, data):
        super().__init__(data)
        self.color = True # True refers to as RED 

    def __str__(self):
        return f"<RBNode {str(self.val)} Color: {'RED' if self.color else 'BLACK'}>"


class RB(BST):
    def __init__(self, args = None):
        self.rotations = 0
        self.coloring = 0
        self.b_height = -1
        super().__init__(args, RBNode)

    @property
    def title(self):
        return f"Height : {self.height}     Rotations : {self.rotations} \n Recoloring : {self.coloring}     Black Height : {self.b_height}"

    
    def insert(self, data):
        new_node = super().insert(data)
        self.balance(new_node)
    
    def balance(self, node):

        if node is self.root:
            node.color = False
            return
            
        uncle = self.get_uncle(node)
        parent = self.get_parent(node)

        if not parent.color: #If Parent is black return
            return

        gparent = self.get_grandparent(node)

        if uncle and uncle.color: #If uncle is RED
            uncle.color = not uncle.color
            parent.color = not parent.color
            gparent.color = not gparent.color
            return self.balance(gparent)
        
        if gparent:    
            if gparent.val > node.val and gparent.left.val > node.val:
                # LL
                gparent.right_rot()
            elif gparent.val < node.val and gparent.right.val < node.val:
                # RR
                gparent.left_rot()
            elif gparent.val > node.val and gparent.left.val < node.val:
                # LR
                parent.left_rot()
                gparent.right_rot()
            else:
                # RL
                parent.right_rot()
                gparent.left_rot()

            parent.color = not parent.color
            gparent.color = not gparent.color

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
        # AVL.left_rot()
        pass

    def __draw__(self, pos, edges):
        import networkx as nx   
        # Delete the placeholder
        pos['X'] =''
        del pos['X']

        T = nx.DiGraph()
        T.add_nodes_from(pos)

        node_colors = ["#FF000078" if n.color else "#00000078" for n in T.nodes]
        edges_colors = ["#FF0000" if n.color else "#000000" for n in T.nodes]

        nx.draw(T,pos, node_size=700,
                node_color=node_colors, edgecolors=edges_colors, 
                linewidths=1)

        nx.draw_networkx_edges(T, pos, edges, min_target_margin=13, min_source_margin=13)
        nx.draw_networkx_labels(T, pos, { p : p.val for p in pos})

