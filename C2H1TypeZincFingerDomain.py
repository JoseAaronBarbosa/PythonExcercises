def IsInTheDomain(Protein):
    Aminoacids = ['C','A','V','L','I','M','G','R','K','H','D','E','N','Q','S','T','Y','F','W','P',]
    stack = list(Protein.upper())
    counter = 0
    if not stack:   # If list is empty
        return False 
    if stack.pop() != 'H': # Take last character and if not H return false
        return False
    if stack: # If list not empty
        while stack.pop() != 'H': # Take last character until H, count characters
            counter += 1
    if counter != 3 and counter != 4 and counter != 5: # If not 3 to 5 characters between H's return false
        return False
    if len(stack) < 9: # If list long enough to make operations
        return False
    for _ in range(8): # Pop 8 characters
        stack.pop()
    if stack.pop() not in ['L','I','V','M','F','Y','W','C','X']: # Check if remaining is :
        return False
    if len(stack) < 4: # If list long enough to make operations
        return False
    for _ in range(3): # Pop 3 characters
        stack.pop()
    if stack.pop() != 'C': # Check if remaining is :
        return False
    counter = 0
    if stack: # If list not empty
        while stack.pop() != 'C': # Take last character until C, count characters
            counter += 1
    if counter != 2 and counter != 3 and counter != 4: # If not 3 to 5 characters between H's return false
        return False
    if stack: # If there are still characters return false
        return False
    return True

Protein = "CAASCGGPYACGGWAGYHAGWH"

print(IsInTheDomain(Protein))