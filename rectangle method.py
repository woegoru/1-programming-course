def rectangle_integration(func, bottom_edge, top_edge, step_count):
    dx = (top_edge - bottom_edge) / step_count 
    s = 0 
    for i in range(step_count):
        x = bottom_edge + dx * i
        Si = dx * abs(func(x))
        s = s + Si
    return(s)
