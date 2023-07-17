from turtle import Turtle ,Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
# print(user_bet)
color = ['red','yellow','orange','green','purple','blue']
y_postion = [-70,-40,-10,20,50,80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_postion[turtle_index])
    all_turtles.append(new_turtle)
    print(all_turtles)
print(all_turtles)        
if user_bet:
    is_race_on = True 

while is_race_on:
    for turtle in all_turtles:
        if  turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"you've won! The {winning_color} turtle is the winner!") 
            else:
                print(f"you've lost! The {winning_color} turtle is the winner!")
        turtle.fd(random.randint(1,10))                 

screen.exitonclick()