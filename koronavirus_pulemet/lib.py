def angleToMouse(x,y):
    vec1  = dict(x = 0 ,y = 1)    
    dx = mouseX-x
    dy = mouseY-y
    n = sqrt(dx*dx+dy*dy)        
    vec2  = dict(x = dx/n, y = dy/n)    
    dot_ = vec1['x']*vec2['x'] + vec1['y']*vec2['y']
    n = abs(sqrt(vec1['x']*vec1['x']+vec1['y']*vec1['y']) * \
            sqrt(vec2['x']*vec2['x']+vec2['y']*vec2['y']))    
    r = 1
    if mouseX-x > 0:
        r = -1
    return degrees(r*acos(dot_ /n))
