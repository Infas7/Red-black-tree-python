class Node:
    def __init__(self, value, color, parent, left=None, right=None):
        self.value  = value
        self.color  = color
        self.parent = parent
        self.left   = left
        self.right  = right

    def __bool__(self):
        return bool(self.value)


class RBTree:  
    def __init__(self):
        self.T_NILL = Node(value=False, color='BLACK', parent=None)
        self.root = self.T_NILL


    # ----------------------------------------------------------------------------------------------------------------
    def print_rb_tree(self, node, indent, last):
        if node != self.T_NILL:
            if node.parent != self.T_NILL:
                print(indent, end ="")
                if last:
                    if(node.parent.left == self.T_NILL):
                        print("└──", end ="")
                    else:
                        print("├──", end ="")
                    indent += "│  " 
                else:
                    print("└──", end ="")
                    indent += "   "

            print(f"{node.color[0]}{node.value}")
            
            self.print_rb_tree(node.right, indent, True)
            self.print_rb_tree(node.left, indent, False)

    def show(self):
        self.print_rb_tree(self.root, "", True)

    def rotate_right(self, node):
        other_node = node.left
        node.left = other_node.right
        if other_node.right:
            other_node.right.parent = node
        other_node.parent = node.parent
        if not node.parent:
            self.root = other_node
        elif node == node.parent.right:
            node.parent.right = other_node
        else:
            node.parent.left = other_node
        other_node.right = node
        node.parent = other_node
    
    def rotate_left(self, node):
        other_node = node.right
        node.right = other_node.left
        if other_node.left:
            other_node.left.parent = node
        other_node.parent = node.parent
        if not node.parent:
            self.root = other_node
        elif node == node.parent.left:
            node.parent.left = other_node
        else:
            node.parent.right = other_node
        other_node.left = node
        node.parent = other_node

    def replace(self, node, other_node):
        if not node.parent:
            self.root = other_node
        elif node == node.parent.left:
            node.parent.left = other_node
        else:
            node.parent.right = other_node
        other_node.parent = node.parent
    
    def get_min_node(self, node):
        while node.left:
            node = node.left
        return node



    # ----------------------------------------------------------------------------------------------------------------
    def insert(self, value):
        if not self.root:
            self.root = Node(value, color='BLACK', parent=self.T_NILL, left=self.T_NILL, right=self.T_NILL)
        else:
            self._insert_opr(value, self.root)

    def _insert_opr(self, value, parent_node):
        if value < parent_node.value:
            if not parent_node.left:
                parent_node.left = Node(value, color='RED', parent=parent_node, left=self.T_NILL, right=self.T_NILL)
                self._insert_fix(parent_node.left)
            else:
                self._insert_opr(value, parent_node.left)

        elif value > parent_node.value:
            if not parent_node.right:
                parent_node.right = Node(value, color='RED', parent=parent_node, left=self.T_NILL, right=self.T_NILL)
                self._insert_fix(parent_node.right)
            else:
                self._insert_opr(value, parent_node.right)

        else:
            print('Value already exists!')        

    def _insert_fix(self, node):  
            while node.parent.color == 'RED':
                # If the parent is the left child of its parent
                if node.parent == node.parent.parent.left:
                    y = node.parent.parent.right
                     # Case 1: If the uncle is red
                    if y.color == 'RED':
                        node.parent.color = 'BLACK'                           
                        y.color = 'BLACK'                                     
                        node.parent.parent.color = 'RED'                      
                        node = node.parent.parent                           
                    else:
                        # Case 2: If the uncle is black and the current node is the right child
                        if node == node.parent.right:
                            node = node.parent                              
                            self.rotate_left(node)  
                        # Case 3: If the uncle is black and the current node is the left child                                                                  
                        node.parent.color = 'BLACK'                           
                        node.parent.parent.color = 'RED'                      
                        self.rotate_right(node.parent.parent)              
                else:
                    y = node.parent.parent.left
                    if y.color == 'RED':
                        node.parent.color = 'BLACK'                           
                        y.color = 'BLACK'                                     
                        node.parent.parent.color = 'RED'                      
                        node = node.parent.parent                           
                    else:
                        if node == node.parent.left:
                            node = node.parent                              
                            self.rotate_right(node)                        
                        node.parent.color = 'BLACK'                           
                        node.parent.parent.color = 'RED'                      
                        self.rotate_left(node.parent.parent)               
            self.root.color = 'BLACK'




    # ----------------------------------------------------------------------------------------------------------------
    def delete( self, value) :
        if self.root:
            self._delete_opr(self.root , value)
        else:
            print("The tree is empty!")

    def _delete_opr( self , node , key ) :
        z = self.T_NILL
        while node != self.T_NILL :
            if node.value == key :
                z = node
            if node.value <= key :
                node = node.right
            else :
                node = node.left
        if z == self.T_NILL :
            print("Value does not exist!")
            return

        other_node = z
        other_node_original_color = other_node.color
        # Case 1: If the node to be deleted has only one child or no child
        if z.left == self.T_NILL :
            x = z.right
            self.replace( z , z.right )
        elif (z.right == self.T_NILL) :
            x = z.left
            self.replace( z , z.left )
         # Case 2: If the node to be deleted has two children
        else :
            other_node = self.get_min_node( z.right )
            other_node_original_color = other_node.color
            x = other_node.right
            if other_node.parent == z :
                x.parent = other_node
            else :
                self.replace( other_node , other_node.right )
                other_node.right = z.right
                other_node.right.parent = other_node

            self.replace( z , other_node )
            other_node.left = z.left
            other_node.left.parent = other_node
            other_node.color = z.color
        if other_node_original_color == 'BLACK' :    
            self._delete_fix( x )

    def _delete_fix( self , x ) :
        while x != self.root and x.color =="BLACK" :           
            if x == x.parent.left :
                s = x.parent.right
                # Case 1: If sibling is red
                if s.color == "RED" :
                    s.color = "BLACK"
                    x.parent.color = "RED"
                    self.rotate_left(x.parent)
                    s = x.parent.right
                # Case 2: If both children of sibling are black
                if s.left.color == "BLACK" and s.right.color == "BLACK" :
                    s.color = "RED"
                    x = x.parent
                else :
                     # Case 3: If the right child of sibling is black
                    if s.right.color == "BLACK" :
                        s.left.color = "BLACK"
                        s.color = "RED"
                        self.rotate_right(s)
                        s = x.parent.right

                    # Case 4: If the left child of sibling is black
                    s.color = x.parent.color
                    x.parent.color = "BLACK"
                    s.right.color = "BLACK"

                    self.rotate_left(x.parent)     
                    x = self.root

            else :      
                s = x.parent.left
                if s.color == "RED" :
                    s.color = "BLACK"
                    x.parent.color = "RED"

                    self.rotate_right(x.parent)       
                    s = x.parent.left

                if s.left.color == "BLACK" and s.right.color == "BLACK" :
                    s.color = "RED"
                    x = x.parent
                else :
                    if s.left.color == "BLACK" :
                        s.right.color = "BLACK"
                        s.color = "RED"

                        self.rotate_left(s)        
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = "BLACK"
                    s.left.color ="BLACK"
                    self.rotate_right(x.parent)
                    x = self.root
        x.color = "BLACK"

    # ----------------------------------------------------------------------------------------------------------------
    def get_min_value(self):
        if self.root:
            node = self.root
            while node.left:
                node = node.left
            return node.value
        else:
            print('The tree is empty!\n')


    # ----------------------------------------------------------------------------------------------------------------      
    def get_max_value(self):
        if self.root:
            node = self.root
            while node.right:
                node = node.right
            return node.value
        else:
            print('The tree is empty!\n')

    
    # ----------------------------------------------------------------------------------------------------------------
    def search(self, value):
        if self.root:
            return self._search_opr(value, self.root)
        else:
            return "False"

    def _search_opr(self, value, current_node):
        if value == current_node.value:
            return "True"
        elif value < current_node.value and current_node.left:
            return self._search_opr(value, current_node.left)
        elif value >  current_node.value and current_node.right:
            return self._search_opr(value, current_node.right)
        else:
            return "False"

         

    

rb_tree = RBTree()

for i in input().split(" "):
    rb_tree.insert(int(i))
rb_tree.show()
print(" ", end='\n')


while True:
    for i in range(int(input())):
        operation = input().split(" ")
        if operation[0] == "Delete":
            rb_tree.delete(int(operation[1]))
            rb_tree.show()
        elif operation[0] == "Insert":
            rb_tree.insert(int(operation[1]))
            rb_tree.show()
        elif operation[0] == "Min":
            print(rb_tree.get_min_value())
        elif operation[0] == "Max":
            print(rb_tree.get_max_value())
        elif operation[0] == "Search":
            print(rb_tree.search(int(operation[1])))
        else:
            print("Invalid Operation!\n")
        print(" ", end='\n')


