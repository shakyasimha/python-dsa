from .stack import Stack 

"""
    Stack implementation: checking delimiters
"""
def is_matched(expr):
    lefty = '({['
    righty = ')}]'
    s = Stack() 
    
    for c in expr:
        if c in lefty: 
            s.push(c)
        elif c in righty: 
            if s.is_empty():
                return False 
            if righty.index(c) != lefty.index(s.pop()):
                return False 
            
    return s.is_empty()