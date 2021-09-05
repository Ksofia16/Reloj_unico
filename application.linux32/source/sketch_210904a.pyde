k = 0
s = 0
def setup ():
    size (500, 500)
def draw ():
    background(1, 1, 1) 
    fill ( 62, 113, 237) 
    square ( width/ 2.5 , k, 100)
    fill ( 98, 66, 155)
    square ( width / 1.5, s, 100)
    if  k > width: 
        k = 0
    else: 
        k = map ( second (), 0, 59, 0, width) 
    if  s > width: 
        s = 0
    else :
        s= map( minute(), 0 ,59, 0 , width) 
    global k
    global s

    
        
    
