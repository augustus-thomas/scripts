#!/bin/python3
#written with Eric Liu
def step(point1, point2):
    del_x = point2[0] - point1[0]
    del_y = point2[1] - point1[1]
    m = del_y / del_x
    
    #left to right
    if point1[0] < point2[0]:
        if abs(m) <= 1:
            increments = 1, m
        else:
            if m > 1:
                increments = 1/m , 1
            else:
                increments = -1/m , -1
    else:
        if abs(m) <= 1:
            increments = -1, -1*m
        else:
            if m > 1:
                increments = -1/m, -1
            else:
                increments = 1/m, 1
    return increments

def DDA(point1, point2):
    inc_x, inc_y = step(point1, point2)
    intermediate_points = []
    current_point = point1
    dimension = max(abs(point2[0] - point1[0]), abs(point2[1] - point1[1]))
    for i in range(dimension):
        intermediate_points.append(current_point)
        current_point = (current_point[0] + inc_x, current_point[1] + inc_y)
    intermediate_points.append(point2)
    
    for i in range(len(intermediate_points)):
        intermediate_points[i] = round(intermediate_points[i][0]), round(intermediate_points[i][1])
    
    return intermediate_points


