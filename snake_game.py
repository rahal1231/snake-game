import pgzrun
import random
HEIGHT=600
WIDTH=600
snake=Actor("snake")
apple=Actor("apple")
snake.pos=100,100
apple.pos=500,500
def draw():
    screen.fill("green")
    snake.draw()
    apple.draw()
def update():
    if keyboard.a:
          snake.x-=5
    if keyboard.d:
         snake.x+=5
    if keyboard.w:
         snake.y-=5
    if keyboard.s:
         snake.y+=5
         



pgzrun.go()
