from turtle import Turtle, Screen
import random


race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make a bet", "Witch of the Turtles will win the race? Type a color: "
                                          "\nThe colors are: red, green, blue, purple, black, yellow")


def setup_turtle(name, colored, y):
    name = Turtle()
    name.shape("turtle")
    name.color(colored)
    name.penup()
    name.goto(-230, y)
    n_c.append(name)



names_list = ["tim", "tom", "jim", "lin", "tam", "pam"]
color_list = ["red", "green", "blue", "purple", "black", "yellow"]
y = 100
n_c = []
for i in range(0,6):
    setup_turtle(names_list[i], color_list[i], y)
    y -= 40

if user_bet:
    race_on = True

while race_on:
    for i in n_c:
        if i.xcor() > 230:
            win_color = i.pencolor()
            race_on = False
            if win_color == user_bet:
                print(f"You have won! The winning turtle is the {user_bet} turtle")
            else:
                print(f"You have lost! The winning turtle is the {win_color} turtle")
        random_move = random.randint(1, 8)
        i.forward(random_move)




screen.exitonclick()