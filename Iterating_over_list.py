# Iterating over lists

def count_odd(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 1:
            count += 1
    return count

def check_odd(numbers):
    for num in numbers:
        if num % 2 == 1:
            return True
    return False

def remove_odd(numbers):
    for num in numbers:
        if num % 2 == 1:
            numbers.remove(num)

def remove_odd2(numbers):
    remove = []
    for num in numbers:
        if num % 2 == 1:
            remove.append(numbers.index(num))
            
    for idx in remove:
        numbers.pop(idx)
        
def remove_odd3(numbers):
    remove = []
    for num in numbers:
        if num % 2 == 1:
            remove.append(num)
            
    for num in remove:
        numbers.remove(num)
        
def remove_odd4(numbers):
    newnums = []
    for num in numbers:
        if num % 2 == 0:
            newnums.append(num)
    return newnums
   
def remove_last_odd(numbers):
    has_odd = False
    last_odd = 0
    
    last_odd_index = 0
    for index in range(len(numbers)):        
        if numbers[index] % 2 == 1:
            has_odd = True
            last_odd_index = index
    
    if has_odd:
        numbers.pop(last_odd_index)
        
def remove_last_odd2(numbers):
    has_odd = False
    last_odd = 0
    
    index = 0
    last_odd_index = 0
    for num in numbers:        
        if num % 2 == 1:
            has_odd = True
            last_odd_index = index
        index +=1
            
    
    if has_odd:
        numbers.pop(last_odd_index)

def remove_last_odd3(numbers):
    has_odd = False
    last_odd = 0
    
    for index in range(len(numbers)-1, -1 ,-1):        
        if numbers[index] % 2 == 1:
            numbers.pop(index)
            return

        
def run():
    numbers = [1, 7, 2, 34, 8, 7, 2, 5, 14, 22, 93, 48, 76, 15, 7]
    print numbers
    remove_last_odd3(numbers)
    
    print numbers
    
run()

    
#run()