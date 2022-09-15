def drawSymbolPlot(func, bottom_edge, top_edge, string_count):
    oll_x = [bottom_edge + string*((top_edge - bottom_edge) / (string_count)) for string in range(string_count+1)]
    oll_y = [int(func(x)) for x in oll_x]
    
    left_edge = min(oll_y)
    for y in oll_y:
        pos = y - left_edge
        print(' ' * pos + '*')
        print()
        
    print()
    print()
