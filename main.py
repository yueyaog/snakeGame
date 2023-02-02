from turtle import Screen
from bin.snake import Snake
from bin.food import Food
from bin.scoreboard import Scoreboard
from bin.farewell import Farewell
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard(0)

screen.update()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision with Food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect Collision with Wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

        restart_option = screen.textinput(title="Restart", prompt="Would you like to restart the snake game (Y/N)?")
        screen.clear()
        farewell = Farewell(restart_option)

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
            restart_option = screen.textinput(title="Restart", prompt="Would you like to restart the snake game (Y/N)?")
            screen.clear()
            farewell = Farewell(restart_option)

screen.exitonclick()
