import numpy as np


def make_matrix(graph_input):

    '''
    converst list of lists into a matrix padded with zeros
    
    for some reason it modifies the graph_input data
    '''
    myarray = []
    
    graph_input_copy = graph_input.copy()
    for count, i in enumerate(graph_input_copy):

        zeros = np.zeros(len(graph_input_copy)-count-1)

        i.extend(zeros)
        myarray.append(i)
    return(np.array(myarray))



class MyGraph:
    
    def __init__(self, node_value, position):
        self.node_value = node_value
        self.position = position

    def add_left_child(self, new_left_child):
        
        self.left_child = new_left_child
        
    def add_right_child(self, new_right_child):
        
        self.right_child = new_right_child
        
        
class GraphDict:

    def __init__(self, matrix, MyGraph):
        
        self.matrix = matrix
        self.graph_dict = {}
        self.MyGraph = MyGraph
        
    def fill_graph_dict(self):

        for row in range(self.matrix.shape[0]):
            for col in range(self.matrix.shape[1]):
                if col <= row:

                    self.graph_dict[(row, col)] = self.MyGraph(node_value=self.matrix[row, col], position= (row, col))
                    
    def add_children(self):
        
        for graph_object in self.graph_dict.keys():
     
    
            row = self.graph_dict[graph_object].position[0]
            col = self.graph_dict[graph_object].position[1]

            if row == self.matrix.shape[0]-1:


                self.graph_dict[graph_object].add_left_child(new_left_child = 'leaf_node')
                self.graph_dict[graph_object].add_right_child(new_right_child = 'leaf_node')

            else:

                self.graph_dict[graph_object].add_left_child(new_left_child = self.graph_dict[(row+1, col)])
                self.graph_dict[graph_object].add_right_child(new_right_child = self.graph_dict[(row+1, col+1)])




