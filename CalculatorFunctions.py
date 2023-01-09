
def polynomial_function():
    # receive the function that user needs the roots from
    function = input("Digite a função aqui: ")
    return function

def fixed_break():
    # fixed search break edges and increase
    # can be changed for more or less precision
    start = -50
    end = 50
    increase = 0.5
    
    # defining the search break
    counter = 0
    while start <= end:
        counter += 1
        start += increase
    start = -50
    return start, end, increase, counter

def find_values(counter, start, increase, function):
    # define the break where it's going to search signal
    # changes 
    
    x_values = []
    y_values = []
    x = start
    for _ in range(counter):
        y = eval(function)
        x_values.append(x)
        y_values.append(y)
        x += increase
    return x_values, y_values

def identifier (x_values, y_values):
    # find the breaks where there are signal changes at the
    # results of y in function of x
    
    break_a = []
    break_b = []
    for p,_ in enumerate(y_values):
        if p > 0:
            if (y_values[p]<0 and y_values[(p-1)]>0) or (y_values[p]>0 and y_values[(p-1)]<0):
                break_a.append(x_values[(p-1)])
                break_b.append(x_values[p])
    
    change_breaks = tuple(zip(break_a, break_b))
    change_breaks = list(map(list,change_breaks))
    return change_breaks

def refiner (change_breaks, function):
    # consists in reduce each find break in identifier until 
    # comply with the given convergence criterion to find the
    # equation root approximation
    
    # convergence criterion is changeble
    criterion = 10**(-6)
    roots = []
    
    for p,_ in enumerate(change_breaks):
        # get the pair in change breaks
        root_point = change_breaks[p]
        
        # get first point
        x1 = root_point [0]
        x = x1
        y1 = eval(function)
        
        # get second point 
        x2 = root_point [1]
        x = x2
        y2 = eval(function)

        # change the pair order if it has different order of number signs
        if y2 < y1:
            x1 = root_point [1]
            x2 = root_point [0]

        # start the refinement
        while abs(x1-x2) > criterion:
            x = (x1+x2)/2 #average
            y = eval(function)
            if y < 0:
                x1 = x
            else:
                x2 = x
        
        # include x value in roots group when find it
        roots.append(round(x,9))  
    return roots
