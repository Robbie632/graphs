class Stack:
    
    '''
    class for constructing a stack structure
    '''
    
    def __init__(self):
        self.items = []
        
    def push(self, item):
        
        '''
        adds item to top of list
        '''
        
        self.items.append(item)
        
    def pop(self):
        
        '''
        removes item from top of list
        '''
        
        return(self.items.pop())
    
    def peek(self):
        
        '''
        returns most recent vlue without mofifying stack
        '''
        
        return(self.items[len(self.items)-1])
    
    def size(self):
        
        '''
        returns length of stack
        '''
        return(len(self.items))
    
    def is_empty(self):
        
        '''
        checks if stack is empty
        '''
        
        if len(self.items) == 0:
            return(True)
        else:
            return(False)
    
    
def is_balanced(stack_object, bracket_string):
    
    '''
    determines whether a string contains balanced parantheses
    
    Input: 
        
        bracket_string : string, contains string to be analysed
    
    Returns:
    
        Boolean, if True then parenthese balanced if not then unbalanced
    '''
    
   
    opening_brackets = ['{', '[', '(']

    closing_brackets = ['}', ']', ')']

    for i in bracket_string:

        if i in opening_brackets:
            stack_object.push(i)
            
        elif i in closing_brackets:
            stack_object.pop()
            
        else:
            continue
            
    return(stack_object.is_empty())