from turtle import Turtle, Screen
import random
SCREEN = Screen()


def main():
    keep_racing = False
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    turtles = {}
    SCREEN.setup(width=500, height=400, startx=None, starty=None)
    setup_race()
    start_num = -100
    for turtle in colors:
        turtles[turtle] = Turtle(shape='turtle')
        turtles[turtle].color(turtle)
        turtles[turtle].penup()
        turtles[turtle].goto(-200, start_num)
        start_num += 40
    bet = get_bet(colors)
    turtle_race(turtles)
    winner = check_winner(turtles)
    if bet == winner:
        print("Congrats! You win!")
    else:
        print("You lose")

    SCREEN.exitonclick()


def setup_race():
    setup = Turtle()
    setup.hideturtle()
    setup.penup()
    setup.goto(210, 150)
    setup.pendown()
    setup.setheading(270)
    setup.forward(300)


def get_bet(colors):
    bet = SCREEN.textinput(title="Make a bet", prompt="Bet on a turtle to win the race. (red, orange, yellow, green, "
                                                      "blue, purple.")
    while bet not in colors:
        bet = SCREEN.textinput(title="Make a bet", prompt="Please bet on an eligible turtle.")
    return bet


def turtle_race(turtles):
    keep_racing = True
    while keep_racing:
        for turtle in turtles:
            rand_distance = random.randint(1, 10)
            turtles[turtle].forward(rand_distance)
            if turtles[turtle].xcor() > 200:
                keep_racing = False


def check_winner(turtles):
    leader = 0
    winner = 0
    for turtle in turtles:
        if turtles[turtle].xcor() > leader:
            leader = turtles[turtle].xcor()
            winner = turtles[turtle]
    return winner


if __name__ == "__main__":
    main()