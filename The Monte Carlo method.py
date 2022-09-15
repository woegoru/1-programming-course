def monte_carlo_integration(func, bottom_edge, top_edge, point_count):
    y1 = sys.float_info.max
    y2 = -sys.float_info.max
    for k in range(1000):
        x = bottom_edge + ((top_edge - bottom_edge)/1000)*k
        if func(x) < y1:
            y1 = func(x)
        if func(x) > y2:
            y2 = func(x)
    S = 0
    for i in range(point_count):
        x = bottom_edge + random.random() * (top_edge - bottom_edge)
        y = y1 + random.random() * (y2 - y1)
        if y <= y1 + func(x):
            S = S + 1
    return(S/point_count) * (top_edge - bottom_edge) * (y2 - y1)
