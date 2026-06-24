import pgzrun
import random
HEIGHT=600
WIDTH=600
snake=Actor("snake")
apple=Actor("apple")
snake.pos=100,100
apple.pos=500,500
score=0
def draw():
    screen.fill("green")
    snake.draw()
    apple.draw()
    screen.draw.text(str(score),(10,10))
def update():
    global score
    if keyboard.a:
          snake.x-=5
    if keyboard.d:
         snake.x+=5
    if keyboard.w:
         snake.y-=5
    if keyboard.s:
         snake.y+=5
    if snake.colliderect(apple):
         apple.x=random.randint(80,520)
         apple.y=random.randint(80,520)
         score+=1


         
         



pgzrun.go()
