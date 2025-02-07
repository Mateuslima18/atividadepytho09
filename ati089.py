def increment_digits(digits):  
    n = len(digits)  
    
    
    digits[-1] += 1  
    
    
    for i in reversed(range(n)):  
        if digits[i] < 10:  
            return digits  
        digits[i] = 0  
        if i - 1 >= 0:  
            digits[i - 1] += 1  
    
     
    return [1] + digits 

 
print(increment_digits([1, 2, 3]))   
print(increment_digits([4, 3, 2, 1]))    
print(increment_digits([9]))