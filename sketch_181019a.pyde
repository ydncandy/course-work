x = 0
def setup():
    size(1154, 500)
    
def draw():
    global x
    x += 1
    background(240,157,32)
    fill(255,79,56)
    noStroke()
    ellipse(577,500,100,100)
    
    ellipse(x ,250,50,50)
    ellipse(x + 20,235,50,50)
    ellipse(x + 5,210,50,50)
    ellipse(x - 10, 245 ,50, 50)
    
    
