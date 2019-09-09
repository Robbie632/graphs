import numpy as np


def make_matrix(graph_input):

    '''
    converst list of lists into a matrix padded with zeros
    
    for some reason it modifies the graph_input data
    
    Input:
    
        graph_input : list, list of lists containing inputs for graph
        
    '''
    myarray = []
    
    graph_input_copy = graph_input.copy()
    bottom_row_length = 2**(len(graph_input_copy)-1)
    for count, i in enumerate(graph_input_copy):

        zeros = np.zeros( bottom_row_length - 2**(count))

        i.extend(zeros)
        myarray.append(i)
    return(np.array(myarray))



class MyNode:
    
    '''
    class for constructing nodes
    
    Input: 
    
        node_value : int or string, value for node
        
        position : tuple, (row, col) encoding node position
    
    '''
    
    def __init__(self, node_value, position):
        
        self.node_value = node_value
        self.position = position
        
        '''
        init for MyGraph Class
        '''

    def add_left_child(self, new_left_child):
        
        '''
        add left child to present node object
        
        Input: 
        
        new_left_child :  MyNode object
        '''
        
        self.left_child = new_left_child
        
    def add_right_child(self, new_right_child):
        
        '''
        add right child to present node object
        
        Input: 
        
        new_right_child :  MyNode object
        '''
        
        self.right_child = new_right_child
        
    
    #def add_parent(self, new_parent):

       # '''
       # add parent to present node object
        
       # Input: 
        
       # new_parent :  MyNode object
        
        
        #self.parent = new_parent
     
        
class GraphDict:
    
    '''
    class for holding nodes representing a binary tree in a graph
    
    Input:
    
        matrix : numpy matrix, matrix containing binary tree padded with zeros
        
        graph_dict : dictionary, keys are tuples containing node coordinates, values are myNode objects
        
        myNode : myNode object
    '''

    def __init__(self, matrix, MyNode):
        
        self.matrix = matrix
        self.graph_dict = {}
        self.MyNode = MyNode
        
    def fill_graph_dict(self):

        for row in range(self.matrix.shape[0]):
            for col in range(self.matrix.shape[1]):
                
                if col < 2**row:
                    print((row, col))

                    self.graph_dict[(row, col)] = self.MyNode(node_value=self.matrix[row, col], 
                                                              position= (row, col))
                    
    def add_children(self):
        
        '''
        adds children to myNode objects contained in graph_dict dictionary
        
        '''
        
        for graph_object in self.graph_dict.keys():
     
    
            row = self.graph_dict[graph_object].position[0]
            col = self.graph_dict[graph_object].position[1]

            if row == self.matrix.shape[0]-1:


                self.graph_dict[graph_object].add_left_child(new_left_child = 'leaf_node')
                self.graph_dict[graph_object].add_right_child(new_right_child = 'leaf_node')

            else:

                self.graph_dict[graph_object].add_left_child(new_left_child = self.graph_dict[(row+1, 2*col)])
                self.graph_dict[graph_object].add_right_child(new_right_child = self.graph_dict[(row+1, (2*col)+1)])




