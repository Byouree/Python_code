def isIn(char, aStr):
    if len(aStr) < 1:
        return False    
    elif len(aStr) == 1:
        return char == aStr
    
    else:     
        midIndex = len(aStr)//2
        midChar = aStr[midIndex]
        
        if char == midChar:
            return True
        elif char > midChar:
            return (isIn(char, aStr[midIndex+1:]))
        else:
            return (isIn(char, aStr[:midIndex]))
                

            
            
print(isIn('z','abc'))   
    
