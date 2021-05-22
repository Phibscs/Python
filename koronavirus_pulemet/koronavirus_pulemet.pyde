import lib
class Gun:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.angle = 0
        self.image_ = loadImage("pulemet.png")
    def  draw_(self):
        push()
        angle = lib.angleToMouse(self.x,self.y)
        translate(self.x,self.y)
        rotate(radians(angle))
        image(self.image_,0,0)
        pop()
    def rotation(self):
        self.angle = lib.angleToMouse(self.x , self.y)
class Pulia:
    def __init__(self,x,y,x1,y1):
        
        self.x = x
        self.y = y
        self.dx = float(x1-x)/100
        self.dy = float(y1-y)/100
        
        print(x , y , x1,y1 , self.dx , self.dy )
        self.image__ = loadImage("pulemet.png")
    def  draw_(self):
        push()
        angle = lib.angleToMouse(self.x,self.y)
        translate(self.x,self.y)
        rotate(radians(angle))
        scale(0.1)
        image(self.image__,0,0)
        pop()
    def move(self):
        self.x += self.dx
        self.y += self.dy
class Maska:
    def __init__(self):
        self.x = random(0,600)
        self.y = -50
        self.speed = random(1,3)
        self.image__ = loadImage("medical-mask.png")
    def draw_(self):
        push()
        translate(self.x,self.y)
        scale(0.1)
        image(self.image__,0,0)
        pop()
    def move(self):
        self.y += self.speed
bullets =[]
masks = []
c = 0
state = 0
def menu():
    img = loadImage("4845455.jpg")
    image(img,300,350)
    fill(255,0,0)
    rect(265,188,72,20)
    rect(265,635,30,20)
    fill(0)
    text("Start game",270,200)
    text("Exit", 270,650)
def setup():
    global gun,masks
    gun = Gun(300,700)
    imageMode(CENTER)
    size(600,700)
def draw():
    background(237,255,0)
    global bullets, c, state,masks
    
    if state == 0:
        menu()
        if mouseX>265 and mouseY>188 and mouseX<337 and mouseY<208 and mousePressed:
            state += 1
        elif mouseX>265 and mouseY>635 and mouseX<295 and mouseY<655 and mousePressed:
            exit()
    elif state == 1:
        for z in range(0,50,2):
            if c*c == z*z and len(masks) == z/2 :
                masks.append(Maska())
        
        gun.draw_()
        gun.rotation()
        for bullet in bullets:
            bullet.move()
            bullet.draw_()
            for maska in masks:
                dx = maska.x - bullet.x
                dy = maska.y - bullet.y
                if sqrt(dx*dx+dy*dy) < 50:
                    maska.y = -random(50,150)
                    maska.x = random(20,580)
                    c += 1
        for maska in masks:
            maska.draw_()
            maska.move()
            if maska.y >700:
                state = 3
        for index in range(len(bullets)-1 , -1 , -1 ):
            if bullets[index].y <= 0:
                del bullets[index]
        
        push()
        fill(0)
        textSize(40)
        text(c,0,30)
        pop()
        if keyPressed:
            if key == TAB:
                state = 2
    elif state == 2:
        if keyPressed:
             if key == 'a':
                state = 1
    elif state == 3:
        background(255,0,0)
        textSize(30)
        f = loadFont("Constantia-BoldItalic-30.vlw")
        textFont(f)
        text("YOU DIED!",230,350)
        if key == ESC:
            exit()
def keyPressed():
    global gun
    if keyCode == LEFT:
        gun.x -= 1
    if keyCode == RIGHT:
        gun.x += 1
    if key == ' ':
        bullets.append(Pulia(gun.x , gun.y , mouseX , mouseY))
        
