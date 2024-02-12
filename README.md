<h1>Red Black Tree Implementation Using Python</h1>

Red-black trees are a variant of binary search trees with an additional field for each node to store its colour, which can be either red or black. By colour-coding the nodes according to certain constraints on all paths from the root to the leaves, red-black trees ensure that the length of the longest path is always less than double the length of the shortest path, making the tree approximately balanced. Hence, red-black trees are considered to be a type of self-balancing binary search tree.For a binary search tree to be a red-black tree, the following properties, known as the "red-black properties," must be satisfied in addition to the properties of a standard binary search tree.

1.	Every node must be either red or black.
2.	The root must always be coloured black.
3.	All leaves must be coloured black.
4.	Both children of a red node must be black.
5.	For all nodes, all paths from a given node to all its descendant leaves must contain the same number of black nodes.

Here in this script, I have implemented a red-black tree that adheres to the above rules using Python. This tree is capable of doing the following operations.
 - inset a value, 
 - delete a value
 - tree query operations; 
     - Search a value
     - find the maximum value
     - find the minimum value

