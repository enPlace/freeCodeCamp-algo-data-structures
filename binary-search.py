def binary_search(listy, target): 
    first = 0
    last = len(listy)-1
    while first <=last:
        midpoint = (last+first)//2

        if listy[midpoint] == target: 
            return midpoint

        elif listy[midpoint] > target: 
            last = midpoint-1

        elif listy[midpoint]<target: 
            first = midpoint+1

    return "item not found"



print(binary_search([1,2,3,4,5,6,7,8,9,10], 7))