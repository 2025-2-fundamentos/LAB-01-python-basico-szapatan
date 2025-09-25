import csv

def loadfile(filename:str="files/input/data.csv"):
    """load file\n
        return list of strings separated by \t
    """
    #//return a list by values separated by \t
    data=[]
    with open(filename, newline='', encoding="utf-8") as f:
        reader=csv.reader(f,delimiter="\t")
        for row in reader:
            data.append(row)
    return data

def mapper(data:list,map_line:any):
    """
    Mapper\n
    procces the each line and retrieve only the required data
    Args:
        data: list of lists where each inner list is a row
        map_line: a function that takes a row and returns a list
    """
    sequence=[pair for sublist in map(map_line,data) for pair in sublist]
    return sequence

def shuffle_sort(x:list,reversed:bool, keys:any):
    """# Function: shuffle_sort
        # Description: Sorts a list of items based on a specified key and direction (ascending or descending).
        #              The function modifies the input list in-place and returns the sorted list.
        # 
        # Args:
        #     x (list): A list of items (typically tuples or dictionaries) to be sorted.
        #               Each item should be a tuple or object with a key that can be accessed by index or key.
        #     reversed (bool): If True, sorts in descending order; if False, sorts in ascending order.
        #     keys (callable or any): A key function (e.g., lambda) that defines how to extract or compute the sort key from each item.
        #                          If a callable (like lambda row: row[1]), it is applied to each element.
        # 
        # Returns:
        #     list: The sorted list of items, modified in-place according to the key and direction.
        # 
        # Example:
        #     >>> data = [("b", 2), ("a", 1), ("c", 3)]
        #     >>> shuffle_sort(data, reversed=False, keys=lambda x: x[1])
        #     [('a', 1), ('b', 2), ('c', 3)]"""
    x.sort(reverse=reversed,key=keys)
    return x

def reducer(x,minmax:bool=False):
    """ Function: reducer
         Description: Aggregates a list of key-value pairs (e.g., from a map operation) by grouping consecutive entries 
                      with the same key and summing their values. Maintains the order of keys and accumulates values for the same key.
         
         Args:
             x (list): A list of tuples (key, value) where key is typically a string or number and value is a number to accumulate.
             minmax(bool): boolean, when is needed to return (key, max, min)
         Returns:
             list: A list of tuples where each tuple is (key, sum_of_values), grouped by the same key.
                    If a new key appears, it starts a new group; if the key matches the last key, the value is appended to the existing group.
         
         Example:
             >>> data = [("A", 10), ("A", 20), ("B", 30), ("B", 40)]
             >>> reducer(data)
             [('A', 30), ('B', 70)]"""
    data=[]
    for key, value in x:
        if data and key==data[-1][0]:
            if not minmax:
                data[-1]=(key,data[-1][1]+value)
            else:
                n_min=min(value,data[-1][2])
                n_max=max(value,data[-1][1])
                data[-1]=(key,n_max,n_min)
        else:
            if not minmax:
                data.append((key,value))
            else:
                data.append((key,value,value))
    return data