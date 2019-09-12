'''
functions to increase CNN understanding and transparency
'''


def get_conv_output_dims(input_dim, kernel_dim, padding, stride):
    
    '''
    calculates the width or length of output tensor after doing 2d convolution or max pooling with inputted paramaters
    '''
    
    return(((input_dim - kernel_dim + (2*padding)) / stride) + 1)


def get_number_weights_biases(input_dim, kernel_dim, padding, stride, no_input_channels, no_kernels):
    
    '''
    calculates the number of weights and biases after doing 2d convolution or max pooling with inputted paramaters
    '''
        
    kernel_squared = kernel_dim**2
    
    num_weights = kernel_squared *  no_input_channels * no_kernels
    
    num_biases = no_kernels
                              
    return(num_weights, num_biases)

