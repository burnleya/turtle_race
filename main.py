import turtle
from turtle import Turtle
from random import choice


class TurtleRace:

    def __init__(self, turtle_competitors):
        self.turtle_competitors = turtle_competitors
        self.random_move_list = [5, 10]
        self.turtle_player_choice = ""
        self.turtle_winner = ""

    def move_random_turtle(self):
        race_complete = False
        while not race_complete:
            random_turtle = choice(self.turtle_competitors)
            random_move = choice(self.random_move_list)
            random_turtle.turtle.forward(random_move)
            race_complete = self.who_won()

    def who_won(self):
        winning_position = 780
        for turtles in self.turtle_competitors:
            print(turtles.turtle.pos()[0])
            if turtles.turtle.pos()[0] >= winning_position:
                self.turtle_winner = turtles.name
                return True

    def who_will_win(self):
        list_of_names = []
        for turtles in self.turtle_competitors:
            list_of_names.append(turtles.name)
        choice_complete = False
        while not choice_complete:
            self.turtle_player_choice = turtle.textinput("Which Turtle will win",
                                                         f"Please chose a turtle from the following list"
                                                         f" {list_of_names}")
            if self.turtle_player_choice in list_of_names:
                choice_complete = True

    def correct_guess(self):
        if self.turtle_player_choice == self.turtle_winner:
            turtle.write(
                f"Congrats, you chose {self.turtle_winner} who won!!", align="right", font=("Arial", 15, "bold")
            )
        else:
            turtle.write(
                    f"Unlucky, {self.turtle_winner} won but you chose {self.turtle_player_choice},"
                    f" who is slow even for a turtle!!", align="right", font=("Arial", 15, "bold")
            )

    def __str__(self):
        return f"Here are my turtles = {self.turtle_competitors}"


class Turtles:
    turtle.title("Turtle Olympics 100 millimeter Race")
    turtle.colormode(255)
    turtle.setup(1600, 400)
    turtle_num = 0
    turtle_positions = {1: (-790, -180),
                        2: (-790, -130),
                        3: (-790, -80),
                        4: (-790, -30),
                        5: (-790, 20),
                        6: (-790, 70),
                        7: (-790, 120),
                        8: (-790, 170)}
    turtle_colors = {1: "blue",
                     2: "red",
                     3: "dark slate blue",
                     4: "yellow",
                     5: "spring green",
                     6: "deep sky blue",
                     7: "light grey",
                     8: "deep pink"}

    def __init__(self, name):
        Turtles.turtle_num += 1
        self.name = name
        self.turtle = Turtle()
        self.shape = self.turtle.shape("turtle")
        self.color = self.turtle.color(Turtles.turtle_colors[Turtles.turtle_num])
        self.turtle.penup()
        self.pos_x = Turtles.turtle_positions[Turtles.turtle_num][0]
        self.pos_y = Turtles.turtle_positions[Turtles.turtle_num][1]
        self.turtle.setpos(self.pos_x, self.pos_y)


def main():
    andy = Turtles("Andy")
    thomas = Turtles("Thomas")
    karen = Turtles("Karen")
    myra = Turtles("Myra")
    judith = Turtles("Judith")
    peter = Turtles("Peter")
    hollie = Turtles("Hollie")
    john = Turtles("John")
    my_turtles = [andy, thomas, karen, myra, judith, peter, hollie, john]
    turtle_olympics = TurtleRace(my_turtles)
    turtle_olympics.who_will_win()
    turtle_olympics.move_random_turtle()
    turtle_olympics.correct_guess()
    print(turtle_olympics.turtle_player_choice)
    print(turtle_olympics.turtle_winner)
    turtle.mainloop()


if __name__ == '__main__':
    main()