from turtle import Turtle, Screen
ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')


class Farewell(Turtle):

    def __init__(self, userinput):
        super().__init__()
        screen = Screen()
        screen.setup(width=600, height=600)
        screen.bgcolor("black")
        screen.title("Good Bye My Snake")
        self.color("blue")
        self.hideturtle()
        self.penup()
        self.input = userinput
        # Based on user input, provide corresponding ending screen
        if self.input.lower() == 'y':
            self.restart_ending()
        elif self.input.lower() == 'n':
            self.ending_ending()
        else:
            self.third_ending()

    def restart_ending(self):
        self.setpos(-25, -25)
        self.write("""
        The journey ends, \n
        You lost the game, \n
        The developer may have been lazy, \n
        This option could be easier, \n
        But you could always restart yourself. \n
        (Click to Exit)        
        """, False, align=ALIGNMENT, font=FONT)

    def ending_ending(self):
        self.setpos(-20, -25)
        self.write("""
        The journey ends, \n
        You lost the game, \n
        This may be the end, \n
        Maybe one day we meet again, \n
        When you are a brand new snake. \n
        (Click to Exit)
        """, False, align=ALIGNMENT, font=FONT)

    def third_ending(self):
        self.setpos(-30, -25)
        self.write("""
        Oh my friend, \n
        you always seek A third option, \n
        But life's choices are not so grand \n
        You only had two options earlier \n
        You missed them \n
        Farewell, my friend. \n
        (Click to Exit)
        """, False, align=ALIGNMENT, font=FONT)






