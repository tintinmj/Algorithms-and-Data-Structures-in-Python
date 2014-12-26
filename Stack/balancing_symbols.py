def checkSymbolBalance(string):
    """ Parameter @string : the input string to be checked
       Returns : True if the input string contains symbols that is balanced
                else False if not
         """
    symbols ={'{':'}','[':']','(':')'}
    stack =[]
    for x in string:  
        if symbols.has_key(x):
            stack.append(x)
        if x in symbols.values():
            if len(stack)>0 and symbols[stack[-1]] == x:
                stack.pop()
            else:
                return False
    return stack == []

if __name__ == "__main__":
    """Driver routine to simulate the function of checkSymbolbalance"""
    print checkSymbolBalance("{{{{{{{}}}}}}}")
    print checkSymbolBalance("((((()))]")
    print checkSymbolBalance("{(())}{}[[]]()")              
        
        
        
        
    
    
    
    
    
    
    
    
