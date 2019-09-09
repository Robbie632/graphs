'''
recursive functions for searching binary trees
'''


def preorder_binary_search(node, output = None):
    
    '''
    function that carries out preorder search of complete binary tree
    
    Input:
    
        node : MyNode object, node corresponding to the node at the top of the binary tree 
    
    Output:
    
        output : list, contains node values in order as would be expected from preorder binary tree search
    '''
 
    if output is None:
        output = []

    
    if node.left_child == 'leaf_node':
        output.append(node.node_value)
        return(output)
    
    else:
        
        output.append(node.node_value)
        output = preorder_binary_search(node = node.left_child, output = output)
        
        return(preorder_binary_search(node = node.right_child, output = output))
    
    
def inorder_binary_search(node, output = None):
    
    '''
    function that carries out ineorder search of complete binary tree
    
    Input:
    
        node : MyNode object, node corresponding to the node at the top of the binary tree 
    
    Output:
    
        output : list, contains node values in order as would be expected from inorder binary tree search
    '''
    
    if output is None:
        output = []

    
    if node.left_child == 'leaf_node':
        output.append(node.node_value)
        return(output)
    
    else:
        
        output = preorder_binary_search(node = node.left_child, output = output)
        output.append(node.node_value)        
        return(preorder_binary_search(node = node.right_child, output = output))