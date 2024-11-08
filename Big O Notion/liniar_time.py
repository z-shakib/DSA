'''
Runtime increases at a linear rate with input size.
'''

def contains_value(arr, value): 
    for item in arr: 
        if item == value: 
            return True
    
    return False

arr = [2,4,7,12,19,23,34,45,56,67,89]
print(contains_value(arr, 4))