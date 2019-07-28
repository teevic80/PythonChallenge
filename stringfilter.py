#This is afunction that takes a list of non-negative integers and strings and returns a new list with the strings filtered out. 

def filter_list(l):
    num_list = [i for i in l if type(i) == int]
    return num_list
    
print(filter_list([1,2,'a','b']))
