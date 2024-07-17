class TreeNode:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
    @staticmethod
    def parse_tuple(data):
        if isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
            return node
        elif data is None:
            return None
        else:
            return TreeNode(data)
    def display_keys(node,space='\t',level=0):
        if node is None:
            print(space*level+'@')
            return
        if node.left is None and node.right is None:
            print(space*level+ str(node.key))
            return
        TreeNode.display_keys(node.right,space,level+1)
        print(space*level+ str(node.key))
        TreeNode.display_keys(node.left,space,level+1)
        # print(space*level+ str(node.key))
    def tranverse_in_order(node): #inorder tranverse_in_order ( inter change mid to left value , it will be pre order, )
        if node is None:
            return[]
        return(TreeNode.tranverse_in_order(node.left) + [node.key]+ TreeNode.tranverse_in_order(node.right))
    def tree_height(node):
        if node is None:
            return 0
        return 1 + max(TreeNode.tree_height(node.left),TreeNode.tree_height(node.right))
    def size(node):
        if node is None:
            return 0
        return 1 + TreeNode.size(node.left) + TreeNode.size(node.right)
    def remove_nione(nums): #remove
        return [x for x in nums if x is not None]
    def is_bst(node):
        if node is None:
            return True,None,None
        is_bst_l,min_l,max_l= TreeNode.is_bst(node.left)
        is_bst_r,min_r,max_r= TreeNode.is_bst(node.right)
        is_bst_node=(is_bst_l and is_bst_r and (max_l is None or node.key> max_l),(min_r is None or node.key<min_r))
        min_key=min(TreeNode.remove_none([min_l,node.key,min_r]))
        max_key=max(TreeNode.remove_none([max_l,node.key,max_r]))
        return is_bst_node,min_key,max_key
tree2 = TreeNode.parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))
print(tree2)
print(tree2.left.key,",",tree2.right.right.key)
print(tree2.left.left.key,",",tree2.right.right.right.key)
TreeNode.display_keys(tree2,'  ')
print(TreeNode.tranverse_in_order(tree2)) 
print(TreeNode.tree_height(tree2))
print(tree2.size())
TreeNode.is_bst(tree2)
