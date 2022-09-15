def trapeze_integration(func, bottom_edge, top_edge, step_count):
    dx = (top_edge - bottom_edge) / step_count 
    s = 0 
    for i in range(0, step_count-1):
        x = bottom_edge + dx * i
        Si  =  dx  *  (abs(func(x  + dx)) + abs(func(x))) / 2
        s = s + Si
    return(s)
