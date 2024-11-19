from turtle import Turtle, Screen
import random

# Initialize race status
race_on = False
screen = Screen()
screen.setup(500, 400)

# Ask the user to bet on a turtle color
user_bet = screen.textinput(
    "Make a bet", 
    "Which of the Turtles will win the race? Type a color: \nThe colors are: red, green, blue, purple, black, yellow"
)

# Function to set up each turtle
def setup_turtle(name, colored, y):
    """
    Sets up a turtle with the specified name, color, and starting position.
    """
    name = Turtle()  # Create a new turtle
    name.shape("turtle")  # Set the shape to 'turtle'
    name.color(colored)  # Set the turtle's color
    name.penup()  # Lift the pen so it doesn't draw lines
    name.goto(-230, y)  # Set the starting position of the turtle
    n_c.append(name)  # Add the turtle to the list of turtles

# Lists to store turtle names and their corresponding colors
names_list = ["tim", "tom", "jim", "lin", "tam", "pam"]
color_list = ["red", "green", "blue", "purple", "black", "yellow"]
y = 100  # Starting Y position for the first turtle
n_c = []  # List to store the turtle objects

# Create the turtles and position them on the screen
for i in range(0, 6):
    setup_turtle(names_list[i], color_list[i], y)
    y -= 40  # Decrease Y position for the next turtle, so they don't overlap

# If the user made a bet, start the race
if user_bet:
    race_on = True

# Start the race if the race_on flag is True
while race_on:
    for i in n_c:
        if i.xcor() > 230:  # Check if any turtle has crossed the finish line
            win_color = i.pencolor()  # Get the color of the winning turtle
            race_on = False  # End the race

            # Print the result
            if win_color == user_bet:
                print(f"You have won! The winning turtle is the {user_bet} turtle.")
            else:
                print(f"You have lost! The winning turtle is the {win_color} turtle.")
        
        # Move the turtle forward by a random amount
        random_move = random.randint(1, 8)
        i.forward(random_move)

# Wait for the user to click on the screen to exit
screen.exitonclick()
